import streamlit as st
import math

nome = st.text_input("Insira seu nome")
st.write(f"Olá, {nome}!")

ladoA = st.number_input("Insira o primeiro lado", format="%.2f")
ladoB = st.number_input("Insira o segundo lado", format="%.2f")
ladoC = st.number_input("Insira o terceiro lado", format="%.2f")
if ladoA + ladoB > ladoC and ladoA + ladoC > ladoB and ladoB + ladoC > ladoA:
    p = (ladoA + ladoB + ladoC) / 2  
    area = math.sqrt(p * (p - ladoA) * (p - ladoB) * (p - ladoC))
    st.write(f"Os lados formam um triângulo. Perímetro = {ladoA + ladoB + ladoC:.2f}")
    st.write(f"Área do triângulo (Heron) = {area:.2f}")
else:
    area_trapezio = ((ladoA + ladoB) * ladoC) / 2
    st.write(f"Isso forma um trapézio cuja área é {area_trapezio:.2f}")

