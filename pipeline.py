# pipeline.py
from config import RAW_DATA_PATH, PROCESSED_DATA_PATH
from processing import (
    ler_dados,
    composicao_df,
    variaveis_categoricas,
    tratar_data,
    analisar_nulos,
    estatisticas_numericas
)
from logger import logger

def pipeline() -> None:
    """
    Executa o pipeline de processamento de dados.
    """
    df = ler_dados(RAW_DATA_PATH)

    if df.empty:
        logger.error("DataFrame está vazio. Pipeline interrompido.")
        return

    relatorio = []
    relatorio.append(composicao_df(df))
    relatorio.append(variaveis_categoricas(df))

    min_data, max_data = tratar_data(df)
    relatorio.append(f"\n**Intervalo de Datas:**\n- Mínima: {min_data}\n- Máxima: {max_data}")

    relatorio.append(analisar_nulos(df))
    relatorio.append(estatisticas_numericas(df))

    logger.info("\n\n".join(relatorio))

    df.to_csv(PROCESSED_DATA_PATH, index=False)
    logger.info(f"Dados processados salvos em: {PROCESSED_DATA_PATH}")


if __name__ == "__main__":
    pipeline()
