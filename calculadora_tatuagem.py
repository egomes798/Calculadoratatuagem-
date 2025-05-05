import streamlit as st

# Configuração de página
st.set_page_config(page_title="Calculadora de Tatuagem", page_icon="🖋", layout="centered")

# Logo do estúdio (use o link da sua logo hospedada)
st.markdown(
    """
    <div style="text-align: center;">
        <img src="https://imgur.com/a/lILAZuj" alt="Egomes.Ink" width="200">
    </div>
    """,
    unsafe_allow_html=True
)

# Estilo visual neutro e moderno
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

# Entrada para o tamanho da tatuagem (em cm)
altura_cm = st.number_input("Altura da tatuagem (em cm)", min_value=1, max_value=50, value=10)

# Definição da base de tamanho com a nova regra de 25cm ou mais
if altura_cm <= 5:
    base_tamanho = 150
elif altura_cm <= 15:
    base_tamanho = 250
elif altura_cm <= 25:
    base_tamanho = 400
else:
    base_tamanho = 500  # Para tamanhos de 25cm ou mais

# Complexidade
complexidade = st.selectbox("Complexidade do desenho", ["Simples", "Média", "Alta"])
fatores_complexidade = {
    "Simples": 1.2,
    "Média": 1.6,
    "Alta": 2.2
}
fator_complexidade = fatores_complexidade[complexidade]

# Local do corpo
local = st.selectbox("Local do corpo", ["Braço/Perna", "Costas/Costela"])
fatores_local = {
    "Braço/Perna": 1.5,
    "Costas/Costela": 2.2
}
fator_local = fatores_local[local]

# Estilo
estilo = st.selectbox("Estilo", ["Fine line", "Realismo"])
fatores_estilo = {
    "Fine line": 1.8,
    "Realismo": 2.8
}
fator_estilo = fatores_estilo[estilo]

# Cálculo do valor final
valor_final = base_tamanho * fator_complexidade * fator_local * fator_estilo

# Garantir valor mínimo
valor_final = max(valor_final, 200)

st.markdown(f"## Valor estimado: **R$ {valor_final:,.2f}**")
