# dag_sample_airflow

import ...  

default arguments:  
* to avoid repeated values *
```
default_args = {
    'owner': 'romank',
    'start_date': days_ago(0),
    'depends_on_past': False,
}
```
