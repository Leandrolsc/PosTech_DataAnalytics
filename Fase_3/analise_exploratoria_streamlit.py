import pandas as pd
import streamlit as st
import os

# Carregar os datasets
dicionario_052020 = pd.read_csv(r'files/dicionarios/dicionarios(052020).csv', encoding='latin1', sep=';')
dicionario_062020 = pd.read_csv(r'files/dicionarios/dicionarios(062020).csv', encoding='latin1', sep=';')
dicionario_072020 = pd.read_csv(r'files/dicionarios/dicionarios(072020).csv', encoding='latin1', sep=';')
dicionario_082020 = pd.read_csv(r'files/dicionarios/dicionarios(082020).csv', encoding='latin1', sep=';')
dicionario_092020 = pd.read_csv(r'files/dicionarios/dicionarios(092020).csv', encoding='latin1', sep=';')
dicionario_102020 = pd.read_csv(r'files/dicionarios/dicionarios(102020).csv', encoding='latin1', sep=';')
dicionario_112020 = pd.read_csv(r'files/dicionarios/dicionarios(112020).csv', encoding='latin1', sep=';')

# Concatenar todos os datasets
all_dictionaries = pd.concat([
    dicionario_052020[['codigo', 'descricao']],
    dicionario_062020[['codigo', 'descricao']],
    dicionario_072020[['codigo', 'descricao']],
    dicionario_082020[['codigo', 'descricao']],
    dicionario_092020[['codigo', 'descricao']],
    dicionario_102020[['codigo', 'descricao']],
    dicionario_112020[['codigo', 'descricao']]
], axis=0).drop_duplicates().reset_index(drop=True)

# Criar um novo DataFrame para marcar a presença dos códigos
presence_df = pd.DataFrame({
    'codigo': all_dictionaries['codigo'],
    'descricao': all_dictionaries['descricao'],
    '052020': all_dictionaries['codigo'].isin(dicionario_052020['codigo']),
    '062020': all_dictionaries['codigo'].isin(dicionario_062020['codigo']),
    '072020': all_dictionaries['codigo'].isin(dicionario_072020['codigo']),
    '082020': all_dictionaries['codigo'].isin(dicionario_082020['codigo']),
    '092020': all_dictionaries['codigo'].isin(dicionario_092020['codigo']),
    '102020': all_dictionaries['codigo'].isin(dicionario_102020['codigo']),
    '112020': all_dictionaries['codigo'].isin(dicionario_112020['codigo'])
})

# Contabilizar quantos True existem em cada coluna
aggregation = presence_df[['052020', '062020', '072020', '082020', '092020', '102020', '112020']].sum()

# Função para contar valores não nulos em cada coluna de um DataFrame
def count_non_nulls(df):
    return df.count()

# Diretório dos arquivos Parquet
input_dir = r'files/microdados'

# Listar todos os arquivos Parquet no diretório de entrada
parquet_files = [f for f in os.listdir(input_dir) if f.endswith('.parquet')]

# Dicionário para armazenar os resultados
results = {}

# Processar cada arquivo Parquet
for parquet_file in parquet_files:
    # Caminho completo do arquivo Parquet
    parquet_path = os.path.join(input_dir, parquet_file)
    
    # Ler o arquivo Parquet
    df = pd.read_parquet(parquet_path)
    
    # Contar valores não nulos em cada coluna
    counts = count_non_nulls(df)
    
    # Armazenar o resultado no dicionário
    results[parquet_file] = counts

# Criar um DataFrame com os resultados
count_df = pd.DataFrame(results).fillna(0).astype(int)

# Adicionar a descrição dos códigos
count_df = count_df.reset_index().rename(columns={'index': 'codigo'})
count_df = count_df.merge(all_dictionaries[['codigo', 'descricao']], on='codigo', how='left')
count_df = count_df.set_index(['codigo', 'descricao'])

# Streamlit app
st.title('Análise Exploratória dos Dicionários de Microdados')
st.write("""
Visualizar como os microdados estão distribuídos. Existem 7 arquivos referentes aos dados de maio de 2020 a novembro de 2020. 
Dessa forma, foram distribuídos dicionários diferentes. Esta primeira etapa tem como objetivo analisar os dicionários para saber a diferença entre eles antes de começar a análise dos dados.
""")

# Criar abas
tab1, tab2 = st.tabs(["Presença dos Códigos", "Contagem de Valores Não Nulos"])

with tab1:
    # Filtros
    st.sidebar.header('Filtros')
    selected_columns = st.sidebar.multiselect('Selecione os meses', ['052020', '062020', '072020', '082020', '092020', '102020', '112020'], default=['052020', '062020', '072020', '082020', '092020', '102020', '112020'])

    # Filtrar o DataFrame com base nos filtros selecionados
    filtered_df = presence_df[['codigo', 'descricao'] + selected_columns]

    # Exibir a tabela
    st.dataframe(filtered_df)

    # Exibir o rodapé com a contagem total
    st.write('### Contagem Total')
    st.write(aggregation[selected_columns].to_frame().T)

with tab2:
    # Exibir a tabela de contagem de valores não nulos
    st.write('### Contagem de Valores Não Nulos por Coluna')
    st.dataframe(count_df)