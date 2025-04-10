from airflow import DAG
import airflow.decorators import dag 
from airflow.operators.python  import PythonOperator 


with DAG(...):
    ta=PythonOperator(task_id='ta')
    tb=PythonOperator(task_id='tb')
    
    
    

from airflow.decorators import dag
from pendulum  import datetime
from airflow.decorators import dag
from pendulum import datetime

@dag(
    start_date=datetime(2025, 1, 1),
    schedule_interval='@daily',
    catchup=False,
    description="E-commerce daily pipeline",
    tags=["team", "teamB"],
    default_args={
        "retries": 1
    },
    dagrun_timeout=timedelta(minutes=20)
    max_consecuitve_failed_dag_runs=2, 
    max_active_runs=1
)
def ecom():
    # Define your tasks here
    pass
