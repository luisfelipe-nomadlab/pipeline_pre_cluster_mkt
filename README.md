# Pipeline de Pré-processamento de Dados para Análise de Cluster

Este projeto contém um pipeline em Python para o pré-processamento e análise exploratória inicial de dados de campanha de marketing, com foco em preparação para análise de cluster.

---

## Estrutura do Projeto

- `config.py`  
  Configura caminhos dos arquivos de dados brutos, dados processados e logs. Cria diretórios automaticamente se não existirem.

- `logger.py`  
  Configura o logger para registrar mensagens de informação e erro tanto no console quanto em arquivo.

- `processing.py`  
  Funções responsáveis por:  
  - leitura dos dados  
  - sumarização da estrutura do DataFrame  
  - análise de variáveis categóricas  
  - tratamento da coluna de datas  
  - análise de valores nulos  
  - estatísticas descritivas para variáveis numéricas

- `pipeline.py`  
  Orquestra a execução das funções do módulo `processing.py`, gera um relatório via logger e salva o dataset processado em arquivo CSV.

---

## Como usar

1. Configure os caminhos para os seus arquivos no `config.py`, especialmente:  
   - `RAW_DATA_PATH` (arquivo CSV/tabulado com dados brutos)  
   - `PROCESSED_DATA_PATH` (local onde o CSV processado será salvo)  
   - `LOG_REPORT_PATH` (local para salvar o arquivo de log)

2. Execute o pipeline:  
   ```bash
   python pipeline.py
3. Verifique os logs gerados em LOG_REPORT_PATH para informações sobre o processamento.

4. Os dados processados estarão salvos no caminho configurado em PROCESSED_DATA_PATH.

## Requisitos
* Python 3.7+
* Pandas

## Descrição das funções principais
* ler_dados(path: str) -> pd.DataFrame
Lê arquivo CSV separado por tabulação e retorna um DataFrame.

* composicao_df(df: pd.DataFrame) -> str
Gera resumo da estrutura do DataFrame (linhas, colunas, tipos e nomes).

* variaveis_categoricas(df: pd.DataFrame) -> str
Resume as variáveis categóricas e mostra exemplos de valores únicos.

* tratar_data(df: pd.DataFrame) -> Tuple[pd.Timestamp, pd.Timestamp]
Converte a coluna Dt_Customer para datetime e retorna intervalo mínimo e máximo.

* analisar_nulos(df: pd.DataFrame) -> str
Calcula e apresenta a proporção e total de valores ausentes.

* estatisticas_numericas(df: pd.DataFrame) -> str
Calcula estatísticas básicas (mínimo, máximo e média) para colunas numéricas.

## Logs e Relatórios
Durante a execução, o pipeline gera um relatório consolidado no arquivo de log configurado, 
contendo informações sobre a composição dos dados, variáveis categóricas, intervalo de datas, valores nulos e estatísticas numéricas.

## Objetivo
Este pipeline visa preparar os dados para análises de cluster, garantindo um entendimento inicial da base, tratamento básico e exportação para etapas seguintes.
