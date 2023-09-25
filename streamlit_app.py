import streamlit as st
import requests
import re

def web_tech_detector(url):
    # Realizar la solicitud GET al sitio web
    response = requests.get(url)
    
    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        # Obtener el contenido HTML de la página
        html_content = response.text
        
        # Buscar pistas sobre el lenguaje de programación y la plataforma utilizados
        language = re.findall(r'<script.*?src=["\'](.*?)["\']', html_content)
        platform = re.findall(r'<link.*?href=["\'](.*?)["\']', html_content)
        
        # Mostrar los resultados en la aplicación de Streamlit
        st.write("Lenguaje de programación detectado:")
        st.write(set(language))
        
        st.write("Plataforma detectada:")
        st.write(set(platform))
    else:
        st.write("Error al acceder al sitio web")

# Configurar la interfaz de la aplicación de Streamlit
st.title("Detector de tecnología web")
url = st.text_input("Ingrese la URL del sitio web")

# Verificar si se ha ingresado una URL
if url:
    # Llamar a la función de detección de tecnología web
    web_tech_detector(url)
