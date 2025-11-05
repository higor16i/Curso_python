import streamlit as st 
st.title("classificação de niveis de glicose no sangue")
st.markdown(
    """
|nivel de glicose  | classificação | 
|------------------|---------------|
| até 100 mg/dL    | normal        |
| 101 a 140 mg/dL  | elevado       |
|acima de 140 mg/dL| muito alto    |
"""
)
glicose = st.number_input("qual o nivel de glicose no seu sangue?", min_value=0)
if st.button("classificar"):
    if glicose <=100:
        st.write("classificação: normal")
    elif glicose >100 and glicose <=140:
        st.write("classificação: elevado")
    else:
        st.error("nivel de glicose muito alto.")
st.selectbox("selecione a qual estado voce pertence:", ["São paulo", "Rio de janeiro", "Minas gerais", "Bahia", "Ceará", "Amazonas", "Paraná", "Rio grande do sul", "Santa catarina", "Pernambuco", "Paraíba", "Maranhão", "Goiás", "Distrito federal", "Mato grosso", "Mato grosso do sul", "Espírito santo", "Rondônia", "Tocantins", "Acre", "Amapá", "Roraima", "Alagoas", "Sergipe", "Piauí", "Rio grande do norte", "Ceará", "Bahia", "Minas gerais"])