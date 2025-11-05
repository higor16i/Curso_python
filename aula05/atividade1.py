import streamlit as st 

st.title("calculadora de troco")

valorun = st.number_input("inserir o preço do produto:", min_value=0.0, step=0.01)
quantidade = st.number_input("inserir a quantidade de produtos comprados:", min_value=1, step=1)
total_compra = valorun * quantidade
valor_pago = st.number_input("inserir o valor pago pelo cliente:", min_value=total_compra, step=0.01)
troco = valor_pago - total_compra
st.write(f"O valor unitário do produto é: R$ {valorun:.2f}")
st.write(f"A quantidade de produtos comprados é: {quantidade}")
st.write(f"O total da compra é: R$ {total_compra:.2f}")
st.write(f"O troco a ser devolvido ao cliente é: R$ {troco:.2f}")