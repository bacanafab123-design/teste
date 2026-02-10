import streamlit as st

# Configuração da página
st.title("🎂 Calculadora de Idade")
st.subheader("Transformando seu script Python em um site!")

# Criando as entradas de dados na interface
ano_nascimento = st.number_input("Entre com o ano em que nasceu:", min_value=1900, max_value=2026, value=2000)
ano_atual = st.number_input("Entre com o ano em que estamos:", min_value=2000, max_value=2026, value=2024)

# Usando um selectbox em vez de input de texto para evitar erros de digitação
ja_fez = st.radio("Você já fez aniversário esse ano?", ("Sim", "Não"))

# Lógica do seu código original
idade = ano_atual - ano_nascimento

if ja_fez == "Não":
    idade = idade - 1

# Exibindo o resultado de forma destacada
st.divider()
st.success(f"### Sua idade é **{idade}** anos.")