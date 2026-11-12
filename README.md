# 🚕 Uber Data Engineering Pipeline | GCP

An end-to-end data engineering project that ingests, transforms, models, and analyzes NYC Yellow Taxi trip data using Google Cloud Platform (GCP), Mage AI, BigQuery, and Looker Studio.

The project demonstrates an ETL workflow, dimensional data modelling, cloud-based data warehousing, and interactive business intelligence reporting.

## 📌 Project Overview

This project implements a cloud-based data pipeline to process NYC Yellow Taxi trip records and transform raw data into an analytical data model.

The pipeline uses Mage AI to orchestrate data ingestion and transformation, Google Cloud services for storage and processing, BigQuery as the data warehouse, and Looker Studio for interactive visualization.

## 🏗️ Architecture

**Pipeline workflow:**

`NYC Taxi Dataset → Google Cloud Storage → Mage AI → Data Transformation → BigQuery → Looker Studio`

### Architecture Components

| Component | Purpose |
|---|---|
| NYC Yellow Taxi Dataset | Source trip records |
| Google Cloud Storage | Cloud data storage |
| Compute Engine | Hosted the Mage AI environment |
| Mage AI | ETL orchestration |
| Python & Pandas | Data cleaning and transformation |
| BigQuery | Cloud data warehouse |
| Looker Studio | Interactive dashboard and reporting |

## ⚙️ Data Engineering Workflow
<img width="1379" height="1091" alt="Blank diagram" src="https://github.com/user-attachments/assets/abf4fd66-5f1f-42de-8a6f-85f6a7b81976" />

### 1. Data Ingestion
- Ingested approximately 100,000 NYC Yellow Taxi trip records.
- Used Google Cloud Storage for cloud-based data storage.
- Configured Mage AI to load the source dataset into the pipeline.

### 2. Data Transformation
Performed data cleaning and transformation using Python and Pandas:

- Converted pickup and drop-off timestamps into datetime objects.
- Removed duplicate records and reset dataframe indexes.
- Generated unique trip identifiers.
- Extracted date and time attributes for analytical purposes.
- Created dimension tables and established relationships with the fact table.

### 3. Dimensional Data Modelling

Designed a **Star Schema** consisting of seven dimension tables and one fact table.

**Dimension Tables:**
1. `datetime_dim`
2. `passenger_count_dim`
3. `trip_distance_dim`
4. `rate_code_dim`
5. `pickup_location_dim`
6. `dropoff_location_dim`
7. `payment_type_dim`

**Fact Table:**
- `fact_table` – Contains 17 columns, including dimension keys and trip-level financial measures.

### 4. Data Warehousing
- Exported the transformed fact table to Google BigQuery.
- Used BigQuery as the analytical data warehouse.
- Configured cloud authentication and permissions for pipeline execution.

### 5. Data Visualization
Developed an interactive Looker Studio dashboard to analyze taxi trip patterns, revenue, payment methods, and passenger behaviour.

## 📊 Key Project Metrics

| Metric | Value |
|---|---:|
| Source records processed | 100,000 |
| Dimension tables | 7 |
| Fact tables | 1 |
| Fact table columns | 17 |
| Dashboard KPIs | 5 |

## 📈 Interactive Dashboard

Explore the dashboard:

**[View Live Looker Studio Dashboard] - https://datastudio.google.com/reporting/c3786204-d89f-415b-af67-27ea4601a248**

## 📄 Project Report

For a detailed overview of the project, implementation,
and dashboard analysis:

[View Uber Analysis Report (PDF)](https://github.com/user-attachments/files/34669461/Uber_Analysis_Report.2.pdf)

### Dashboard Features

- Total revenue and trip record count.
- Average trip distance, fare, and tip amount.
- Dynamic filters for vendor, payment type, rate code, and trip distance.
- Revenue and fare analysis.
- Pickup and drop-off location analysis.
- Passenger count and payment type distribution.

## 🛠️ Tech Stack

- **Programming:** Python
- **Data Processing:** Pandas
- **ETL Orchestration:** Mage AI
- **Cloud Platform:** Google Cloud Platform
- **Cloud Storage:** Google Cloud Storage
- **Compute:** Google Compute Engine
- **Data Warehouse:** Google BigQuery
- **Visualization:** Looker Studio
- **Version Control:** Git & GitHub

## 📁 Project Structure

```text
uber-data-engineering-gcp/
│
├── charts/
├── custom/
├── data_exporters/
├── data_loaders/
├── dbt/
├── extensions/
├── interactions/
├── pipelines/
├── scratchpads/
├── transformers/
├── utils/
│
├── README.md
├── requirements.txt
├── metadata.yaml
├── __init__.py
├── .gitignore
│
└── Uber_Analysis_Report.pdf
```

*Note: The structure above illustrates the main project components. Actual Mage-generated files and configuration may vary.*

## 🚀 Running the Project

1. Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/uber-data-engineering-gcp.git
cd uber-data-engineering-gcp
```

2. Create and activate a Python virtual environment.

3. Install the required dependencies:

```bash
pip install mage-ai pandas google-cloud-bigquery db-dtypes
```

4. Configure your Google Cloud project, BigQuery dataset, and authentication.

5. Configure the Mage project using your own secure `io_config.yaml` configuration.

6. Start Mage:

```bash
mage start uber-de-project
```

7. Execute the pipeline through the Mage interface.

**Note:** Google Cloud resources, credentials, and the original dataset are not included in this repository. You must configure your own cloud environment and data source before running the pipeline.

## 💡 Key Learnings

- Building end-to-end ETL pipelines using Mage AI.
- Working with Google Cloud Storage and Compute Engine.
- Implementing dimensional modelling and star schemas.
- Performing data cleaning, deduplication, and feature extraction with Pandas.
- Integrating Python pipelines with Google BigQuery.
- Building interactive analytical dashboards using Looker Studio.
- Managing cloud authentication, IAM permissions, and dependencies.

## 📚 Dataset & Acknowledgements

- **Dataset:** NYC TLC Yellow Taxi Trip Records.

This is an independent learning project inspired by the referenced tutorial. The dataset represents NYC Yellow Taxi trip records and is not proprietary Uber data.

---

**Author:** Aman Phadke

[GitHub](https://github.com/AmanPhadke) · [LinkedIn](https://www.linkedin.com/in/amanphadke/)
