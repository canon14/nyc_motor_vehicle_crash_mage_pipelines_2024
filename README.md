# DE Zoomcamp 2024 Final Project - nyc_motor_vehicle_crash_mage_pipelines

## Links 
- Looker Dashboard (final project output) --> https://lookerstudio.google.com/u/0/reporting/ec1ed7c8-175b-4f46-94ef-1a99bcdb44a4/page/cVsvD
- DBT Repository --> https://github.com/canon14/zoomcamp2004_dbt

## Problem description
Motor Vehicle Crashes or Collisions are inevitable, especially in big cities such as New York City where the streets are always bustling with motor vehicles every hour of the day. The purpose of the project is to create an end-to-end pipeline processes that will run in Google Cloud Environment via Terraform/Docker setup, extract daily Motor Vehicle Crashes data from NYC Open Data via API using Mage (alternative to Airflow), transform data with DBT, load the final data to Google Big Query, and utilize Google Data Studio (Looker) to build the final reports. 

## Questions to solve with the project
- How many motor vehicle crashes happen in a day on average in New York City?
- What is the borough distribution of these crashes?
- What is the time of day distribution of these crashes? (Early Morning, Morning, Afternoon, Evening, Night)
- How many total number of people injured?
- How many total number of people killed?

## Technologies
- Programming Language = Python, SQL
- Cloud Technology = The project is developed fully in Google Cloud
- IAC = Terraform
- Data ingestion and Orchestration = Mage (End-to-End)
- Data Warehouse = Google Big Query
- Data Transformation = DBT
- Dashboard = Google Data Studio (Looker)

### Project Detail - Reproducibility
1. Deploy Mage onto Google Cloud using Terraform and setup Google Cloud Permissions - https://www.youtube.com/watch?v=zAwAX5sxqsg&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=28
2. Download initial Motor Vehicle Crash data - https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Crashes/h9gi-nx95/about_data
3. Setup Mage Pipeline to process our initial data from step 2 and load to a BigQuery table. 
4. Setup Data Ingestion Pipeline to extract daily motor vehicle collision data from NYC Open Data API (via Socrata) and load data as parquet files in Google Cloud Storage. This pipeline will be scheduled to run daily at midnight EST.
5. Setup Data Pipeline to fetch parquet files from step 4, clean the data, and load output to BigQuery.
6. Setup DBT Cloud and connect it to our BigQuery DW using our GCP Project Credentials. - https://cloud.getdbt.com/
7. Create staging models, referencing tables in BigQuery.
8. Create our final mart model by transforming and processing our staging models.
9. Start to build the report in Looker - https://lookerstudio.google.com/

Optional 
1. Download NYC Population by Zip Code - https://data.census.gov/
2. Create mage pipeline to process data and load to BigQuery
3. Create a staging and production model in DBT to clean and transform data (remove NULLs, get borough information, etc)
4. Add the final data into our Looker Dashboard, maybe help to find more insights. Examples: correlation between population and the number of collisions, etc. 
