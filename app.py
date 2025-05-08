import streamlit as st
import pandas as pd
from PIL import Image

df = pd.read_excel("base_de_requisicoes.xlsx")

df.columns = df.columns.str.strip()

st.set_page_config(layout="wide", page_title="Requisições Operacionais", page_icon="📋")

imagem = Image.open("logo.png")

col1, col2 = st.columns([1, 1])
with col1:
    st.image(imagem, width=100)
with col2:
    st.markdown("<h1 style='margin-bottom: 0;'>Requisições<br>Operacionais</h1>", unsafe_allow_html=True)

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