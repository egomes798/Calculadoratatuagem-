import streamlit as st

# Função para calcular o valor da tatuagem com base nos parâmetros
def calcular_valor(tamanho, complexidade, local, estilo):
    # Valores de Tamanho
    if tamanho == "Pequeno (Até 5cm)":
        valor_tamanho = 100
    elif tamanho == "Médio (5cm até 15cm)":
        valor_tamanho = 200
    elif tamanho == "Grande (15cm ou mais)":
        valor_tamanho = 400
    
    # Fatores de Complexidade
    if complexidade == "Simples":
        fator_complexidade = 1.5
    elif complexidade == "Média":
        fator_complexidade = 2.0
    elif complexidade == "Alta":
        fator_complexidade = 2.5

    # Valores para Local do Corpo
    if local == "Braço/Perna":
        valor_local = 200
    elif local == "Costas/Costela":
        valor_local = 350

    # Fatores de Estilo
    if estilo == "Fine line":
        fator_estilo = 2.5
    elif estilo == "Realismo":
        fator_estilo = 3.5

    # Calcular o valor final
    valor_final = valor_tamanho * fator_complexidade * (valor_local / 200) * fator_estilo

    return valor_final

# Título do app
st.title("Calculadora de Orçamento de Tatuagem")

# Seleção de Tamanho
tamanho = st.selectbox("Selecione o Tamanho da Tatuagem", ["Pequeno (Até 5cm)", "Médio (5cm até 15cm)", "Grande (15cm ou mais)"])

# Seleção de Complexidade
complexidade = st.selectbox("Selecione a Complexidade do Desenho", ["Simples", "Média", "Alta"])

# Seleção de Local do Corpo
local = st.selectbox("Selecione o Local do Corpo", ["Braço/Perna", "Costas/Costela"])

# Seleção de Estilo
estilo = st.selectbox("Selecione o Estilo de Tatuagem", ["Fine line", "Realismo"])

# Botão para calcular o valor
if st.button("Calcular Valor"):
    valor = calcular_valor(tamanho, complexidade, local, estilo)
    st.write(f"O valor estimado para a tatuagem é: R$ {valor:.2f}")
