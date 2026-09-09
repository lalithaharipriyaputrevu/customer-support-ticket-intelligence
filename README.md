# Customer Support Ticket Intelligence

##  Project Overview

An end-to-end customer support analytics project designed to identify service
performance gaps, understand ticket drivers, and provide actionable
recommendations for improving SLA compliance and support efficiency.

This project analyzes 50,000 customer support tickets across customer segments,
support channels, issue types, resolution times, SLA performance, escalations,
and customer satisfaction.

 **Data Disclaimer:** This project uses synthetic data created for
 portfolio and learning purposes. It represents a fictional customer-facing
 company's support operations and does not contain real customer or company
 data.

##  Business Problem

Customer support teams need to understand:

- Which issues generate the highest support volume?
- Where are SLA breaches occurring?
- Which issues have the highest escalation rates?
- Which customer segments require additional attention?
- How does resolution time affect SLA performance?
- Which support channels require process improvement?
- What actions can improve support efficiency and customer experience?

##  Tools & Technologies

- **Python** — Data generation and preparation
- **PostgreSQL** — Data storage and SQL analysis
- **SQL** — Data validation, aggregation, segmentation, and KPI analysis
- **Azure Blob Storage** — Cloud data storage
- **Azure Data Factory** — Data ingestion and transformation pipeline
- **Azure SQL Database** — Cloud relational data storage
- **Power BI** — Interactive dashboard and business intelligence
- **DAX** — KPI and analytical measures

##  Data Pipeline

```text
Python
   ↓
CSV Data
   ↓
Azure Blob Storage
   ↓
Azure Data Factory
   ↓
Data Transformation
   ↓
Azure SQL Database
   ↓
Power BI
   ↓
Interactive Analytics Dashboard


