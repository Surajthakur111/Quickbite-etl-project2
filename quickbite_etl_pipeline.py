from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
import boto3

default_args = {
    'owner': 'quickbite_team',
    'start_date': days_ago(1),
    'retries': 1,
}

def run_glue_job():
    glue = boto3.client('glue', region_name='us-east-2')
    response = glue.start_job_run(JobName='glue_job_total_sales')
    print("Started Glue Job:", response['JobRunId'])

with DAG(
    dag_id='quickbite_etl_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False
) as dag:

    trigger_glue_job = PythonOperator(
        task_id='trigger_glue_job',
        python_callable=run_glue_job
    )
