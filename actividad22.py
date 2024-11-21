import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Configuración de la página
st.set_page_config(page_title="Optimización No Lineal", layout="wide")

# Estilo personalizado
st.markdown("""
    <style>
    .main {
        background-color: #f7f2f2;
    }
    .title {
        color: #5a5a5a;
        font-size: 30px;
        font-weight: bold;
        text-align: center;
    }
    .subtitle {
        color: #8b5b93;
        font-size: 24px;
        font-weight: bold;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Título y subtítulo
st.markdown('<div class="title">UNIVERSIDAD NACIONAL DEL ALTIPLANO</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">NELIDA ARACELY QUISPE CALATAYUD</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.header("Actividad: Optimización No Lineal")

### EJERCICIO 1 ###
if st.button('Ejercicio 1: Demostrar que $f(x) = 3x + 2$ es convexa en $\\mathbb{R}$'):
    st.subheader("Ejercicio 1: Demostrar que $f(x) = 3x + 2$ es convexa en $\\mathbb{R}$")
    st.markdown("""
    1. **Definición de convexidad:**  
       Una función es convexa si cumple:  
       \\[
       f(\\lambda x_1 + (1 - \\lambda)x_2) \\leq \\lambda f(x_1) + (1 - \\lambda)f(x_2), \\quad \\forall \\lambda \\in [0, 1].
       \\]  
       Además, si $f(x)$ es dos veces diferenciable, una función es convexa si:  
       \\[
       f''(x) \\geq 0 \\quad \\forall x \\in \\mathbb{R}.
       \\]

    2. **Evaluación de la función:**  
       Sea $f(x) = 3x + 2$. Como $f(x)$ es lineal, verificamos la convexidad usando la segunda derivada.

    3. **Primera derivada:**  
       \\[
       f'(x) = 3.
       \\]

    4. **Segunda derivada:**  
       \\[
       f''(x) = 0.
       \\]

    5. **Criterio de convexidad:**  
       Como $f''(x) = 0 \\geq 0$, $f(x)$ es convexa.
    """)
    # Gráfico Ejercicio 1
    x1 = np.linspace(-10, 10, 100)
    y1 = 3 * x1 + 2
    fig1, ax1 = plt.subplots()
    ax1.plot(x1, y1, label="$f(x) = 3x + 2$", color='purple')
    ax1.set_title("Gráfico de $f(x) = 3x + 2$")
    ax1.set_xlabel("$x$")
    ax1.set_ylabel("$f(x)$")
    ax1.legend()
    st.pyplot(fig1)

### EJERCICIO 2 ###
if st.button('Ejercicio 2: Verificar si $f(x) = x^3$ es convexa, cóncava o ninguna en $[0, \\infty)$'):
    st.subheader("Ejercicio 2: Verificar si $f(x) = x^3$ es convexa, cóncava o ninguna en $[0, \\infty)$")
    st.markdown("""
    1. **Definición de convexidad y concavidad:**  
       - Convexa si $f''(x) \\geq 0$.  
       - Cóncava si $f''(x) \\leq 0$.

    2. **Evaluación de la función:**  
       \\[
       f(x) = x^3.
       \\]

    3. **Primera derivada:**  
       \\[
       f'(x) = 3x^2.
       \\]

    4. **Segunda derivada:**  
       \\[
       f''(x) = 6x.
       \\]

    5. **Análisis del signo de $f''(x)$:**  
       - $f''(x) > 0$ para $x > 0 \\Rightarrow$ Convexa.  
       - $f''(x) = 0$ para $x = 0$.  

       Por lo tanto, $f(x)$ es **convexa** en $[0, \\infty)$.
    """)
    # Gráfico Ejercicio 2
    x2 = np.linspace(-2, 2, 100)
    y2 = x2**3
    fig2, ax2 = plt.subplots()
    ax2.plot(x2, y2, label="$f(x) = x^3$", color='green')
    ax2.axhline(0, color='black', linewidth=0.5)
    ax2.axvline(0, color='black', linewidth=0.5)
    ax2.set_title("Gráfico de $f(x) = x^3$")
    ax2.set_xlabel("$x$")
    ax2.set_ylabel("$f(x)$")
    ax2.legend()
    st.pyplot(fig2)

### EJERCICIO 3 ###
if st.button('Ejercicio 3: Comprobar si $f(x) = x^2 - 4x + 5$ es convexa'):
    st.subheader("Ejercicio 3: Comprobar si $f(x) = x^2 - 4x + 5$ es convexa")
    st.markdown("""
    1. **Evaluación de convexidad:** Verificamos el signo de la segunda derivada.  

    2. **Primera derivada:**  
       \\[
       f'(x) = 2x - 4.
       \\]

    3. **Segunda derivada:**  
       \\[
       f''(x) = 2.
       \\]

    4. **Criterio de convexidad:**  
       Como $f''(x) = 2 > 0$, la función es **convexa**.
    """)
    # Gráfico Ejercicio 3
    x3 = np.linspace(-2, 6, 100)
    y3 = x3**2 - 4*x3 + 5
    fig3, ax3 = plt.subplots()
    ax3.plot(x3, y3, label="$f(x) = x^2 - 4x + 5$", color='blue')
    ax3.set_title("Gráfico de $f(x) = x^2 - 4x + 5$")
    ax3.set_xlabel("$x$")
    ax3.set_ylabel("$f(x)$")
    ax3.legend()
    st.pyplot(fig3)

### EJERCICIO 4(a) ###
if st.button('Ejercicio 4(a): Verificar la convexidad de $f(x) = \\ln(x)$ en $[1, \\infty)$'):
    st.subheader("Ejercicio 4(a): Verificar la convexidad de $f(x) = \\ln(x)$ en $[1, \\infty)$")
    st.markdown("""
    1. **Primera derivada:**  
       \\[
       f'(x) = \\frac{1}{x}.
       \\]

    2. **Segunda derivada:**  
       \\[
       f''(x) = -\\frac{1}{x^2}.
       \\]

    3. **Análisis del signo:**  
       - Para $x > 0$, $f''(x) < 0 \\Rightarrow$ No es convexa.  
       - $f(x)$ es **cóncava**.
    """)
    # Gráfico Ejercicio 4(a)
    x4a = np.linspace(1, 10, 100)
    y4a = np.log(x4a)
    fig4a, ax4a = plt.subplots()
    ax4a.plot(x4a, y4a, label="$f(x) = \\ln(x)$", color='orange')
    ax4a.set_title("Gráfico de $f(x) = \\ln(x)$")
    ax4a.set_xlabel("$x$")
    ax4a.set_ylabel("$f(x)$")
    ax4a.legend()
    st.pyplot(fig4a)

### EJERCICIO 5 ###
if st.button('Ejercicio 5: Verificar la convexidad de $f(x) = \\sqrt{x}$ en $[0, \\infty)$'):
    st.subheader("Ejercicio 5: Verificar la convexidad de $f(x) = \\sqrt{x}$ en $[0, \\infty)$")
    st.markdown("""
    1. **Primera derivada:**  
       \\[
       f'(x) = \\frac{1}{2\\sqrt{x}}.
       \\]

    2. **Segunda derivada:**  
       \\[
       f''(x) = -\\frac{1}{4x^{3/2}}.
       \\]

    3. **Análisis del signo:**  
       - $f''(x) < 0$ para $x > 0 \\Rightarrow$ La función es **cóncava**.
    """)
    # Gráfico Ejercicio 5
    x5 = np.linspace(0.1, 10, 100)
    y5 = np.sqrt(x5)
    fig5, ax5 = plt.subplots()
    ax5.plot(x5, y5, label="$f(x) = \\sqrt{x}$", color='red')
    ax5.set_title("Gráfico de $f(x) = \\sqrt{x}$")
    ax5.set_xlabel("$x$")
    ax5.set_ylabel("$f(x)$")
    ax5.legend()
    st.pyplot(fig5)
