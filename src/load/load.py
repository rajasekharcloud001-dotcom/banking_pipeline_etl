from google.cloud import bigquery
from google.cloud import secretmanager
import pandas as pd

def get_secret(secret_id, project_id):
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/{project_id}/secrets/{secret_id}/versions/latest"
    response = client.access_secret_version(request={"name": name})
    return response.payload.data.decode("UTF-8")

def load(df, project_id):
    """Clean data ని BigQuery కి load చేయి"""
    
    print(f"📤 Loading to BigQuery...")
    
    # Secrets తీసుకో
    dataset = get_secret("dataset-name", project_id)
    table = get_secret("table-name", project_id)
    
    # BigQuery client
    client = bigquery.Client(project=project_id)
    
    # Table reference
    table_ref = f"{project_id}.{dataset}.{table}"
    
    # Load config
    job_config = bigquery.LoadJobConfig(
        write_disposition="WRITE_APPEND"
    )
    
    # Load చేయి
    job = client.load_table_from_dataframe(
        df, table_ref, job_config=job_config
    )
    job.result()
    
    print(f"✅ Loaded {len(df)} records to {table_ref}")

if __name__ == "__main__":
    import os
    import sys
    sys.path.append("src/transform")
    from transform import transform
    
    project_id = os.getenv("GCP_PROJECT", "hello-dev-491512")
    local_path = os.getenv("LOCAL_PATH", "data/banking_data_2026-03-30.csv")
    
    df = transform(local_path)
    load(df, project_id)