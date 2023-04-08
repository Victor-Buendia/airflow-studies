# airflow-studies
Repo to publish all my airflow studies and experiments.

### Observation
There is a dependency problem with the constraints used by Airflow regarding `lazy-object-proxy==1.9.0`, so I created a `constraints.txt` and removed the constraint related to this dependency. The removal is automated with bash script, so you dont't have to worry about it.

# Quickstart
To put an Airflow server up using a Python Virtual Environment and get started with your studies, just run:

```sh
	chmod +x ./quickstart/start.sh && ./quickstart/start.sh
```