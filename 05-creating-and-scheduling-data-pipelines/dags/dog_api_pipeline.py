import logging


from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from airflow.providers.google.cloud.transfers.local_to_gcs import LocalFilesystemToGCSOperator
from airflow.utils import timezone


import requests
import json


def _get_dog_api():
   response = requests.get("https://dog.ceo/api/breeds/image/random")
   data = response.json()
   logging.info(data)
   with open("/opt/airflow/dags/dog.json","w") as f:
      json.dump(data, f)

  # case: need to append data    
  #  with open("/opt/airflow/dags/dog.json","a") as f:
  #     json.dump(data, f)
 

# 1st way: open file in Python
# with open("hello.txt","w") as f:
#     f._____
#     f._____

# 2st way: open file in Python
# f = open("")
# f.close()

# open/initial DAG is reqested:
# 1.DAG id (unique) *best practice to name as file's name
# 2.start_date *req. datatime obj. of Python
# 3.schedule
with DAG(
    "dog_api_pipeline",
    start_date = timezone.datetime(2024, 3, 23),
    schedule = "@daily", # Cron Expression / this DAG will run when we click trigger
    tags = ["DS525"], # create tag for searching easily
 ):
   # create task
   # each operator req. task_id & difference parameters
    start = EmptyOperator(task_id = "start")

    get_dog_api = PythonOperator(
      task_id="get_dog_api",
      python_callable=_get_dog_api, # callable = function name + not have () because we will not call by ourselves, will let airflow to do.
    )

    upload_to_gcs = LocalFilesystemToGCSOperator(
      task_id="upload_to_gcs",
      src="/opt/airflow/dags/dog.json",
      dst="dog.json",
      bucket="example_airflow_444532",
      gcp_conn_id="my_gcp_conn",
    )

    end = EmptyOperator(task_id = "end")

    start >> get_dog_api >> upload_to_gcs >> end  # create dependency of tasks
