# Project Week2: Building a Data Modeling with Cassandra (NoSQL)

## What we do in this project?
We use docker for importing Apache Cassadra and create database which will use to collect data that we will extract them from json files in data's folder.

## Data Modeling
In this project, We build 1 table and decide to extract id, login_name, type, organize, create_date, and public columns to store in the table and we also set id, type as Primary key and create_date as Cluster column. Moreover we sort data in create_date column by descending.


## File in the project
1. docker-compose.yml:  Use for install Cassandra by using docker
2. requirements.txt:  Use for install neccesary library
3. etl.py:  Use for Setup Cassandra, create table, insert data, and run query
4. github_events_01.json - github_events_05.json (5 files):  Data for extract


## Instruction
1. Please check you path that Is is in "02-data-modeling-ii"? 
-> If yes, please skip to the next step
-> Unless, Please run this code in terminal: $ cd 02-data-modeling-ii for chaging path first
2. Install docker -> Run this code in terminal: $ docker compose up
3. Install neccesary library -> Run this code in terminal: $ pip install -r requirements.txt
4. Setup Cassandra, create table, insert data, and run query -> Run this code in terminal: $ python etl.py