from azure.storage.blob import BlobServiceClient
import yaml

# Load credentials from config/credentials.yaml
with open("config/credentials.yaml", "r") as file:
    config = yaml.safe_load(file)

# Retrieve the connection string and container name
connection_string = config["azure_blob_storage"]["connection_string"]
container_name = config["azure_blob_storage"]["container_name"]   

# Create a client for the Blob service
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# Verify the connection by listing available containers
containers = blob_service_client.list_containers()

print("🔍 Listing containers in Azure Blob Storage:")
for container in containers:
    print(f" {container['name']}")

print(" Successful connection to Azure Blob Storage.")
