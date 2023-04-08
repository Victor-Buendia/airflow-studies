from datetime import datetime, timedelta, date
from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
	dag_id = 'my-first-dag'
	, start_date = datetime.now()
	, schedule = '*/5 * * * *'
	, catchup = False
	, tags = ["learning"]
) as dag:
	
	hello_world = BashOperator(
		task_id = 'hello'
		, bash_command = 'echo "hello world!"'
	)