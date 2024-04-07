# nyc_motor_vehicle_crash_mage_pipelines_2024

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



