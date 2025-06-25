import streamlit as st
from predict import prever_atraso

st.set_page_config(page_title="Previsão de Atraso", layout="centered")
st.title("⏳ Previsão de Atraso de Tarefas com IA")

# Inputs
estimativa = st.slider("Estimativa (horas)", 1, 24, 8)
tipo = st.selectbox("Tipo da tarefa", ["feature", "bug", "melhoria"])
prioridade = st.selectbox("Prioridade", ["baixa", "média", "alta"])

if st.button("Prever"):
    resultado = prever_atraso(estimativa, tipo, prioridade)
    if resultado == 1:
        st.error("🚨 Esta tarefa tem ALTA CHANCE de atraso!")
    else:
        st.success("✅ Esta tarefa provavelmente será entregue no prazo.")
