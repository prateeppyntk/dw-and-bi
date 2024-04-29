from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.utils import timezone


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

# create task
# each operator req. task_id
with DAG(
    "my_fist_dag",
    start_date = timezone.datetime(2024, 3, 23),
    schedule = None, # this DAG will run when we click trigger
    tags = ["DS525"], # create tag for searching easily
 ):
    my_first_task = EmptyOperator(task_id = "my_first_task")
    my_second_task = EmptyOperator(task_id = "my_second_task")

    my_first_task >> my_second_task  # create dependency of tasks