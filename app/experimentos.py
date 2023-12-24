import pandas as pd

# Ruta al archivo CSV
csv_file_path = 'data.csv'  # Reemplaza con la ruta de tu archivo

# Leer el archivo CSV
df = pd.read_csv(csv_file_path)

# Mostrar las primeras 5 filas y las primeras 5 columnas
print(df.iloc[:10, :10])