import streamlit as st
import random
import time

st.set_page_config(page_title="Ecuaciones de Primer Grado", page_icon="🧠")

st.title("🧮 Resolver Ecuaciones de Primer Grado")

# Generar ecuación aleatoria
a = random.randint(1, 10)
x_real = random.randint(1, 20)
b = random.randint(0, 10)

resultado = a * x_real + b
ecuacion = f"{a}x + {b} = {resultado}"

st.subheader("Resuelve la siguiente ecuación:")
st.latex(ecuacion)

# Campo para la respuesta (solo enteros)
respuesta = st.number_input("Ingresa el valor de x (solo números enteros)", step=1, format="%d")

# Botón para verificar
if st.button("Verificar"):
    if respuesta == x_real:
        st.success("✅ ¡Correcto!")
        st.balloons()
    else:
        st.error("❌ Incorrecto. Intenta de nuevo.")
