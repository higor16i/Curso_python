import streamlit as st 
st.title("problema Retângulo")
base = st.number_input("Digite a base do retângulo (em metros):",)
altura = st.number_input("Digite a altura do retângulo (em metros):",)
area = base * altura
perimetro = 2 * base + altura * 2
diagonal = (base**2 + altura**2)**0.5
st.write(f"A área do retângulo é de {area:.2f} metros quadrados.")
st.write(f"O perímetro do retângulo é de {perimetro:.2f} metros.")
st.write(f"A diagonal do retângulo é de {diagonal:.2f} metros.")            