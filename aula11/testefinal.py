import streamlit as st

st.title("Altura média e menores de 16")

n = st.number_input("Quantas pessoas?", min_value=1, step=1)

nomes = []
idades = []
alturas = []

for i in range(int(n)):
    nomes.append(st.text_input(f"Nome {i+1}", key=f"nome{i}"))
    idades.append(st.number_input(f"Idade {i+1}", min_value=0, step=1, key=f"idade{i}"))
    alturas.append(st.number_input(f"Altura {i+1} (m)", min_value=0.0, step=0.01, key=f"altura{i}"))

if st.button("Calcular"):
    media = sum(alturas) / len(alturas)
    menores = [nomes[i] for i in range(len(nomes)) if idades[i] < 16]
    porcent = (len(menores) / len(nomes)) * 100

    st.write(f"Altura média: {media:.2f} m")
    st.write(f"Porcentagem com menos de 16 anos: {porcent:.1f}%")
    if menores:
        st.write("Nomes dos menores de 16:")
        for nome in menores:
            st.write(nome)
    else:
        st.write("Nenhum menor de 16.")
