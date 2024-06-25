# Integración de FastAPI y Streamlit

Este proyecto demuestra la integración de FastAPI con Streamlit. La aplicación FastAPI proporciona una API RESTful para crear y recuperar elementos de una base de datos en PostgreSQL, mientras que la aplicación Streamlit proporciona una interfaz de usuario para interactuar con la API.


## Configuración e Instalación

   **Clonar el repositorio:**

   git clone https://github.com/dnl0037/cypherser.git
   cd <directorio-del-repositorio>

## Crear y activar un entorno virtual:

    python -m venv env
    source env/bin/activate  # En Windows usa `env\Scripts\activate`

## Instalar las dependencias requeridas:

    pip install -r requirements.txt

## Cambiar keys a base de datos 

## Ejecución de la Aplicación

  ### Iniciar la aplicación FastAPI:

  uvicorn app.main:app --reload

  ### Iniciar la aplicación Streamlit:
  
  streamlit run stream_app.py

