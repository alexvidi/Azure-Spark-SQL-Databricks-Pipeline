import requests
import pandas as pd
import json
from azure.storage.blob import BlobServiceClient
import yaml
import io
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Load credentials from config/credentials.yaml
with open("config/credentials.yaml", "r") as file:
    config = yaml.safe_load(file)

# Retrieve the connection string and container name
connection_string = config["azure_blob_storage"]["connection_string"]
container_name = config["azure_blob_storage"]["container_name"]

# JSONPlaceholder API URL
API_URL = "https://jsonplaceholder.typicode.com/posts"

def fetch_data():
    """Fetch data from the JSONPlaceholder API and return it as a DataFrame."""
    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()
        df = pd.DataFrame(data)
        logging.info(" Successfully fetched data from JSONPlaceholder API.")
        return df
    except requests.exceptions.RequestException as e:
        logging.error(f" Error fetching data from API: {e}")
        raise

def upload_to_blob(dataframe, blob_name):
    """Save a DataFrame as JSON in Azure Blob Storage."""
    try:
        # Establish connection to Azure Blob Storage
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        container_client = blob_service_client.get_container_client(container_name)

        # Convert DataFrame to JSON format
        json_data = dataframe.to_json(orient="records", indent=2)
        json_bytes = io.BytesIO(json_data.encode())

        # Upload JSON data to Azure Blob Storage
        blob_client = container_client.get_blob_client(blob_name)
        blob_client.upload_blob(json_bytes, overwrite=True)

        logging.info(f" Successfully uploaded data to Azure Blob Storage as '{blob_name}'.")
    except Exception as e:
        logging.error(f" Error uploading data to Azure Blob Storage: {e}")
        raise

# Execute ingestion process
if __name__ == "__main__":
    logging.info(" Starting data ingestion process...")
    
    df = fetch_data()
    
    logging.info(" Uploading data to Azure Blob Storage...")
    upload_to_blob(df, "jsonplaceholder_posts.json")
    
    logging.info(" Data ingestion process completed successfully.")

