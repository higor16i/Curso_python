import streamlit as st

#Problema lanchonete
st.title("lanchonte do clodoauto")
st.header("Menu de opções do restaurante")
st.subheader("Opções de lanches")
st.markdown(
"""
|codigo|Descrição do item| Preço  |
|------|-----------------|--------|
|1001  |X-Burguer        |R$ 8,00 |
|1002  |X-SENAI          |R$ 10,00|
|1003  |X-Campeão        |R$ 12,00|
|1004  |X-ESP32          |R$ 15,00|
|1005  |X-C37            |R$ 18,00|
"""
)
opcao = st.selectbox("Selecione o codigo do lanche desejado:",
                                options=["1001","1002","1003","1004","1005"])
codigo=int(opcao)
quantidade = st.number_input("digite a quantidade desejada", min_value=0)

match codigo:
    case 1001:
        preco = 8.00
    case 1002:
        preco = 10.00
    case 1003:
        preco = 12.00
    case 1004:
        preco = 15.00
    case 1005:
        preco = 18.00
total = preco * quantidade
st.subheader("total a pagar: R$" + (str(total)))