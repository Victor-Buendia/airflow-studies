from dotenv.main import load_dotenv
import opendatasets as od
import os
load_dotenv()

user = os.environ['KAGGLE_USERNAME']
apiKey = os.environ['KAGGLE_API_KEY']

if not os.path.exists('./higher-education-students-performance-evaluation/'):
	with open('kaggle.json', 'w') as fp:
		os.chdir(os.path.abspath(""))
		fp.write('{' + f'"username":"{user}","key":"{apiKey}"' + '}')
	od.download('https://www.kaggle.com/datasets/mariazhokhova/higher-education-students-performance-evaluation')
	os.remove('kaggle.json')