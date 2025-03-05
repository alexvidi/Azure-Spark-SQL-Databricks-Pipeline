# Azure-Spark-SQL-Databricks-Pipeline

Este proyecto implementa un pipeline completo de procesamiento de datos utilizando Azure Synapse Analytics, Azure Data Lake Storage, Apache Spark en Databricks y consultas SQL para analizar los datos procesados.

## 📌 Estructura del Proyecto

```bash
Azure-Spark-SQL-Databricks-Pipeline/
│── config/
│   ├── credentials.yaml  # Archivo de credenciales para conexiones
│── data/
│   ├── jsonplaceholder_posts.json  # Archivo JSON original con los datos
│   ├── jsonplaceholder_posts.csv  # Archivo convertido a CSV para Synapse
│   ├── SQL queries_Azure Synapse Analytics.csv  # Resultado de las consultas SQL
│── docs/
│── notebooks/
│   ├── Spark-SQL 04-03.ipynb  # Notebook con consultas y procesamiento en Databricks
│── src/
│   ├── etl/
│   │   ├── azure_connection.py  # Script de conexión con Azure
│   │   ├── convert_json_to_csv.py  # Conversión de JSON a CSV
│   │   ├── ingest_jsonplaceholder_data.py  # Ingesta de datos
│── test/
│── utils/
│── .gitignore
│── README.md
│── requirements.txt  # Dependencias del proyecto
```

---

## 🚀 Paso a Paso del Proyecto

### 1️⃣ Configuración y Conexión con Azure
- Se creó un **Azure Data Lake Storage Gen2** para almacenar los archivos de datos.
- Se configuró una **cuenta de almacenamiento** en Azure.
- Se estableció la conexión con **Azure Synapse Analytics** para realizar consultas SQL sobre los datos.
- Se utilizó el script `azure_connection.py` para gestionar la autenticación y conexión con los servicios de Azure.

### 2️⃣ Ingesta y Conversión de Datos
- Inicialmente, se obtuvo un archivo **JSON** (`jsonplaceholder_posts.json`).
- Se creó el script `convert_json_to_csv.py` para convertir el JSON en un archivo CSV adecuado para la consulta en Azure Synapse Analytics.
- Se utilizó la librería `pandas` para manipular y guardar los datos en formato CSV.

### 3️⃣ Carga de Datos en Azure Data Lake
- Se subió el archivo `jsonplaceholder_posts.csv` a **Azure Data Lake Storage**.
- Se generó una **URL SAS Token** para permitir la consulta desde Azure Synapse.
- Se validó el acceso a los archivos desde Azure Synapse.

### 4️⃣ Procesamiento con Apache Spark en Databricks
- Se utilizó un **notebook en Databricks** (`Spark-SQL 04-03.ipynb`) para explorar los datos en Apache Spark.
- Se ejecutaron consultas SQL sobre los datos transformados.
- Se verificó la estructura de los datos en Databricks.

### 5️⃣ Consultas en Azure Synapse Analytics
- Se utilizó `OPENROWSET` en **Azure Synapse SQL** para leer el archivo CSV directamente desde Data Lake.
- Se realizaron consultas SQL para filtrar y analizar los datos.
- Se exportó el resultado en `SQL queries_Azure Synapse Analytics.csv` para su posterior análisis.

### 6️⃣ Exportación y Descarga de Resultados
- Se descargó el resultado de las consultas SQL en un archivo CSV.
- Se validó la integridad de los datos después de la consulta.

---

## 🔧 Scripts Importantes

### **🔹 Conexión a Azure (`azure_connection.py`)
```python
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient

# Conexión con Azure Storage
account_url = "https://datalakealexvidal.dfs.core.windows.net/"
credential = DefaultAzureCredential()
blob_service_client = BlobServiceClient(account_url, credential)
```

### **🔹 Conversión de JSON a CSV (`convert_json_to_csv.py`)
```python
import pandas as pd
import json
import os

# Definir rutas de entrada y salida
input_path = "C:/Users/alexv/Azure-Spark-SQL-Databricks-Pipeline/data/jsonplaceholder_posts.json"
output_path = "C:/Users/alexv/Azure-Spark-SQL-Databricks-Pipeline/data/jsonplaceholder_posts.csv"

# Cargar JSON y convertir a DataFrame
def convert_json_to_csv(input_path, output_path):
    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    df = pd.DataFrame(data)
    df.to_csv(output_path, index=False, encoding="utf-8")

convert_json_to_csv(input_path, output_path)
```

### **🔹 Consulta SQL en Azure Synapse**
```sql
SELECT *
FROM OPENROWSET(
    BULK 'https://datalakealexvidal.dfs.core.windows.net/raw-data-1/jsonplaceholder_posts.csv',
    FORMAT = 'CSV',
    PARSER_VERSION = '2.0'
) AS posts;
```

---

## 📌 Tecnologías Utilizadas

- **Azure Synapse Analytics** → Consultas SQL sobre Data Lake
- **Azure Data Lake Storage Gen2** → Almacenamiento de datos
- **Apache Spark en Databricks** → Procesamiento de datos
- **Python (pandas, json)** → Manipulación y conversión de datos
- **SQL (T-SQL, Synapse SQL)** → Consultas y análisis de datos
- **Azure Blob Storage** → Gestión de archivos en la nube

---

## 📌 Próximos Pasos
- **Automatizar** la carga de datos en Azure usando **Azure Data Factory**.
- **Implementar un pipeline en Apache Airflow** para la orquestación de tareas.
- **Visualizar datos con Power BI** desde Azure Synapse Analytics.

---

## 🚀 Contribuciones y Mejora
Si deseas contribuir a este proyecto, puedes hacer un **fork** y enviar un **pull request** con mejoras en la estructura del código o documentación.

Para cualquier duda, ¡contáctame! 😊



