import streamlit as st
import random

st.set_page_config(page_title="Ecuaciones de primer grado", page_icon="🧮")

st.title("🧮 Resolviendo ecuaciones de primer grado")

# --- Generar la ecuación aleatoria ---
if "a" not in st.session_state:
    st.session_state.a = random.randint(1, 10)
    st.session_state.b = random.randint(-10, 10)
    st.session_state.x = random.randint(-10, 10)
    st.session_state.c = st.session_state.a * st.session_state.x + st.session_state.b

st.write("Resuelve la ecuación:")

ecuacion = f"{st.session_state.a}x + {st.session_state.b} = {st.session_state.c}"
st.latex(ecuacion)

# --- Campo para ingresar la respuesta ---
respuesta = st.number_input("Ingresa el valor de x (solo enteros):", step=1, format="%d")

# --- Botón para verificar ---
if st.button("Verificar"):
    if respuesta == st.session_state.x:
        st.success("🎉 ¡Correcto! Bien hecho.")
        st.balloons()
        # Reiniciar con nueva ecuación
        st.session_state.a = random.randint(1, 10)
        st.session_state.b = random.randint(-10, 10)
        st.session_state.x = random.randint(-10, 10)
        st.session_state.c = st.session_state.a * st.session_state.x + st.session_state.b
    else:
        st.error("❌ Incorrecto. Intenta de nuevo.")
