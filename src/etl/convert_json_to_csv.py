import pandas as pd
import json
import os

# Define input and output file paths
input_path = "/mnt/c/Users/alexv/Azure-Spark-SQL-Databricks-Pipeline/data/jsonplaceholder_posts.json"
output_path = "/mnt/c/Users/alexv/Azure-Spark-SQL-Databricks-Pipeline/data/jsonplaceholder_posts.csv"

# Check if the JSON file exists
if not os.path.exists(input_path):
    print(f" Error: The file {input_path} does not exist.")
    exit()

# Load JSON data
try:
    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)  # Read JSON file
except Exception as e:
    print(f" Error reading JSON file: {e}")
    exit()

# Convert JSON data to a Pandas DataFrame
df = pd.DataFrame(data)

# Save DataFrame as CSV
try:
    df.to_csv(output_path, index=False, encoding="utf-8")
    print(f" Conversion successful. CSV file saved at: {output_path}")
except Exception as e:
    print(f" Error saving CSV file: {e}")

