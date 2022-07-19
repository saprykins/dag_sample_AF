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

sources
[link](https://www.bigdataschool.ru/blog/apache-airflow-quick-start.html)
