# Azure Data Pipeline

The project uses Azure services to ingest, transform, store, and analyze customer support ticket data.

## Pipeline Architecture

```text
Python
   ↓
CSV Files
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
Interactive Dashboard
```
# Azure Components
## Azure Blob Storage
Stores the generated CSV ticket and customer files.

# Azure Data Factory
Organizes the data pipeline and performs the data transformation before loading the data into Azure SQL database.

# Azure SQL Database
Stores the transformed support ticket data in a relational database for analysis purpose.

# Power BI
Connects to the prepared data and provides interactive dashboards for support performance analysis.

## Data Flow
- Customer and ticket data was generated using Python.
- CSV files were uploaded to Azure Blob Storage.
- Azure Data Factory ingested the ticket data.
- Data types were transformed during the Data Factory data flow.
- Transformed data was loaded into the dbo.tickets table in Azure SQL Database.
- SQL was used for validation and analytical queries.
- Power BI was used to visualize KPIs, trends, and operational insights.

