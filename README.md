# Spotify ELT Project
Karl and Bryan will build a Spotify ELT Data Pipeline. The primary objective of the project is to conceptually learn and be familar with building an ELT pipeline, framework, and infrastructure from scratch.

Ingest Raw Data → Load → Transform → Reporting Dashboard 

## Data Tech Stack
* Spotify Web API
* Databricks
* Microsoft Azure Cloud
* dbt
* Airflow
* Python
* Github

## Microsoft Azure

After creating a Microsoft Azure account(s), we must connect to a Mircosoft Azure Container and Storage in order to upload and save files after calling a Spotify API Endpoint(s).

1. Install `azure-storage-blob` python library
    - ``` pipenv install azure-storage-blob ```
2. Get and save Azure Blob Storage Credientials
    - `storage_account_key`
    - `storage_account_name`
    - `connection_string`
    - `container_name`