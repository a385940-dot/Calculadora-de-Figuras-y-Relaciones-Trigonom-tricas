import streamlit as st
st.tittle ("Calculadora de Figuras y Relaciones Trigonométricas")
figura_elegida=st.selectbox ("Selecciona una figura:", ("Círculo", "Triángulo", "Rectángulo", "Cuadrado"))
st.write(f"Tu figura elegida es: {figura_elegida}")
