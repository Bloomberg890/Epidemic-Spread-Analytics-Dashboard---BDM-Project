# \# 🚀 Epidemic Spread Analytics Dashboard (BDM Project)

# 

# A real-time big data analytics system that models and visualizes infectious disease spread using \*\*Kafka, Apache Spark, Neo4j, and Flask\*\*, deployed with \*\*Docker\*\*.

# 

# \---

# 

# \## 📌 Project Overview

# 

# This project implements an \*\*end-to-end real-time data pipeline\*\* to simulate and analyze epidemic spread using contact tracing data.

# 

# It leverages \*\*graph-based modeling\*\* to identify:

# 

# \* 🧍 Super-spreaders

# \* 📍 High-risk locations (hotspots)

# \* 🟢 Safe zones

# \* 🔗 Contact relationships

# 

# \---

# 

# \## 🏗️ System Architecture

# 

# ```

# Kafka (Streaming Data Source)

# &#x20;       ↓

# Spark Structured Streaming (Real-time ingestion)

# &#x20;       ↓

# ETL Processing (Cleaning \& Transformation)

# &#x20;       ↓

# Spark Analytics (Degree, Location Trends)

# &#x20;       ↓

# Neo4j Graph Database (Storage)

# &#x20;       ↓

# &#x20;       ┌───────────────────────────────┬───────────────────────────────┐

# &#x20;       ↓                               ↓

# Neo4j Bloom                      Flask Web App (Plotly Dashboard)

# (Graph Visualization)            (Charts \& Maps)

# &#x20;       ↓                               ↓

# Interactive Network              Bar Charts, Maps, Tables

# &#x20;       └───────────────┬───────────────────────────────┘

# &#x20;                       ↓

# &#x20;             Docker Deployment (AWS Ready)

# ```

# 

# \---

# 

# \## ⚙️ Tech Stack

# 

# \* \*\*Apache Kafka\*\* – Real-time data streaming

# \* \*\*Apache Spark (PySpark)\*\* – Streaming + ETL + Analytics

# \* \*\*Neo4j\*\* – Graph database for contact network

# \* \*\*Flask\*\* – Web application backend

# \* \*\*Plotly\*\* – Interactive visualizations \& maps

# \* \*\*Docker\*\* – Containerization

# \* \*\*Python\*\* – Core programming language

# 

# \---

# 

# \## 🔥 Features

# 

# \### 📊 Real-Time Data Processing

# 

# \* Simulated contact tracing using Kafka

# \* Continuous ingestion using Spark Structured Streaming

# 

# \### 🧹 ETL Pipeline

# 

# \* Data cleaning and transformation

# \* Schema-based structured processing

# 

# \### 📈 Spark Analytics

# 

# \* Degree Centrality (Super-spreaders)

# \* Location-based case aggregation (Hotspots)

# 

# \### 🕸️ Graph Modeling (Neo4j)

# 

# \* Individuals as nodes

# \* Contacts as relationships

# \* Query-based graph insights

# 

# \### 🌍 Visualization Dashboard

# 

# \* Bar charts (Top spreaders, hotspots, safe areas)

# \* Interactive Map (geographical spread)

# \* Contact relationship tables

# 

# \### 🐳 Deployment

# 

# \* Fully containerized using Docker

# \* Ready for AWS EC2 deployment

# 

# \---

# 

# \## 📂 Project Structure

# 

# ```

# epidemic\_project/

# │

# ├── app.py                 # Flask dashboard

# ├── spark\_stream.py        # Spark streaming + analytics

# ├── producer.py            # Kafka data generator

# ├── Dockerfile             # Docker configuration

# ├── requirements.txt       # Dependencies

# └── README.md

# ```

# 

# \---

# 

# \## 🚀 How to Run

# 

# \### 1️⃣ Start Kafka

# 

# ```bash

# zookeeper-server-start.sh config/zookeeper.properties

# kafka-server-start.sh config/server.properties

# ```

# 

# \---

# 

# \### 2️⃣ Run Kafka Producer

# 

# ```bash

# python producer.py

# ```

# 

# \---

# 

# \### 3️⃣ Run Spark Streaming

# 

# ```bash

# python spark\_stream.py

# ```

# 

# \---

# 

# \### 4️⃣ Start Flask App

# 

# ```bash

# python app.py

# ```

# 

# 👉 Open in browser:

# 

# ```

# http://127.0.0.1:5000

# ```

# 

# \---

# 

# \## 🐳 Run with Docker

# 

# \### Build Image

# 

# ```bash

# docker build -t epidemic-dashboard .

# ```

# 

# \### Run Container

# 

# ```bash

# docker run -p 5000:5000 epidemic-dashboard

# ```

# 

# \---

# 

# \## 🧠 Key Insights

# 

# \* Identifies \*\*super-spreaders\*\* using graph degree

# \* Detects \*\*hotspots\*\* based on location clustering

# \* Visualizes \*\*real-time epidemic spread\*\*

# \* Enables \*\*data-driven public health decisions\*\*

# 

# \---

# 

# \## 🌍 Real-World Applications

# 

# \* Public health monitoring

# \* Pandemic response systems

# \* Smart city health analytics

# \* Contact tracing platforms

# 

# \---

# 

# \## ⚡ Novelty

# 

# \* Graph-based epidemic modeling using Neo4j

# \* Integration of Spark Streaming with graph analytics

# \* Real-time visualization pipeline

# \* Combined use of \*\*big data + graph databases\*\*

# 

# \---

# 

# \## 📊 Future Enhancements

# 

# \* Machine Learning for outbreak prediction

# \* Real-time alerts for high-risk zones

# \* Advanced graph algorithms (community detection)

# \* Live dashboard updates without refresh

# 

# \---

# 

# \## 👩‍💻 Team

# 

# \* Shinigdapriya Sathish

# \* Yuvashree P H

# 

# \---

# 

# \## 📜 License

# 

# This project is for academic purposes under the Big Data Management Laboratory course.

# 

# \---

# 

# \## ⭐ Acknowledgment

# 

# Sri Sivasubramaniya Nadar College of Engineering

# ICS1612 – Big Data Management Laboratory



