#Librerias
import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

#Configurarción Páginas
st.set_page_config(
	page_title = 'Caso Mercado Libre',
	page_icon = '🛒',
	)

st.title('***Alan Arturo Vargas Andrade***')
st.title('Sobre Mi')

with st.expander("Saber un poco más"):
    st.write("""
        Soy el tipo de persona que no le teme a los desafíos, me gusta aportar innovación y motivación al equipo de trabajo. \n 
        Me describo como una persona dinámica, analítica, con gran facilidad para aprender y orientado a resultados. \n
    """)


st.header('Experiencia Profesional')

with st.expander("Saber un poco más"):
    st.write("""
        Cuento con experiencia en manipulación e interpretación de datos. \n 
        Las herramientas que más uso son; SQL, Power BI, Python y Excel.
    """)

st.header('Empleos Anteriores')

tab1, tab2, tab3, tab4, tab5 = st.tabs(["IQVIA", "Rappi", "MexWürst", "Wonder World Media",'Antoeli'])

with tab1:
   st.subheader("Data Analyst")
   st.caption('2021 - presente')
   st.markdown('- Uso de bases de datos (SSIS, SQL, Access)')
   st.markdown('- Automatización de movimientos de datos y transformación de los mismos, ETL (Extraction, Transformation and Load)')
   st.markdown('- Implementación de soluciones de BI')
   st.markdown('- Extracción y transformación de datos Sell Out Sell In')
   st.markdown('- Análisis de la integridad de la Base de Datos')
   st.markdown('- Análisis y diseño de reportes para dirección general y clientes')
   #st.markdown('')
with tab2:
   st.subheader("Analista Retail CPG´s")
   st.caption('2019 - 2020')
   st.markdown('- Implementación de metodología Agile Scrum(reducción de backlog, tiempo de finalización y entrega de tareas, reducción de errores en promociones)')
   st.markdown('- Montaje de tiendas, productos y precios en aplicación y Web (CMS)')
   st.markdown('- Actualización y depuración de base de datos (SQL)')
   st.markdown('- Implementación de nuevos procesos internos dentro de la aplicación con el área Tech')

with tab3:
   st.subheader("Especialista en Marketing")
   st.caption('2018 - 2019')
   st.markdown('- Análisis de portafolio de productos')
   st.markdown('- Análisis económico, financiero y operaciones')
   st.markdown('- Dirección del cambio de la imagen corporativa' )
   st.markdown('- Creación e implementación de estrategía de marketing (Web, SEO, SEM y app)')

with tab4:
   st.subheader("Internship 🇪🇸")
   st.caption('2017 - 2018')
   st.markdown('- Prácticas profesionales en España en el área de gestión comercial y marketing digital.')
   st.markdown('- Búsqueda de mercados no cubiertos en el área metropolitana de Barcelona')
   st.markdown('- Diseño e implementación de estrategias de marketing digital (RRSS, Web, e-commerce, tradicional)')
   st.markdown('- Organización y planificación de eventos corporativos')

with tab5:
   st.subheader("Asesor de Ventas")
   st.caption('2017')
   st.markdown('- Orientación y asesoría al cliente en la elección del equipo adecuado a sus necesidades, brindando demostraciones pre-venta, para una elección adecuada conforme a lo requerido.')
   st.markdown('- Detección de necesidades específicas del cliente, generando confianza y satisfacción, incluyendo dentro del proceso de venta la asesoría de los requerimientos de instalación y mantenimiento, en la post-venta manteniendo contacto al cliente verificando la satisfacción y seguimiento de sus necesidades')

st.header('Educación')
tab5, tab6, tab7 = st.tabs(['Máster Universitario 🇪🇸','Licenciatura 🇲🇽','Diploma'])

with tab5:
	st.subheader('Dirección de Marketing y Gestión Comercial')
	st.markdown('EAE BUSINESS SCHOOL / UNIVERSITAT POLITÈCNICA DE CATALUNYA')
	st.caption('2017 - 2018')

with tab6:
	st.subheader('Química')
	st.markdown('Universidad La Salle')
	st.caption('2012 - 2016')

with tab7:
	st.subheader('Big Data')
	st.markdown('Fundación Carlos Slim / SEP')
	st.caption('527 horas / 2021')







