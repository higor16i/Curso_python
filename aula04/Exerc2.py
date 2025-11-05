import streamlit as st
import math as mt
st.title("problema Retângulo")
base = st.number_input("Digite a base do retângulo (em metros):",min_value=0.0)
altura = st.number_input("Digite a altura do retângulo (em metros):",min_value=0.0)

area = base * altura
perimetro = 2 * base + altura * 2
x = mt.pow(base, 2) + mt.pow(altura, 2)
diagonal = mt.sqrt(x)
st.write(f"A área do retângulo é de {area:.2f} metros quadrados.")
st.write(f"O perímetro do retângulo é de {perimetro:.2f} metros.")
st.write(f"A diagonal do retângulo é de {diagonal:.2f} metros.")            