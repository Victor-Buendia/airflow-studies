#!/bin/sh

# Create Python3 virtual environment to isolate installation
python3 -m venv ./quickstart/venv
# Activating virtual environment
source ./quickstart/venv/bin/activate
# Check if the venv is active before installing
echo $(which python3)
echo "Installing will go in 10 seconds..."
sleep 10

# Airflow needs a home. `~/airflow` is the default, but you can put it
# somewhere else if you prefer (optional)
export AIRFLOW_HOME=~/airflow

# Install Airflow using the constraints file
AIRFLOW_VERSION=2.5.3
PYTHON_VERSION="$(python3 --version | cut -d " " -f 2 | cut -d "." -f 1-2)"
# For example: 3.9

# Downloading constraints from Airflow website
wget https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt -O ./quickstart/constraints.txt
# For example: https://raw.githubusercontent.com/apache/airflow/constraints-2.5.3/constraints-3.7.txt

# Removing lazy-object-proxy dependency
grep -v ^lazy-object ./quickstart/constraints.txt > ./quickstart/tmp.txt
mv ./quickstart/tmp.txt ./quickstart/constraints.txt
pip3 install "apache-airflow==${AIRFLOW_VERSION}" --constraint ./quickstart/constraints.txt

# Installing pandas for examples
pip3 install pandas

# The Standalone command will initialise the database, make a user,
# and start all components for you.
airflow standalone

# Visit localhost:8080 in the browser and use the admin account details
# shown on the terminal to login.
# Enable the example_bash_operator DAG in the home page