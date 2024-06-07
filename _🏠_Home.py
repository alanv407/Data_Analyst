#Libreries
import streamlit as st
import pandas as pd
import time

#Configurarción Páginas
st.set_page_config(
	page_title = 'Portfolio',
	page_icon = '💼',
	)
st.title('Home Page')

st.header('Personal Portfolio 💼.')

with st.container(border=True):
    st.subheader('Use of this Web App')
    st.markdown('On the left side are the different parts of this presentation; Home, About me and Case Analysis, if applicable you will also find some filters.')

with st.container(border=True):
    st.subheader('More info')
    st.caption('In some cases you will find a box like the one shown below, by clicking you will see more information')
    with st.expander("Know a little more"):
        st.write("""
            This is an example 
        """)
with st.container(border=True):
    st.subheader('Tabs')
    st.caption('In other cases you will find Tabs, to see the information of each one you just have to click on each one')
    tab1, tab2 = st.tabs(['Tab 1','Tab 2'])
    with tab1:
        st.caption('Tab 1')
        st.write("""This is an example in Tab 1""")
    with tab2:
        st.caption('Tab 2')
        st.write("""This is another example in Tab 2""")
	
with st.container(border=True):    
    st.markdown('**You can find the code for this Web App GitHub in:** https://github.com/alanv407/Data_Analyst')

if st.button("Let's get started!"):
    st.toast('Hip!')
    time.sleep(.5)
    st.toast('Hip!')
    time.sleep(.5)
    st.toast('Hooray!', icon='🎉')

