# dag_sample_airflow

import ...  

default arguments:  
  to avoid repeated values  
```
default_args = {
    'owner': 'romank',
    'start_date': days_ago(0),
    'depends_on_past': False,
}
```

DAG  
```
with DAG(
    'mydag',
    default_args=default_args,
    schedule_interval='@once',
    catchup=False
) as dag:
    t1 = BashOperator(
        task_id='echo_hi',
        bash_command='echo "Hello"',
    )
    t2 = BashOperator(
        task_id='print_date',
        bash_command='date',
    )
    t1 >> t2
```
sources:  
[link](https://www.bigdataschool.ru/blog/apache-airflow-quick-start.html)
