import pandas as pd
import streamlit as st 
import plotly.express as px 

# leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# encabezado
st.header("Análisis Exploratorio de Anuncios de Venta de Vehículos")

# crear un botón para construir el histograma
hist_button = st.button('Construir histograma')

if hist_button: # al hacer click en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
    
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
    
# crear casillas de verificación
show_histogram = st.checkbox('Mostrar histograma')
show_scatter = st.checkbox('Mostrar gráfico de dispersión')

if show_histogram: # si la casilla del histograma está seleccionada
    st.write('Creación de un histograma para el conjunto de datos')
    fig = px.histogram(car_data, x="odometer", title="Distribución del Odómetro (Kilometraje)")
    st.plotly_chart(fig, use_container_width=True)
    
if show_scatter: # si la casilla del gráfico de dispersión está seleccionada
    st.write('Creación de un gráfico de dispersión para la relación entre precio y odómetro')
    fig = px.scatter(car_data, x="odometer", y="price", title="Precio vs. Odómetro (Kilometraje)")
    st.plotly_chart(fig, use_container_width=True)

