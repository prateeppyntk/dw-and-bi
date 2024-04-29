import logging


from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from airflow.utils import timezone


def _say_hello():
   logging.debug("This is DEBUG log")
   logging.info("hello")


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
    "hello",
    start_date = timezone.datetime(2024, 3, 23),
    schedule = None, # this DAG will run when we click trigger
    tags = ["DS525"], # create tag for searching easily
 ):
   # create task
   # each operator req. task_id & difference parameters
    start = EmptyOperator(task_id = "start")
    
    echo_hello = BashOperator(
      task_id="echo_hello",
      bash_command="echo 'hello'",
    )

    say_hello = PythonOperator(
      task_id="say_hello",
      python_callable=_say_hello, # callable = function name + not have () because we will not call by ourselves, will let airflow to do.
    )

    end = EmptyOperator(task_id = "end")

    start >> echo_hello >> end  # create dependency of tasks
    start >> say_hello >> end  # it wil have 2 lines
