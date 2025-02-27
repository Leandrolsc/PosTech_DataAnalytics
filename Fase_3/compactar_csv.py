import os
import pandas as pd

# Diretórios
input_dir = r'Fase_3\files\dados_brutos'
output_dir = r'Fase_3\files\microdados'

os.makedirs(output_dir, exist_ok=True)


csv_files = [f for f in os.listdir(input_dir) if f.endswith('.csv')]

for csv_file in csv_files:
    csv_path = os.path.join(input_dir, csv_file)
    
    df = pd.read_csv(csv_path)
    
    parquet_file = os.path.splitext(csv_file)[0] + '.parquet'
    
    parquet_path = os.path.join(output_dir, parquet_file)
    
    df.to_parquet(parquet_path, compression='gzip')

print("Conversão concluída!")