"""
# AIRFLOW SENSORS

# AIRFLOW EXECUTORS



# SLAs  AND REPORTING IN AIRFLOW

# 1. Defining SLA
# Import the timedelta object
from datetime import timedelta

# Create the dictionary entry
default_args = {
  'start_date': datetime(2024, 1, 20),
  'sla': timedelta(minutes = 30)
}

# Add to the DAG
test_dag = DAG('test_workflow', default_args=default_args, schedule_interval=None)

# 2. Defining a task SLA
# Import the timedelta object
from datetime import timedelta

test_dag = DAG('test_workflow', start_date=datetime(2024,1,20), schedule_interval=None)

# Create the task with the SLA
task1 = BashOperator(task_id='first_task',
                     sla =timedelta(hours = 3),
                     bash_command='initialize_data.sh',
                     dag=test_dag)


# 3. Generate and email a report

# Define the email task
email_report = EmailOperator(
        task_id='email_report',
        to='airflow@datacamp.com',
        subject='Airflow Monthly Report',
        html_content="Attached is your monthly workflow report - please refer to it for more detail",
        files=['monthly_report.pdf'],
        dag=report_dag
)

# Set the email task to run after the report is generated
email_report << generate_report

# 4. Adding status emails
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.sensors.filesystem import FileSensor
from datetime import datetime, timedelta

default_args = {
    'start_date': datetime(2023, 2, 20),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'email_on_failure': True,
    'email': ['your_email@example.com'],
    'email_on_success': True
}

report_dag = DAG(
    dag_id='execute_report',
    schedule_interval="0 0 * * *",
    default_args=default_args
)

precheck = FileSensor(
    task_id='check_for_datafile',
    filepath='salesdata_ready.csv',
    start_date=datetime(2023, 2, 20),
    mode='reschedule',
    dag=report_dag
)

"""