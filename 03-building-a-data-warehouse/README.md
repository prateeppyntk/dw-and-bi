# Project Week3: Building an ETL Pipeline for a Cloud Data Warehouse (Google BigQuery)

## What we do in this project?
- We will extract data from each json file, transform some of data into the new columns, and load transformed data into each table in Google BigQuery.

## Data Modeling
In this project, We build 3 tables and extract 

![Data Modeling](data_model.png)


## File in the project
1. requirements.txt:  Use for install neccesary library
2. etl_bigquery.py:  Use for create events table and ETL data into it
3. etl_bigquery_act.py:  Use for create actors table and ETL data into it
4. etl_bigquery_rep.py:  Use for create repositories table and ETL data into it
5. github_events_01.json - github_events_05.json (5 files):  Data for ETL process


## Instruction
1. Please check you path that Is is in "02-data-modeling-ii"? 
-> If yes, please skip to the next step
-> Unless, Please run this code in terminal: $ cd 02-data-modeling-ii for chaging path first
2. Install docker -> Run this code in terminal: $ docker compose up
3. Install neccesary library -> Run this code in terminal: $ pip install -r requirements.txt
4. Setup Cassandra, create table, insert data, and run query -> Run this code in terminal: $ python etl.py
