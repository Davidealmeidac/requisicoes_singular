import streamlit as st
import pandas as pd
from PIL import Image
from io import BytesIO
import base64

# Função para converter imagem em base64
def imagem_to_base64(img):
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

# Configuração da página
st.set_page_config(layout="wide", page_title="Requisições Operacionais", page_icon="📋")

# Carrega a logo e o dataframe
imagem = Image.open("logo.png")
df = pd.read_excel("base_de_requisicoes.xlsx")
df.columns = df.columns.str.strip()

# --- Logo centralizada ---
st.markdown(
    """
    <div style="display: flex; justify-content: center;">
        <img src="data:image/png;base64,{}" width="100">
    </div>
    """.format(imagem_to_base64(imagem)),
    unsafe_allow_html=True
)

# --- Título centralizado ---
st.markdown("<h1 style='text-align: center; margin-top: 10px;'>Requisições Operacionais</h1>", unsafe_allow_html=True)

# Linha divisória (opcional)
st.markdown("---")

# --- Filtros e tabela (ocupando a largura total) ---
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

# Aplica filtros
for col, valores in filtros.items():
    df = df[df[col].isin(valores)]

# Exibe os resultados
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

st.subheader("📑 Resultado das Requisições")
st.dataframe(df[colunas_exibicao], use_container_width=True)