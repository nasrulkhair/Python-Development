 
"""
 # WORKING WITH TEMPLATES
 
 # 1. Creating a templated BashOperator
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
  'start_date': datetime(2023, 4, 15),
}

cleandata_dag = DAG('cleandata',
                    default_args=default_args,
                    schedule_interval='@daily')

# Create a templated command to execute
templated_command = 'bash cleandata.sh {{ ds_nodash }}'


# Modify clean_task to use the templated command
clean_task = BashOperator(task_id='cleandata_task',
                          bash_command= templated_command,
                          dag=cleandata_dag)

# 2. Templates with multiple arguments
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
  'start_date': datetime(2023, 4, 15),
}

cleandata_dag = DAG('cleandata',
                    default_args=default_args,
                    schedule_interval='@daily')

# Modify the templated command to handle a
# second argument called filename.
templated_command = '''
  bash cleandata.sh {{ ds_nodash }} {{ params.filename }}
'''

# Modify clean_task to pass the new argument
clean_task = BashOperator(task_id='cleandata_task',
                          bash_command=templated_command,
                          params={'filename': 'salesdata.txt'},
                          dag=cleandata_dag)

# Create a new BashOperator clean_task2
clean_task2 = BashOperator(task_id='cleandata_task2',
                           bash_command = templated_command,
                           params = {'filename':'supportdata.txt'},
                           dag = cleandata_dag)
                           
# Set the operator dependencies

clean_task >> clean_task2

#____________________________________________________________________________

#MORE TEMPLATE

# 1. Using list with templates
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

filelist = [f'file{x}.txt' for x in range(30)]

default_args = {
  'start_date': datetime(2020, 4, 15),
}

cleandata_dag = DAG('cleandata',
                    default_args=default_args,
                    schedule_interval='@daily')

# Modify the template to handle multiple files in a 
# single run.
templated_command = '''
  <% for filename in params.filenames %>
  bash cleandata.sh {{ ds_nodash }} {{ filename }};
  <% endfor %>
'''

# Modify clean_task to use the templated command
clean_task = BashOperator(task_id='cleandata_task',
                          bash_command=templated_command,
                          params={'filenames': filelist},
                          dag=cleandata_dag)


# 2. Sending templated emails
from airflow import DAG
from airflow.operators.email import EmailOperator
from datetime import datetime

# Create the string representing the html email content
html_email_str = '''
Date: {{ ds }}
Username: {{ params.username }}
'''

email_dag = DAG('template_email_test',
                default_args={'start_date': datetime(2023, 4, 15)},
                schedule_interval='@weekly')
                
email_task = EmailOperator(task_id='email_task',
                           to='testuser@datacamp.com',
                           subject="{{ macros.uuid.uuid4()}}",
                           html_content= html_email_str,
                           params={'username': 'testemailuser'},
                           dag=email_dag)


# ___________________________________________________________________________

# BRANCHING

# 1. define a BranchPythonOperator
# Create a function to determine if years are different
def year_check(**kwargs):
    current_year = int(kwargs["ds"][0:4])
    previous_year = int(kwargs["prev_ds"][0:4])
    if current_year == previous_year:
        return 'current_year_task'
    else:
        return 'new_year_task'

# Define the BranchPythonOperator
branch_task = BranchPythonOperator(task_id='branch_task', dag=branch_dag,
                                   python_callable= year_check, provide_context=True)
# Define the dependencies
branch_task >> current_year_task
branch_task >> new_year_task

# ____________________________________________________________________________

# CREATING A PRODUCTION PIPELINE

# 1. Creating a production pipeline #1
from airflow import DAG
from airflow.sensors.filesystem import FileSensor
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import date, datetime

def process_data(**context):
    with open('/home/repl/workspace/processed_data.tmp', 'w') as file:
        file.write(f'Data processed on {date.today()}')

dag = DAG(
    dag_id='etl_update',
    default_args={'start_date': datetime(2023, 4, 1)},
    schedule_interval='@daily',  # Add schedule interval if needed
    catchup=False  # Set to False if you don't want to catch up on missed intervals
)

sensor = FileSensor(
    task_id='sense_file',
    filepath='/home/repl/workspace/startprocess.txt',
    poke_interval=5,
    timeout=60,  # Increase timeout if needed
    mode='poke',  # Default mode
    dag=dag
)

bash_task = BashOperator(
    task_id='cleanup_tempfiles',
    bash_command='rm -f /home/repl/*.tmp',
    dag=dag
)

python_task = PythonOperator(
    task_id='run_processing',
    python_callable=process_data,
    dag=dag
)

sensor >> bash_task >> python_task


# 2. Creating a production pipeline #2
from airflow import DAG
from airflow.sensors.filesystem import FileSensor
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from dags.process import process_data
from datetime import timedelta, datetime

# Update the default arguments and apply them to the DAG
default_args = {
  'start_date': datetime(2023,1,1),
  'sla': timedelta(minutes = 90)
}

dag = DAG(dag_id='etl_update', default_args=default_args)

sensor = FileSensor(task_id='sense_file', 
                    filepath='/home/repl/workspace/startprocess.txt',
                    poke_interval = 45,
                    dag=dag)

bash_task = BashOperator(task_id='cleanup_tempfiles', 
                         bash_command='rm -f /home/repl/*.tmp',
                         dag=dag)

python_task = PythonOperator(task_id='run_processing', 
                             python_callable=process_data,
                             provide_context = True,
                             dag=dag)

sensor >> bash_task >> python_task


# 3. Adding the final changes to your pipeline
  ### FULL SET WORKFLOW
  
from airflow import DAG
from airflow.sensors.filesystem import FileSensor
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.operators.python import BranchPythonOperator
from airflow.operators.empty import EmptyOperator
from airflow.operators.email import EmailOperator
from dags.process import process_data
from datetime import datetime, timedelta

# Update the default arguments and apply them to the DAG.

default_args = {
  'start_date': datetime(2023,1,1),
  'sla': timedelta(minutes=90)
}
    
dag = DAG(dag_id='etl_update', default_args=default_args)

sensor = FileSensor(task_id='sense_file', 
                    filepath='/home/repl/workspace/startprocess.txt',
                    poke_interval=45,
                    dag=dag)

bash_task = BashOperator(task_id='cleanup_tempfiles', 
                         bash_command='rm -f /home/repl/*.tmp',
                         dag=dag)

python_task = PythonOperator(task_id='run_processing', 
                             python_callable=process_data,
                             provide_context=True,
                             dag=dag)

email_subject='''
  Email report for {{ params.department }} on {{ ds_nodash }}
'''

email_report_task = EmailOperator(task_id='email_report_task',
                                  to='sales@mycompany.com',
                                  subject=email_subject,
                                  html_content='',
                                  params={'department': 'Data subscription services'},
                                  dag=dag)

no_email_task = EmptyOperator(task_id='no_email_task', dag=dag)

def check_weekend(**kwargs):
    dt = datetime.strptime(kwargs['execution_date'],"%Y-%m-%d")
    # If dt.weekday() is 0-4, it's Monday - Friday. If 5 or 6, it's Sat / Sun.
    if (dt.weekday() < 5):
        return 'email_report_task'
    else:
        return 'no_email_task'
    
branch_task = BranchPythonOperator(task_id='check_if_weekend',
                                   python_callable=check_weekend,
                                   provide_context=True,                                
                                   dag=dag)

sensor >> bash_task >> python_task

python_task >> branch_task >> [email_report_task, no_email_task]

"""