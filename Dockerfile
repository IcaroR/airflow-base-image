FROM apache/airflow:latest-python3.8

# Use root user to perform installations
USER root

ARG AIRFLOW_HOME=/opt/airflow
ARG AIRFLOW_UID=50000  # Default airflow user ID

# Add your dags directory
ADD dags /opt/airflow/dags

# Set airflow user ID
ENV AIRFLOW_UID=${AIRFLOW_UID}

# Ensure the correct ownership of files
RUN chown -R ${AIRFLOW_UID}:0 ${AIRFLOW_HOME}

# Switch to the airflow user
USER ${AIRFLOW_UID}

# Upgrade pip and install required packages
RUN pip install --upgrade pip
RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org boto3
