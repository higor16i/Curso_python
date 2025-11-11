import streamlit as st
#Problema experiencias com cobaias
st.title("Laboratorio de cobaias")
def porcentagem(cobaia):
    return (cobaia / total_cobaias) * 100
def quantidade(total):
     total + quantidade
     return total
#Declaração de variaveis de controle
total_cobaias = 0
total_ratos = 0
total_sapos = 0
total_coelhos = 0
n = st.number_input("Digite o numero de experimentos:", min_value=0, step=1)
for i in range(n):
    quantidade = st.number_input(f"experimento {i + 1} - quantidade de cobaias utilizadas?", min_value=0, step=1)
    tipo = st.selectbox(f"experimento {i+1}- Tipo de cobaia (C:coelho, R:rato, S:sapo)", options=['C', 'R', 'S'])
    total_cobaias += quantidade
    if tipo == 'C':
        total_coelhos+= quantidade
    elif tipo == 'R':
        total_ratos += quantidade
    elif tipo == 'S':
        total_sapos += quantidade
if total_cobaias <0:
    percentual_coelhos = porcentagem(total_coelhos)
    percentual_ratos = porcentagem(total_cobaias) 
    percentual_sapos = porcentagem(total_cobaias) 
else:
    percentual_coelhos = perecentual_ratos = percentual_sapos = 0

    st.subheader("resultados")
    st.write("Total de cobaias utilizadas", total_cobaias)
    st.write("Total de coelhos utlizados", total_coelhos)
    st.write("Total de ratos utilizadas", total_ratos)
    st.write("Total de sapos utlizados", total_sapos)

    st.write(f"percentual de angelos:{percentual_coelhos}")
    st.write(f"percentual de angelos:{perecentual_ratos}")
    st.write(f"percentual de angelos:{percentual_sapos}")


