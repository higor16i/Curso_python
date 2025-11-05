import streamlit as st
import math as mt
st.header("Calculadora de Bhaskara")
st.write("calculadora de raizes de uma \n equação do segundo grau")
st.write("ax² + bx + c = 0")
a = st.text_input("valor de a:",)
b = st.text_input("valor de b:",)
c = st.text_input("valor de c:",)

if st.button("calcular raizes"):
    try:
        a = float(a)
        b = float(b)
        c = float(c)
        delta=mt.pow(b,2)- 4 * a *c
        st.write(f"o valor de delta é: {delta}")
        if delta <0:
            st.warning("não existem raizes reais para essa equação.")
        elif delta ==0:
            raiz= (-b + mt.sqrt(delta)) / (2 * a)
            st.success(f"a equação possui uma raiz real: {raiz}")
        else:
            raiz1= (-b + mt.sqrt(delta)) / (2 * a)
            raiz2= (-b - mt.sqrt(delta)) / (2 * a)
            st.success(f"a equação possui duas raizes reais: {raiz1} e {raiz2}")
    except:
        st.error("por favor, insira valores numéricos válidos para a, b e c.")