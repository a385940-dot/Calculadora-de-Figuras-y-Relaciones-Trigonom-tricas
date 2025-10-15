# Importar las bibliotecas necesarias
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Configurar el título principal de la aplicación
st.title("Calculadora de Figuras y Relaciones Trigonométricas")

# Crear pestañas para separar las secciones de la aplicación
tab1, tab2 = st.tabs(["Calculadora Geométrica", "Funciones Trigonométricas"])

# --- Pestaña de Calculadora Geométrica (Parte 1 y 2) ---
with tab1:
    st.header("Calculadora de Áreas y Perímetros")

    # 1. Selector para elegir la figura geométrica
    figura = st.selectbox(
        "Selecciona una figura geométrica:",
        ["Círculo", "Triángulo", "Rectángulo", "Cuadrado"]
    )

    # Widget para seleccionar el color de la figura
    color = st.color_picker("Elige un color para la figura", "#00f900")

    # 2. Lógica para mostrar parámetros y realizar cálculos según la figura
    if figura == "Círculo":
        st.subheader("Círculo")
        radio = st.number_input("Ingresa el radio (r):", min_value=0.1, value=5.0, step=0.1)
        
        # 3. Cálculos
        area_circulo = np.pi * radio**2  # Fórmula: A = π * r^2 [cite: 8]
        perimetro_circulo = 2 * np.pi * radio  # Fórmula: P = 2 * π * r [cite: 8]

        # 4. Mostrar resultados
        col1, col2 = st.columns(2)
        col1.metric("Área", f"{area_circulo:.2f}")
        col2.metric("Perímetro", f"{perimetro_circulo:.2f}")

        # Visualización de la figura
        fig, ax = plt.subplots()
        circulo = plt.Circle((0, 0), radio, color=color, fill=True)
        ax.add_artist(circulo)
        ax.set_aspect('equal')
        ax.set_xlim(-radio - 1, radio + 1)
        ax.set_ylim(-radio - 1, radio + 1)
        plt.title("Visualización del Círculo")
        st.pyplot(fig)

    elif figura == "Triángulo": # Asumimos un triángulo rectángulo para facilitar la visualización
        st.subheader("Triángulo (Rectángulo)")
        base = st.number_input("Ingresa la base (b):", min_value=0.1, value=10.0, step=0.1)
        altura = st.number_input("Ingresa la altura (h):", min_value=0.1, value=5.0, step=0.1)
        
        # 3. Cálculos
        area_triangulo = 0.5 * base * altura # Fórmula: A = 1/2 * b * h [cite: 9]
        hipotenusa = np.sqrt(base**2 + altura**2) # Teorema de Pitágoras
        perimetro_triangulo = base + altura + hipotenusa # Fórmula: P = a + b + c [cite: 9]

        # 4. Mostrar resultados
        col1, col2 = st.columns(2)
        col1.metric("Área", f"{area_triangulo:.2f}")
        col2.metric("Perímetro", f"{perimetro_triangulo:.2f}")
        
        # Visualización de la figura
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

        # 3. Cálculos
        area_rectangulo = base_rect * altura_rect # Fórmula: A = b * h [cite: 10]
        perimetro_rectangulo = 2 * (base_rect + altura_rect) # Fórmula: P = 2 * (b + h) [cite: 10]

        # 4. Mostrar resultados
        col1, col2 = st.columns(2)
        col1.metric("Área", f"{area_rectangulo:.2f}")
        col2.metric("Perímetro", f"{perimetro_rectangulo:.2f}")

        # Visualización de la figura
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
        
        # 3. Cálculos
        area_cuadrado = lado**2 # Fórmula: A = l^2 [cite: 11]
        perimetro_cuadrado = 4 * lado # Fórmula: P = 4l [cite: 11]
        
        # 4. Mostrar resultados
        col1, col2 = st.columns(2)
        col1.metric("Área", f"{area_cuadrado:.2f}")
        col2.metric("Perímetro", f"{perimetro_cuadrado:.2f}")

        # Visualización de la figura
        fig, ax = plt.subplots()
        cuadrado = plt.Rectangle((0, 0), lado, lado, color=color, fill=True)
        ax.add_patch(cuadrado)
        ax.set_aspect('equal')
        ax.set_xlim(-1, lado + 1)
        ax.set_ylim(-1, lado + 1)
        plt.title("Visualización del Cuadrado")
        st.pyplot(fig)

  # --- Pestaña de Funciones Trigonométricas (Parte 3) ---
with tab2:
    st.header("Graficador de Funciones Trigonométricas")

    # 1. Selector para la función trigonométrica
    funcion = st.selectbox(
        "Selecciona una función:",
        ["Seno", "Coseno", "Tangente"]
    )

    # 2. Sliders para controlar amplitud y rango
    amplitud = st.slider("Amplitud", 0.1, 5.0, 1.0) [cite: 35]
    rango_max = st.slider("Rango (en múltiplos de π)", 1, 10, 2)
    
    # Generar los valores de x en el rango especificado
    x = np.linspace(0, rango_max * np.pi, 500)
    
    # 3. Calcular y graficar la función seleccionada
    if funcion == "Seno":
        st.subheader(f"Función: $f(x) = {amplitud} \cdot \sin(x)$")
        y = amplitud * np.sin(x) # Fórmula: sin(x) [cite: 34]
        st.line_chart(y)

    elif funcion == "Coseno":
        st.subheader(f"Función: $f(x) = {amplitud} \cdot \cos(x)$")
        y = amplitud * np.cos(x) # Fórmula: cos(x) [cite: 34]
        st.line_chart(y)

    elif funcion == "Tangente":
        st.subheader(f"Función: $f(x) = {amplitud} \cdot \\tan(x)$")
        y = amplitud * np.tan(x) # Fórmula: tan(x) [cite: 34]
        # Para la tangente, es mejor usar matplotlib para controlar los límites del eje y
        # y evitar que las asíntotas distorsionen la gráfica.
        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.set_ylim(-10, 10) # Limitar el eje y para una mejor visualización
        ax.set_title("Gráfica de la Tangente")
        ax.grid(True)
        st.pyplot(fig)

  streamlit run app.py
