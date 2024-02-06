# Project Week1: Building a Data Modeling with Postgres(SQL)


## สิ่งที่ทำในโปรเจค
1. ติดตั้ง PostgreSQL และ Adminder (UI สำหรับใช้งาน PostgreSQL บน Web Server) จาก Docker
2. สร้างตารางไว้สำหรับจัดเก็บข้อมูลจากไฟล์ในโฟลเดอร์ data (5 ไฟล์)
3. นำไฟล์ .json ในโฟลเดอร์ data มาขั้นตอน ETL และจัดเก็บใส่ตารางที่สร้างไว้


## ไฟล์ที่ใช้ในโปรเจค
1. docker-compose.yml
2. create_tables.py
3. etl.py
4. github_events_01.json
5. github_events_02.json
6. github_events_03.json
7. github_events_04.json
8. github_events_05.json


## วิธีการใช้งานโค๊ด
1. ตรวจสอบว่า path ใน Terminal อยู่ที่โฟลเดอร์ 01-data-modeling-i หรือไม่ ถ้าไม่ใช่ ให้รันโค๊ดนี้ $ cd 01-data-modeling-i ก่อนทำขั้นตอนถัดไป
2. ติดตั้ง library ชื่อ psycopg2 ด้วยโค๊ด $ pip install psycopg2
3. ติดตั้ง PostgreSQL และ Adminder จาก Docker $ docker compose up
4. สร้างตารางไว้สำหรับเก็บข้อมูล ด้วยโค๊ด $ python create_tables.py
5. Extract, Transform, และ Load ข้อมูลจากไฟล์ .json มาเก็บไว้ที่ตาราง ด้วยโค๊ด $ python etl.py

## Data Model
![Data Model](https://github.com/prateeppyntk/dw-and-bi/assets/139861072/cfcbf742-4154-4716-91fb-6a29c6a112e8)
