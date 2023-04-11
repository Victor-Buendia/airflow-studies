from datetime import datetime, timedelta, date
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.decorators import task
import os

with DAG(
	dag_id = 'my-first-dag'
	, start_date = datetime(2023,4,9)
	, schedule = '*/1 * * * *'
	, catchup = False
	, tags = ["learning"]
) as dag:

	os.chdir('/opt/airflow/dags/')

	hello_world = BashOperator(
		task_id = 'hello'
		, bash_command = 'echo "hello world!"'
	)

	@task(task_id = 'my_python')
	def myfunc(**kwargs):
		print("Call me JOHN!")

	my_python = myfunc()

	@task(task_id = 'download_data')
	def download(**kwargs):
		import opendatasets as od

		user = os.environ['KAGGLE_USERNAME']
		apiKey = os.environ['KAGGLE_API_KEY']

		print(os.path.abspath(""))

		if not os.path.exists('./higher-education-students-performance-evaluation/'):
			with open('kaggle.json', 'w') as fp:
				fp.write('{' + f'"username":"{user}","key":"{apiKey}"' + '}')
			od.download('https://www.kaggle.com/datasets/mariazhokhova/higher-education-students-performance-evaluation')
			os.remove('kaggle.json')

		task_instance = kwargs['ti']
		task_instance.xcom_push(key = 'Entries', value = 'Data')
		return 0;

	download_kaggle_files = download()

	hello_world >> my_python >> download_kaggle_files