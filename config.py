# config.py
import os

RAW_DATA_PATH = "/content/drive/MyDrive/ML/clueter_np/data_raw/marketing_campaign.csv"
PROCESSED_DATA_PATH = "/content/drive/MyDrive/ML/clueter_np/data_processd/processin_data_marketing_campaign.csv"
LOG_REPORT_PATH = "/content/drive/MyDrive/ML/clueter_np/resultados_processamento/relatorio_processamento.txt"

# Cria diretórios se não existirem
os.makedirs(os.path.dirname(PROCESSED_DATA_PATH), exist_ok=True)
os.makedirs(os.path.dirname(LOG_REPORT_PATH), exist_ok=True)
