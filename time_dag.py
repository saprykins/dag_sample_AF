# SCHEDULER CHECKS

from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

dag = DAG(
    dag_id = 'orders',
    # schedule_interval=timedelta(hours=24),
    schedule_interval = '@daily',
    
    # starts at 9h30 8th of July UTC time 
    # 13h UTC = 15h Paris time
    start_date=datetime(2023, 7, 8, 9, 30) 
    )

def workflow():
    print('context')

workflow = PythonOperator(
    task_id='log_out', 
    python_callable=workflow, 
    dag=dag
    )

workflow
