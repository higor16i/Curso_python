import streamlit as st

#Tabula

st.title("TÁBUADA")
st.header("Ánalise de calculadora para tabuada")
multiplicante = None
try:
    multiplicante=int(st.text_input("Insira o número para a tabuada (de 1 a 10)"))
    for i in range(1,11):
        multiplicador = int(multiplicante * i)
        st.write(f"\n{multiplicante} * {1*i} = {multiplicador}")
except ValueError:
    if multiplicante == None:
        st.warning("Digite algum valor e pressione enter!")
    else:
        st.error("Digite somente números inteiros!")