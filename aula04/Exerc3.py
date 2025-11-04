import streamlit as st

st.title("problema Terreno")
st.write("digite a largura do terreno em metros:")
largura = st.number_input("Largura (m):",)
st.write("digite o comprimento do terreno em metros:")
comprimento = st.number_input("Comprimento (m):",)
st.write("digite o valor do metro quadrado do terreno:")
valor = st.number_input("Valor (R$):",)
area = largura * comprimento
valortotal = area * valor

st.write(f"A área do terreno é de {area:.2f} metros quadrados.")
st.write(f"O preço total do terreno é de R$ {valortotal:.2f}.")