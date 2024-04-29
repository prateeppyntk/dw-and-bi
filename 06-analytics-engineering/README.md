# Project Week6: สร้าง Analytics Workflow ด้วย dbt และการนำเอาแนวคิด Analytics Engineering มาใช้

## What we do in this project?
We create the automate data pipeline by using Airflow to proceed to exract data from 5 datasets, create tables, and insert data into each table.

## Data Modeling
In the pipeline, we did not indicate the dependency of get_files and create_tables task, it can be proceeded together.
![Data Modeling](data_model_airflow.jpg)

## File in the project
1. docker-compose.yml:  Use for install Airflow.
2. etl.py Use for process in pipeline
3. github_events_01.json - github_events_05.json (5 files):  Data for process

## Instruction
1. Please check you path that Is is in "05-creating-and-scheduling-data-pipelines"? 
-> If yes, please skip to the next step
-> Unless, Please run this code in terminal: $ cd 02-data-modeling-ii for chaging path first
2. Install Airflow:
   -> $ docker-compose up
3. When finished installment, go to ports tab and open port:8080.
4. Username and password = airflow (If you did not config with other value.)
5. Find DAG'name = etl
6. Then, you can run this pipeline in Airflow

**To make sure before proceed 5th step**
1. Create connection of PostgreSQL in Airflow
2. Config your conn name in etl.py
-- If you done, you can skip this step.--


