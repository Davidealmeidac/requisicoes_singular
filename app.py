import streamlit as st
import pandas as pd

# Carregar a planilha
df = pd.read_excel(r"C:\Users\davi.costa\Documents\base_de_requisicoes.xlsx")

# Renomear colunas para facilitar (caso necessário)
df.columns = df.columns.str.strip()

# Título
st.set_page_config(layout="wide", page_title="Requisições Operacionais", page_icon="📋")
st.title("📋 Requisições operacionais")

# Lista de filtros com campos desejados
colunas_filtro = [
    'Solicitante',
    'Colaborador',
    'Colaborador ausente',
    'Motivo da cob.',
    'Tipo de movimentação',
    'Data da solicitação'
]

# Filtros em formato de lista com pesquisa
filtros = {}
for col in colunas_filtro:
    opcoes = df[col].dropna().unique().tolist()
    selecao = st.multiselect(f"Filtrar por {col}:", options=opcoes, key=col)
    if selecao:
        filtros[col] = selecao

# Aplicar os filtros
for col, valores in filtros.items():
    df = df[df[col].isin(valores)]

# Colunas finais da tabela
colunas_exibicao = [
    'Solicitante',
    'Data da solicitação',
    'Matrícula',
    'Colaborador',
    'Colaborador ausente',
    'Tipo de movimentação',
    'Recurso de cobertura',
    'Motivo da cob.',
    'Data Início',
    'Posto'
]

st.markdown("---")
st.subheader("📑 Resultado das Requisições")

# Exibir tabela (com rolagem horizontal para mobile)
st.dataframe(df[colunas_exibicao], use_container_width=True)
