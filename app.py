import os
from flask import Flask
import pandas as pd
import plotly.express as px
from neo4j import GraphDatabase

app = Flask(__name__)

driver = GraphDatabase.driver(
    os.getenv("NEO4J_URI", "bolt://localhost:7687"),
    auth=("neo4j", "neo4j123")
)

def run_query(query):
    with driver.session() as session:
        result = session.run(query)
        return pd.DataFrame([dict(r) for r in result])


@app.route("/")
def dashboard():

    # -------------------------------
    # SUPER-SPREADERS
    # -------------------------------
    df1 = run_query("""
        MATCH (p:Person)-[:CONTACT]->()
        RETURN p.name AS name, COUNT(*) AS degree
        ORDER BY degree DESC LIMIT 10
    """)

    fig1 = px.bar(df1, x="name", y="degree",
                  title="Top Super Spreaders")

    # -------------------------------
    # HOTSPOTS
    # -------------------------------
    df2 = run_query("""
        MATCH (p:Person)
        RETURN p.location AS location, COUNT(*) AS cases
        ORDER BY cases DESC
    """)

    fig2 = px.bar(df2, x="location", y="cases",
                  title="Hotspot Locations")

    # -------------------------------
    # SAFE LOCATIONS
    # -------------------------------
    df3 = df2.sort_values(by="cases").head(5)

    fig3 = px.bar(df3, x="location", y="cases",
                  title="Safe Locations")

    # -------------------------------
    # MAP VISUALIZATION
    # -------------------------------
    location_coords = {
     "Chennai": [13.0827, 80.2707],
     "Bangalore": [12.9716, 77.5946],
     "Hyderabad": [17.3850, 78.4867],
     "Delhi": [28.7041, 77.1025],
     "Mumbai": [19.0760, 72.8777],
     "Kolkata": [22.5726, 88.3639],
     "Pune": [18.5204, 73.8567],
     "Ahmedabad": [23.0225, 72.5714],
     "Jaipur": [26.9124, 75.7873],
     "Lucknow": [26.8467, 80.9462],
     "Coimbatore": [11.0168, 76.9558],
     "Madurai": [9.9252, 78.1198],
     "Trichy": [10.7905, 78.7047],
     "Visakhapatnam": [17.6868, 83.2185]
    }
    df2["lat"] = df2["location"].map(lambda x: location_coords.get(x, [0, 0])[0])
    df2["lon"] = df2["location"].map(lambda x: location_coords.get(x, [0, 0])[1])

    fig_map = px.scatter_mapbox(
        df2,
        lat="lat",
        lon="lon",
        size="cases",
        hover_name="location",
        title="Disease Spread Map",
        zoom=4
    )

    fig_map.update_layout(mapbox_style="open-street-map")

    # -------------------------------
    # CONTACT TABLE
    # -------------------------------
    df4 = run_query("""
        MATCH (a:Person)-[:CONTACT]->(b:Person)
        RETURN a.name AS From, b.name AS To, a.location AS Location
        LIMIT 20
    """)

    table_html = df4.to_html(index=False, classes="table")

    # -------------------------------
    # FULL DATA TABLE
    # -------------------------------
    df5 = run_query("""
        MATCH (p:Person)
        RETURN p.name AS Name, p.location AS Location
        LIMIT 20
    """)

    table2_html = df5.to_html(index=False, classes="table")

    # -------------------------------
    # RETURN HTML (FIXED INDENTATION)
    # -------------------------------
    return f"""
<html>
<head>
    <title>Epidemic Dashboard</title>

    <style>
        body {{
            font-family: Arial;
            background-color: #f4f6f9;
            margin: 20px;
        }}
        h1 {{
            text-align: center;
            color: #2c3e50;
        }}
        h2 {{
            color: #34495e;
        }}
        .card {{
            background: white;
            padding: 20px;
            margin-bottom: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        .btn {{
            display: block;
            width: 200px;
            margin: 20px auto;
            padding: 10px;
            background-color: #3498db;
            color: white;
            text-align: center;
            border-radius: 5px;
            text-decoration: none;
            font-weight: bold;
        }}
        .btn:hover {{
            background-color: #2980b9;
        }}
        .table {{
            width: 100%;
            border-collapse: collapse;
        }}
        .table th, .table td {{
            padding: 8px;
            border: 1px solid #ddd;
            text-align: center;
        }}
        .table th {{
            background-color: #2c3e50;
            color: white;
        }}
    </style>
</head>

<body>

    <h1>🚀 Epidemic Spread Analytics Dashboard</h1>

    <a href="/" class="btn">🔄 Refresh Dashboard</a>

    <div class="card">
        <h2>Top Super Spreaders</h2>
        {fig1.to_html(full_html=False)}
    </div>

    <div class="card">
        <h2>Hotspot Locations</h2>
        {fig2.to_html(full_html=False)}
    </div>

    <div class="card">
        <h2>Safe Locations</h2>
        {fig3.to_html(full_html=False)}
    </div>

    <div class="card">
        <h2>Geographical Spread</h2>
        {fig_map.to_html(full_html=False)}
    </div>

    <div class="card">
        <h2>Contact Relationships</h2>
        {table_html}
    </div>

    <div class="card">
        <h2>People Dataset</h2>
        {table2_html}
    </div>

</body>
</html>
"""


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
