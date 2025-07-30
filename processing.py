# processing.py
import pandas as pd
from typing import Tuple
from logger import logger

def ler_dados(path: str) -> pd.DataFrame:
    """
    Lê dados de um arquivo separado por tabulação.

    Parameters
    ----------
    path : str
        Caminho do arquivo.

    Returns
    -------
    DataFrame
        Dados carregados.
    """
    try:
        df = pd.read_csv(path, sep="\t")
        logger.info("Arquivo carregado com sucesso.")
        return df
    except Exception as e:
        logger.error(f"Erro ao carregar o arquivo: {e}")
        return pd.DataFrame()


def composicao_df(df: pd.DataFrame) -> str:
    """
    Gera informações estruturais sobre o DataFrame.

    Parameters
    ----------
    df : DataFrame
        Base de dados.

    Returns
    -------
    str
        Texto com resumo da estrutura.
    """
    linhas, colunas = df.shape
    tipos = df.dtypes.value_counts()

    resumo = [
        "**Estrutura da Base de Dados**\n",
        f"- Total de linhas: {linhas} | colunas: {colunas}",
        "- Colunas:",
    ] + [f"  • {col}" for col in df.columns] + [
        f"- Tipos de dados:\n{tipos.to_string()}"
    ]
    return "\n".join(resumo)


def variaveis_categoricas(df: pd.DataFrame) -> str:
    """
    Resume as variáveis categóricas.

    Parameters
    ----------
    df : DataFrame
        Base de dados.

    Returns
    -------
    str
        Resumo textual.
    """
    resultado = ["\n**Variáveis Categóricas**"]
    for col in df.select_dtypes(include="object").columns:
        unicos = df[col].unique()
        resultado.append(f"\n- {col}:")
        resultado.append(f"  • Valores únicos: {df[col].nunique()}")
        resultado.append(f"  • Exemplos: {unicos[:5]}")
    return "\n".join(resultado)


def tratar_data(df: pd.DataFrame) -> Tuple[pd.Timestamp, pd.Timestamp]:
    """
    Converte coluna de data.

    Parameters
    ----------
    df : DataFrame
        Base de dados.

    Returns
    -------
    Tuple
        Data mínima e máxima.
    """
    df["Dt_Customer"] = pd.to_datetime(df["Dt_Customer"], dayfirst=True, errors="coerce")
    return df["Dt_Customer"].min(), df["Dt_Customer"].max()


def analisar_nulos(df: pd.DataFrame) -> str:
    """
    Calcula a proporção de valores ausentes.

    Parameters
    ----------
    df : DataFrame

    Returns
    -------
    str
        Texto com estatísticas de nulos.
    """
    na = df.isna().sum()
    total = df.shape[0]
    percentual = na / total * 100

    texto = [
        "\n**Valores Nulos**",
        f"Total de nulos: {df.isna().sum().sum()}",
        pd.DataFrame({"total": na, "percentual": percentual}).to_string()
    ]
    return "\n".join(texto)


def estatisticas_numericas(df: pd.DataFrame) -> str:
    """
    Calcula estatísticas básicas para variáveis numéricas.

    Parameters
    ----------
    df : DataFrame

    Returns
    -------
    str
        Texto com estatísticas descritivas.
    """
    linhas = ["\n**Estatísticas Numéricas**"]
    for col in df.select_dtypes(include="number").columns:
        stats = df[col].agg(["min", "max", "mean"])
        linhas.append(f"\n- {col}:\n{stats.to_string()}")
    return "\n".join(linhas)
