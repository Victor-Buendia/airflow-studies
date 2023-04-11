# airflow-studies
Repo to publish all my airflow studies and experiments.

### Observation
There is a dependency problem with the constraints used by Airflow regarding `lazy-object-proxy==1.9.0`, so I created a `constraints.txt` and removed the constraint related to this dependency. The removal is automated with bash script, so you dont't have to worry about it.

# Quickstart
To put an Airflow server up using a Python Virtual Environment and get started with your studies, just run:

```sh
chmod +x ./quickstart/start.sh && ./quickstart/start.sh
```

# Using Docker
To start Airflow using Docker containers, use:

```sh
docker-compose up --build
```

# Permissions

```sh
chmod -R 777 {$pwd}/docker/dags
```

# Parameters
Change in the `airflow.cfg` these parameters for convenient update of DAGs:

```sh
# Number of seconds after which a DAG file is parsed. The DAG file is parsed every
# ``min_file_process_interval`` number of seconds. Updates to DAGs are reflected after
# this interval. Keeping this number low will increase CPU usage.
min_file_process_interval = 5

# How often (in seconds) to check for stale DAGs (DAGs which are no longer present in
# the expected files) which should be deactivated, as well as datasets that are no longer
# referenced and should be marked as orphaned.
parsing_cleanup_interval = 60

# How often (in seconds) to scan the DAGs directory for new files. Default to 5 minutes.
dag_dir_list_interval = 5
```

# Restarting the server

```sh
docker-compose up -d --no-deps --build airflow-webserver airflow-scheduler
```

https://stackoverflow.com/questions/46059161/airflow-how-to-pass-xcom-variable-into-python-function
https://stackoverflow.com/questions/51734923/airflow-python-operator-writes-files-to-different-locations