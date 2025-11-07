import streamlit as st

def grafico(datsu1, datsu2, datsu3):
    st.subheader("Visualização dos lançamentos")
    st.area_chart([1, 2, 3, 4, 5, 6, datsu1],
                  use_container_width=True, height=200, color='#00FF00')
    st.area_chart([1, 2, 3, 4, 5, 6, datsu2],
                  use_container_width=True, height=200, color='#0000FF')
    st.area_chart([1, 2, 3, 4, 5, 6, datsu3],
                  use_container_width=True, height=200, color='#FF0000')

st.title("🎯 Simulação de lançamento de dardo 🎯")
st.write("Simulação de lançamento de três dardos. "
         "O objetivo é mostrar qual dardo atingiu a **maior distância**.")

st.header("Insira as três distâncias dos dardos lançados pelo jogador:")
coluna1, coluna2, coluna3 = st.columns(3)
with coluna1:
    dardo1 = st.number_input("Distância do 1° dardo (m)", min_value=0.0, step=0.1)
with coluna2:
    dardo2 = st.number_input("Distância do 2° dardo (m)", min_value=0.0, step=0.1)
with coluna3:
    dardo3 = st.number_input("Distância do 3° dardo (m)", min_value=0.0, step=0.1)

if dardo1 == dardo2 == dardo3:
    dardo_vencedor = "Empate total"
elif dardo1 == dardo2 and dardo1 > dardo3:
    dardo_vencedor = "Empate entre Dardo 1 e Dardo 2"
elif dardo1 == dardo3 and dardo1 > dardo2:
    dardo_vencedor = "Empate entre Dardo 1 e Dardo 3"
elif dardo2 == dardo3 and dardo2 > dardo1:
    dardo_vencedor = "Empate entre Dardo 2 e Dardo 3"
elif dardo1 > dardo2 and dardo1 > dardo3:
    dardo_vencedor = "Dardo 1"
elif dardo2 > dardo1 and dardo2 > dardo3:
    dardo_vencedor = "Dardo 2"
else:
    dardo_vencedor = "Dardo 3"

max_distancia = max(dardo1, dardo2, dardo3)

if st.button("Apresentar o maior lançamento"):
    st.subheader("🏆 Resultado:")
    if "Empate" in dardo_vencedor:
        st.write(f"**{dardo_vencedor}** com {max_distancia:.2f} m!")
    else:
        st.write(f"O vencedor foi o **{dardo_vencedor}** com {max_distancia:.2f} m!")
        grafico(dardo1, dardo2, dardo3)
