from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator

# Creating the functions that will be called by the operators
def print_hello():
    return 'Hello world!'

def print_goodbye(ti):
    message = ti.xcom_pull(task_ids='hello_task')
    return message + ' see you later!'

# Creating the DAG
with DAG('hello_world', description='Simple tutorial DAG',
            schedule_interval='0 12 * * *', #Passin the cron expression
            start_date=datetime(2024, 9, 4), catchup=False) as dag:

    # Creating the operators, in this case, I want to run python functions
    hello_operator = PythonOperator(
        task_id='hello_task', 
        python_callable=print_hello, 
        dag=dag
    )

    goodbye_operator = PythonOperator(
        task_id='goodbye_task', 
        python_callable=print_goodbye, 
        depends_on_past=True, # This will make the task wait for the previous task to finish
        dag=dag
    )

    # Setting the order of the tasks
    hello_operator >> goodbye_operator   