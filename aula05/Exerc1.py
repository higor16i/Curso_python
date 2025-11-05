import streamlit as st
import math as mt
TITULO = "calculo da area de um quadrado, triangulo e trapezio"
st.markdown(f"<h1 style='text-align: center;'> {TITULO}</h1>", unsafe_allow_html=True)
medidaA= st.number_input("inserir a medida A:",min_value=0.0)
medidaB= st.number_input("inserir a medida B:",min_value=0.0)
medidaC= st.number_input("inserir a medida C:",min_value=0.0)
areaquadrado= mt.pow(medidaA,2)
areatriangulo= (medidaA*medidaB)/2
areatrapezio= ((medidaA+medidaB)*medidaC)/2
st.markdown("<h2 style='text-align: left;'> Resultados:</h2>", unsafe_allow_html=True)
st.write(f"a area do quadrado é de {areaquadrado:.4f} metros quadrados.")
st.write(f"a area do triangulo é de {areatriangulo:.4f} metros quadrados.")
st.write(f"a area do trapezio é de {areatrapezio:.4f} metros quadrados.")

