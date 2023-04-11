FROM apache/airflow:2.5.3
WORKDIR /
COPY requirements.txt .
RUN pip install --user --upgrade pip
RUN pip install --no-cache-dir --user -r /requirements.txt