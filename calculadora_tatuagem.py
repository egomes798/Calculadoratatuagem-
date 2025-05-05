import streamlit as st

# Estilo com cores neutras e toques de roxo
st.set_page_config(page_title="Calculadora de Tatuagem", page_icon="🖋", layout="centered")

# Logo no topo (substitua o link pela URL da sua logo no GitHub ou Imgur)
st.markdown(
    """
    <div style="text-align: center;">
        <img src="https://i.imgur.com/YOUR_LOGO.png" alt="Egomes.Ink" width="200">
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
        body {
            background-color: #f5f5f5;
        }
        .main {
            background-color: #ffffff;
            padding: 2rem;
            border-radius: 10px;
        }
        h1, h2, h3 {
            color: #3a3a3a;
        }
        .stButton>button {
            background-color: #6f42c1;
            color: white;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Calculadora de Tatuagem")

# Entrada: altura da tatuagem em cm
altura_cm = st.slider("Altura da tatuagem (cm)", 1, 50, 10)

# Classificar tamanho
if altura_cm <= 5:
    base_tamanho = 150
elif altura_cm <= 15:
    base_tamanho = 250
else:
    base_tamanho = 400

# Complexidade
complexidade = st.selectbox("Complexidade do desenho", ["Simples", "Média", "Alta"])
fatores_complexidade = {
    "Simples": 1.5,
    "Média": 2.0,
    "Alta": 2.5
}
fator_complexidade = fatores_complexidade[complexidade]

# Local do corpo
local = st.selectbox("Local do corpo", ["Braço/Perna", "Costas/Costela"])
fatores_local = {
    "Braço/Perna": 2.0,
    "Costas/Costela": 2.6
}
fator_local = fatores_local[local]

# Estilo
estilo = st.selectbox("Estilo", ["Fine line", "Realismo"])
fatores_estilo = {
    "Fine line": 2.5,
    "Realismo": 3.5
}
fator_estilo = fatores_estilo[estilo]

# Cálculo final
valor_final = base_tamanho * fator_complexidade * fator_local * fator_estilo

# Valor mínimo garantido
valor_final = max(valor_final, 200)

st.markdown(f"## Valor estimado: **R$ {valor_final:,.2f}**")
