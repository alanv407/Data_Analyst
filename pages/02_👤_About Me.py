#Libreries
import streamlit as st
import pandas as pd

#CPage Configuration
st.set_page_config(
	page_title = 'About Me',
	page_icon = ' 👨',
   initial_sidebar_state="expanded"
	)

st.title('**Arturo Vargas**')

st.header("Data & Analytics | Data Analyst")

st.divider()

st.subheader('About Me')

with st.expander("Summary"):
    st.markdown("""
         - Highly motivated and results-oriented professional with 4 years of experience in Data Science. Proven ability to leverage strong analytical skills and attention to detail. Adept at working collaboratively in fast-paced environments.
         - Experience in Data Analyst, Data Management (MDM) and Data Steward.
    """)


st.subheader('Skills')

with st.expander("Skills"):
    st.markdown("""
                I have experience handling and interpreting data.
                
                The tools that I use most are:
                  
                  - SQL (Snowflake ❄️, MS Server, Redash)
                  - 🐍 Python (Jupyter Notebook, Pandas, Numpy, MatplotLib, Plotly, Streamlit)
                  - Power BI
                  - MS Office: Word, Excel, Power Point
    """)

st.divider()

st.header('Experience')

with st.container(border=True):

   tab5, tab4, tab3, tab2, tab1 = st.tabs(["Nissan", "IQVIA", "Rappi", "MexWürst", "Wonder World Media"])

   with tab5:
      st.subheader("Sr. Data Specialist")
      st.caption('2023 - today')
      st.markdown("""
                  - Gather and process information from various internal and internal sources of customer and marketing data.
                  - Perform validation processes to ensure data accuracy, completeness, and consistency.
                  - Identify and analyze problems, errors, defects, and other problems in the database.
                  - Responsible for ongoing data quality & data cleansing initiatives to fix identified issues.
                  """)
      
   with tab4:
      st.subheader("Data Analyst")
      st.caption('2021 - 2022')
      st.markdown("""
                  - Analysis and design of reports for general management and clients (Power BI, Python).
                  - Automation of data movements and their transformation, ETL (Extraction, Transformation and Load).
                  - Market analysis and commercial indicators.
                  - Price analysis, market penetration, new product launch, market share, growth elements, etc.
                  - Incentive analysis for sales force.
                  - Solve doubts from strategic clients about our data.
                  - Use of databases (SSIS, MS Server SQL, Access, Python).
                  """)
      
   with tab3:
      st.subheader("Retail  Analyst")
      st.caption('2019 - 2020')
      st.markdown("""
                  - Updating and debugging of database (Redase SQL).
                  - QA Retail CPG’s.
                  - Assembly of stores, products and prices in application and Web (Internal CMS).
                  - Implementation of Scrum Agile reducing errors and backlog.
                  """)

   with tab2:
      st.subheader("Marketing Scientist")
      st.caption('2018 - 2019')
      st.markdown("""
                  - Data Mining
                  - Data visualization
                  - Creation and execution digital marketing strategies (RRSS, web, SEO, SEM, Blogs, app).""")

   with tab1:
      st.subheader("Internship 🇪🇸")
      st.caption('2017 - 2018')
      st.markdown('- Assistant in the sales process')
      st.markdown('- Management of various events for the promotion of the brand')
      st.markdown('- Management of clearance sales events')

st.divider()

st.header('Education')

with st.container(border=True):

   tab5, tab6, tab7 = st.tabs(['Máster 🇪🇸','Bachelor 🇲🇽','Diploma'])

   with tab5:
      st.subheader('Marketing Management')
      st.markdown('''
                  EAE Business School / Universitat Politècnica de Catalunya
                  Attended in Barcelone Spain''')
      st.caption('2017 - 2018')

   with tab6:
      st.subheader('Chemical Engineering ')
      st.markdown('Universidad La Salle (ULSA)')
      st.caption('2012 - 2016')

   with tab7:
      st.subheader('Big Data')
      st.markdown('Fundación Carlos Slim / SEP')
      st.caption('527 horas / 2021')
