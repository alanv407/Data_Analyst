#Librerias
import streamlit as st
import pandas as pd
import plotly.express as px

#Configurarción Páginas
st.set_page_config(
	page_title = 'Case Analysis',
	page_icon = '🛒',
	)
st.title('Home')

st.header('Take Home Exercise.')
st.subheader('About this Web App')
st.markdown('For the development of this Web App the Python programming language was used, the following libraries were used; Pandas, Plotly and Streamlit')

st.subheader('Use of this Web App')
st.markdown('On the left side are the different parts of this presentation; Home, About me and Case Analysis, if applicable you will also find some filters, at the bottom is the code used for this Web App')

st.subheader('More info')
st.caption('In some cases you will find a box like the one shown below, by clicking you will see more information')
with st.expander("know a little more"):
    st.write("""
        This is an example 
    """)

st.subheader('Tabs')
st.caption('In other cases you will find Tabs, to see the information of each one you just have to click on each one')
tab1, tab2 = st.tabs(['Tab 1','Tab 2'])

with tab1:
   st.caption('Tab 1')
   st.write("""
        This is an example in Tab 1
    """)

with tab2:
   st.caption('Tab 2')
   st.write("""
        This is another example in Tab 2
       """)
	
st.write('You can find the code for this page in: https://github.com/alanv407/Data_Analyst')
st.title('Lets get started!')
