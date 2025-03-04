from azure.storage.blob import BlobServiceClient
import yaml

# Cargar credenciales desde config/credentials.yaml
with open("config/credentials.yaml", "r") as file:
    config = yaml.safe_load(file)

# Obtener la connection string y el nombre del contenedor
connection_string = config["azure_blob_storage"]["connection_string"]
container_name = config["azure_blob_storage"]["container_name"]   

# Crear un cliente para el servicio de blobs
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# Verificar si la conexión es exitosa listando los contenedores disponibles
containers = blob_service_client.list_containers()

print("🔍 Listando contenedores en Azure Blob Storage:")
for container in containers:
    print(f" {container['name']}")

print(" Conexión exitosa a Azure Blob Storage.")
