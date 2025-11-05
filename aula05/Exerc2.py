import streamlit as st
TITULO = "cálculo da duração de tempo"
st.set_page_config(page_title=TITULO)
st.title(TITULO)
tempo = st.number_input("inserir o tempo em segundos:")
horas = tempo // 3600
minutos = (tempo % 3600) // 60
segundos = tempo % 6
st.write(f"{horas} horas, {minutos} minutos e {segundos} segundos.")