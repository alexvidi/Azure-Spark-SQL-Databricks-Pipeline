import requests
import pandas as pd
import json
from azure.storage.blob import BlobServiceClient
import yaml
import io

# Cargar credenciales desde config/credentials.yaml
with open("config/credentials.yaml", "r") as file:
    config = yaml.safe_load(file)

# Obtener la connection string y el nombre del contenedor
connection_string = config["azure_blob_storage"]["connection_string"]
container_name = config["azure_blob_storage"]["container_name"]

# URL de la API de JSONPlaceholder
API_URL = "https://jsonplaceholder.typicode.com/posts"

def fetch_data():
    """Obtiene datos desde la API de JSONPlaceholder."""
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        return df
    else:
        raise Exception(f"Error al obtener datos: {response.status_code}")

def upload_to_blob(dataframe, blob_name):
    """Guarda un DataFrame como JSON en Azure Blob Storage."""
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service_client.get_container_client(container_name)

    # Convertir DataFrame a JSON
    json_data = dataframe.to_json(orient="records", indent=2)
    json_bytes = io.BytesIO(json_data.encode())

    # Subir a Azure Blob Storage
    blob_client = container_client.get_blob_client(blob_name)
    blob_client.upload_blob(json_bytes, overwrite=True)

    print(f" Datos subidos exitosamente a Azure Blob Storage como '{blob_name}'.")

# Ejecutar el proceso de ingesta
if __name__ == "__main__":
    print(" Obteniendo datos desde JSONPlaceholder...")
    df = fetch_data()
    
    print(" Subiendo datos a Azure Blob Storage...")
    upload_to_blob(df, "jsonplaceholder_posts.json")
    
    print(" Proceso de ingesta completado.")
