## Logical blocks of a DAG file

import ...  

default arguments  

DAG instantiation  

Tasks generation  

Set up dependencies  


## Sample DAG file  

Check in file list

## Send file to DAG-folder
```
gsutil cp dag-example.py gs://us-central1-airflow-check-c-0ac5f198-bucket/dags
```
Send operators
```
gsutil cp dag-example.py gs://europe-west1-test-dag-w-new-af7c368b-bucket/plugins
```
 
```
gsutil cp $HOME/my_operator.py gs://<COMPOSER_BUCKET_NAME>/plugins
```
```
gsutil cp $HOME/my_dag.py gs://<COMPOSER_BUCKET_NAME>/dags
```

## DAG file description
Dependency description  
  Tasks t2 and t3 are in paralel  
  t2 starts only if t1 successful
```
#    t2
#   /  
# t1    
#   \  
#    t3
```
The below descriptions are equivalent
```
t1 >> t2 
t1 >> t3 

t1.set_downstream([t2, t3])
t1 >> [t2, t3]
[t2, t3] << t1
```

Launch is possible by Pub/Sub and Function [lnk](https://stackoverflow.com/questions/58551125/trigger-cloud-composer-dag-with-a-pub-sub-message)  
  
sources:  
[rus link](https://www.bigdataschool.ru/blog/apache-airflow-quick-start.html)

# Time scheduling

Irregular periods [link](https://www.astronomer.io/guides/scheduling-in-airflow/)
