
# QuickBite ETL Pipeline Project

Overview
This project demonstrates an end-to-end data pipeline using AWS Glue and Amazon MWAA (Managed Airflow). It automates the process of transforming order data and storing the results in S3, triggered by a scheduled Airflow DAG.

## Pipeline Components
- **Source**: CSV files in S3 (fact_order.csv)
- **Processing**: AWS Glue job (`glue_job_total_sales`) aggregates order data
- **Orchestration**: MWAA DAG (`quickbite_etl_pipeline`) triggers Glue job daily
- **Destination**: Transformed data stored in S3 at `/trusted/aggregates/sales_by_region/`

## Success Criteria
Airflow DAG runs successfully  
Glue job is triggered by DAG and completes  
Output files are written to S3  

## How to Run
1. Upload the DAG to `s3://quickbite-data-suraj/dags/`
2. Enable and trigger the DAG in Airflow UI
3. Confirm Glue run and output

## Screenshots
See `/screenshots/` folder for DAG and job run evidence.
