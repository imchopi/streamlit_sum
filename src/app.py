import streamlit as st

st.title("Título de la APP")
st.write("Contenido de la APP")

n1 = st.slider("Introduce el primer número", 0, 200, 10)
n2 = st.slider("Introduce el segundo número", 0, 200, 10)

# Suma los números
sum = int(n1) + int(n2)
st.write("La suma es: ", sum)