import pandas as pd
import json
import os

# Definie paths de entrada y salida
input_path = "/mnt/c/Users/alexv/Azure-Spark-SQL-Databricks-Pipeline/data/jsonplaceholder_posts.json"
output_path = "/mnt/c/Users/alexv/Azure-Spark-SQL-Databricks-Pipeline/data/jsonplaceholder_posts.csv"

# Verificar si el archivo JSON existe
if not os.path.exists(input_path):
    print(f" Error: El archivo {input_path} no existe.")
    exit()

# Cargar JSON
try:
    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)  # Cargar el archivo JSON
except Exception as e:
    print(f" Error al leer el JSON: {e}")
    exit()

# Convertir a DataFrame
df = pd.DataFrame(data)

# Guardar como CSV
try:
    df.to_csv(output_path, index=False, encoding="utf-8")
    print(f" Conversión exitosa. Archivo CSV guardado en: {output_path}")
except Exception as e:
    print(f" Error al guardar el CSV: {e}")
