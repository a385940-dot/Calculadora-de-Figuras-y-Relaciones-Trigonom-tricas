import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Titulos
st.title("Calculadora de Figuras y Relaciones Trigonométricas")
st.sidebar.write("Nombre: Alexa Gabriela Torres")
st.sidebar.write("Matricula: 385940")
tab1, tab2 = st.tabs(["Calculadora Geométrica", "Funciones Trigonométricas"])

# Códgio para Calculaora geométrica
with tab1:
    st.header("Calculadora de Áreas y Perímetros")
    # Selector para elegir la figura geométrica
    figura = st.selectbox("Selecciona una figura geométrica:",["Círculo", "Triángulo", "Rectángulo", "Cuadrado"])
    
    # Seleccionar el color de la figura
    color = st.color_picker("Elige un color para la figura", "#00f900")

    if figura == "Círculo":
        st.subheader("Círculo")
        radio = st.number_input("Ingresa el radio (r):", min_value=0.1, value=5.0, step=0.1)
        
        area_circulo = np.pi * radio**2
        perimetro_circulo = 2 * np.pi * radio

        col1, col2 = st.columns(2)
        col1.metric("Área", f"{area_circulo:.2f}")
        col2.metric("Perímetro", f"{perimetro_circulo:.2f}")

        fig, ax = plt.subplots()
        circulo = plt.Circle((0, 0), radio, color=color, fill=True)
        ax.add_artist(circulo)
        ax.set_aspect('equal')
        ax.set_xlim(-radio - 1, radio + 1)
        ax.set_ylim(-radio - 1, radio + 1)
        plt.title("Visualización del Círculo")
        st.pyplot(fig)

    elif figura == "Triángulo":
        st.subheader("Triángulo (Rectángulo)")
        base = st.number_input("Ingresa la base (b):", min_value=0.1, value=10.0, step=0.1)
        altura = st.number_input("Ingresa la altura (h):", min_value=0.1, value=5.0, step=0.1)
        
        area_triangulo = 0.5 * base * altura
        hipotenusa = np.sqrt(base**2 + altura**2)
        perimetro_triangulo = base + altura + hipotenusa

        col1, col2 = st.columns(2)
        col1.metric("Área", f"{area_triangulo:.2f}")
        col2.metric("Perímetro", f"{perimetro_triangulo:.2f}")
        
        fig, ax = plt.subplots()
        puntos = np.array([[0, 0], [base, 0], [0, altura]])
        triangulo = plt.Polygon(puntos, color=color, fill=True)
        ax.add_patch(triangulo)
        ax.set_aspect('equal')
        ax.set_ylim(-1, altura + 1)
        ax.set_xlim(-1, base + 1)
        plt.title("Visualización del Triángulo")
        st.pyplot(fig)

    elif figura == "Rectángulo":
        st.subheader("Rectángulo")
        base_rect = st.number_input("Ingresa la base (b):", min_value=0.1, value=8.0, step=0.1)
        altura_rect = st.number_input("Ingresa la altura (h):", min_value=0.1, value=4.0, step=0.1)

        area_rectangulo = base_rect * altura_rect
        perimetro_rectangulo = 2 * (base_rect + altura_rect)

        col1, col2 = st.columns(2)
        col1.metric("Área", f"{area_rectangulo:.2f}")
        col2.metric("Perímetro", f"{perimetro_rectangulo:.2f}")

        fig, ax = plt.subplots()
        rectangulo = plt.Rectangle((0, 0), base_rect, altura_rect, color=color, fill=True)
        ax.add_patch(rectangulo)
        ax.set_aspect('equal')
        ax.set_xlim(-1, base_rect + 1)
        ax.set_ylim(-1, altura_rect + 1)
        plt.title("Visualización del Rectángulo")
        st.pyplot(fig)

    elif figura == "Cuadrado":
        st.subheader("Cuadrado")
        lado = st.number_input("Ingresa la longitud del lado (l):", min_value=0.1, value=6.0, step=0.1)
        
        area_cuadrado = lado**2
        perimetro_cuadrado = 4 * lado
        
        col1, col2 = st.columns(2)
        col1.metric("Área", f"{area_cuadrado:.2f}")
        col2.metric("Perímetro", f"{perimetro_cuadrado:.2f}")

        fig, ax = plt.subplots()
        cuadrado = plt.Rectangle((0, 0), lado, lado, color=color, fill=True)
        ax.add_patch(cuadrado)
        ax.set_aspect('equal')
        ax.set_xlim(-1, lado + 1)
        ax.set_ylim(-1, lado + 1)
        plt.title("Visualización del Cuadrado")
        st.pyplot(fig)

# -----------------------------------------------------------
# 4. CÓDIGO DE LA SEGUNDA PESTAÑA (Funciones Trigonométricas)
# -----------------------------------------------------------
with tab2:
    st.header("Graficador de Funciones Trigonométricas")

    # Selector para la función trigonométrica
    funcion = st.selectbox(
        "Selecciona una función:",
        ["Seno", "Coseno", "Tangente"]
    )

    # Sliders para controlar amplitud y rango
    amplitud = st.slider("Amplitud", 0.1, 5.0, 1.0)
    rango_max = st.slider("Rango (en múltiplos de π)", 1, 10, 2)
    
    # Generar los valores de x en el rango especificado
    x = np.linspace(0, rango_max * np.pi, 500)
    
    if funcion == "Seno":
        st.subheader(f"Función: f(x) = {amplitud} * sin(x)")
        y = amplitud * np.sin(x)
        st.line_chart(y)

    elif funcion == "Coseno":
        st.subheader(f"Función: f(x) = {amplitud} * cos(x)")
        y = amplitud * np.cos(x)
        st.line_chart(y)

    elif funcion == "Tangente":
        st.subheader(f"Función: f(x) = {amplitud} * tan(x)")
        y = amplitud * np.tan(x)
        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.set_ylim(-10, 10) # Limitar el eje y para una mejor visualización
        ax.set_title("Gráfica de la Tangente")
        ax.grid(True)
        st.pyplot(fig)
