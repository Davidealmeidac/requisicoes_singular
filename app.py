import streamlit as st
import pandas as pd
from PIL import Image

df = pd.read_excel("base_de_requisicoes.xlsx")

df.columns = df.columns.str.strip()

st.set_page_config(layout="wide", page_title="Requisições Operacionais", page_icon="📋")

col1, col2 = st.columns([3, 7])  # Ajuste os valores para controlar o tamanho relativo

with col1:
    imagem = Image.open("logo.png")
    st.image(imagem, width=150)

with col2:
    st.title("Requisições Operacionais")
colunas_filtro = [
    'Solicitante',
    'Colaborador',
    'Colaborador ausente',
    'Motivo da cob.',
    'Tipo de movimentação',
    'Data da solicitação'
]

filtros = {}
for col in colunas_filtro:
    opcoes = df[col].dropna().unique().tolist()
    selecao = st.multiselect(f"Filtrar por {col}:", options=opcoes, key=col)
    if selecao:
        filtros[col] = selecao

for col, valores in filtros.items():
    df = df[df[col].isin(valores)]

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

st.dataframe(df[colunas_exibicao], use_container_width=True)