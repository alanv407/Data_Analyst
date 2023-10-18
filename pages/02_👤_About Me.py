#Librerias
import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

#Configurarción Páginas
st.set_page_config(
	page_title = 'Case Analysis',
	page_icon = '🛒',
	)

st.title('***Arturo Vargas***')
st.title('About Me')

with st.expander("Know a bit more"):
    st.write("""
        I am the kind of person who is not afraid of challenges, I like to bring innovation and motivation to the work team. \n 
        I describe myself as a dynamic, analytical person, easy to learn and results-oriented. \n
    """)


st.header('Skills')

with st.expander("Skills"):
    st.write("""
        I have experience handling and interpreting data. \n
        The tools that I use most are; SQL, Power BI, Python and Excel.
    """)

st.header('Previous jobs')

tab6, tab1, tab2, tab3, tab4, tab5 = st.tabs(["Nissan", "IQVIA", "Rappi", "MexWürst", "Wonder World Media",'Antoeli'])

with tab6:
   st.subheader("Data Specialist")
   st.caption('2023')
   st.markdown('- Gather and process information from various internal and external sources of customer and marketing data.')
   st.markdown('- Mantain access to the data, ingest, process, cleanse, format, store and distribute data.')
   st.markdown('Validation of vendors ETL´s process')
	
with tab1:
   st.subheader("Data Analyst")
   st.caption('2021 - 2022')
   st.markdown('- Analysis of the integrity of the Database')
   st.markdown('- Use of databases(SSIS, SQL, Access)')
   st.markdown('- ETL development (Extraction, Transformation and Load)')
   st.markdown('- Market analysis and commercial indicators, incentive analysis for sales force')
   st.markdown('- Analysis and design of reports for general management and clients (Power BI)')
   #st.markdown('')
with tab2:
   st.subheader("Retail CPG´s Analyst")
   st.caption('2019 - 2020')
   st.markdown('- QA Retail CPGs')
   st.markdown('- Assembly of stores, products and prices in application and Web (CMS)')
   st.markdown('- Updating and debugging of database (SQL)')
   st.markdown('- Implementation of Agile Scrum methodology (reduction of backlog, completion time and delivery of tasks, reduction of errors in promotions)')

with tab3:
   st.subheader("Marketing scientist")
   st.caption('2018 - 2019')
   st.markdown('- Data Mining')
   st.markdown('- Data visualization')
   st.markdown('- Creation and execution digital marketing strategies (RRSS, web, SEO, SEM, Blogs, app). ')

with tab4:
   st.subheader("Internship 🇪🇸")
   st.caption('2017 - 2018')
   st.markdown('- Assistant in the sales process')
   st.markdown('- Management of various events for the promotion of the brand')
   st.markdown('- Management of clearance sales events')

st.header('Education')
tab5, tab6, tab7 = st.tabs(['Máster 🇪🇸','Bachelor 🇲🇽','Diploma'])

with tab5:
	st.subheader('Marketing Management')
	st.markdown('EAE BUSINESS SCHOOL / UNIVERSITAT POLITÈCNICA DE CATALUNYA')
	st.caption('2017 - 2018')

with tab6:
	st.subheader('Chemical Engineering ')
	st.markdown('Universidad La Salle')
	st.caption('2012 - 2016')

with tab7:
	st.subheader('Big Data')
	st.markdown('Fundación Carlos Slim / SEP')
	st.caption('527 horas / 2021')
