#Librerias
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff

#Configurarción Páginas
st.set_page_config(
	page_title = 'Supply Chain',
	page_icon = '🛒',
	)

st.title('📈📊 Cases Analysis 📈📊')

st.subheader('The objective of carrying out the project using this tool is as follows:')


with st.expander("know a little more"):
    st.write("""
	 - Being able to perform the exercise several times with updated data and in an automated way\n
         - Obtaining statistical data is much easier and faster than in Excel \n
         - In case of exceeding more than ±1,040,000 rows, we could not perform the exercise in Excel \n
    """)

#Obtención de la data
	#Guardar archivo en cahce interno para evitar que se actualice de forma seguida
cargar = st.file_uploader('Arrastra o selecciona el ejercicio en Excel para poder continuar')
if not cargar:
     st.warning('Adjuntar archivo para generar visualización del Análisis')
     st.stop()

@st.cache(allow_output_mutation=True)
def load_model(model_name):
     df=pd.read_excel(cargar, dtype={'route': str})
     return(df)
df=load_model(cargar)

df['DS%'] = ((df['deliveries']/df['shipments'])*100).round(2)

#DATA
st.header('What we have here?')
st.subheader('DataFrame')
st.caption('Only the first 100 rows are displayed')
st.dataframe(df.head(100))
st.write('The Dataframe dimensions are as follows (Rows, Columns):',df.shape)
with st.expander("Analysis result"):
    st.write("""
        The information contained in the Excel: \n
         - Dates, times, routes, cities, etc. \n
         - Dataframe dimension
         - Added Delivery Success calculation
    """)


st.header('We are asked to consider how to reach the following goals: \n - Achieve 99.5% Delivery Success (DS) \n - Achieve 125 shipments per Route')

#Preparación datos

st.subheader('Currently')
tab1, tab2 = st.tabs(['General info','General info2'])

with tab1:
   st.caption('Descriptive statistics information')
   st.dataframe(df.describe(include='all' ).transpose())
   st.write('The DataFrame dimensions are as follows (rows, columns):', df.shape)
   with st.expander("Results"):
    st.write("""
        - Uniques: \n
            -Date: 111  \n
            -Routes: 13,365  \n
            -Cities: 17 \n
            -City_cluster:58 \n
            -Carrier: 25
        - Date range: from 06-04-222 to 25-07-2022 
    """)

with tab2:
   st.caption('Descriptive statistics information')
   st.dataframe(df.describe().transpose())
   with st.expander("Results"):
    st.write("""
        - DS average is 98.19, 1.31% below target\n
        - At this time the average Delivery Route (SPR) is 108.79, 16.21 less than the target
    """)


#Preparacion Data y gràficas
    #Filtro lateral
columnas = ('city','city_cluster','carrier','driver_experience','cycle_flag')
filtro = st.sidebar.radio('Choose column', columnas)
st.sidebar.write('You are seeing: ', filtro)

    #gráfica de distribución general
x =df['DS%']
hist_data = [x]
group_labels = ['distplot'] # name of the dataset
fig_displot_city = ff.create_distplot(hist_data, group_labels)

    #gráfica de distribución general
x_1 =df['shipments']
hist_data_1 = [x_1]
group_labels_1 = ['distplot'] # name of the dataset
fig_displot_ship = ff.create_distplot(hist_data_1, group_labels_1)

    #grafica de caja
fig_box_edo = px.box(df, x = filtro , y = 'DS%')
    #grafica de Barras Estado
df_fig1 = df.groupby(by=filtro).mean()
df_fig1 = df_fig1.sort_values(by='DS%', ascending = False)
df_fig1 = df_fig1.reset_index()
fig1 = px.bar(df_fig1, x=filtro, y='DS%')

st.header('Análysis')
st.subheader('General Analysis')
tab1, tab2 = st.tabs(['Delivery Success','Shimpents'])

with tab1:
    st.caption('Distribution plot DS')
    st.write(fig_displot_city)
    with st.expander("Resuls"):
        st.write("""
            - The distribution in general looks correct \n
            - 3 outliers can be seen with the following values; 0, 15.2 and 19.48
        """)


with tab2:
    st.caption('Shipments Distribution')
    st.write(fig_displot_ship)
    with st.expander("Results"):
        st.write("""
            - The distribution in general looks correct
        """)

st.subheader('Delivery Success Analysis')
st.write('You are seeing ', filtro)
df_ciudad = df.groupby(by=[filtro]).mean()

tab1, tab2, tab3, tab4= st.tabs(['General info',"Box Plot", "Bar Graph", 'Variable Correlation'])

with tab1:
   st.caption('General info')
   st.dataframe(df_ciudad)
   with st.expander("Results"):
    st.write("""
        - Only the city of Saltillo achieves the Delivery Success goal, Jalapa almost did it \n
         - No city achieves an average in expected shipments \n
             - The closest is CDMX 6 shipments below the target
             - The city with the lowest average shipments is Puebla with 61 shipments on average
         - The only carrier that achieves the objective is Envios Express, SSJ Serv Logistica, it is very close
         - If we analyze by cycle_flag, the SP group achieves the DS objective but very far from SPR
         - The cycle_flag that is closest to SOR is C1, the one that is furthest away is SD
         - If we analyze by experience, the Experienced category has the best index in DS and SPR

    """)

with tab2:
   st.caption('Plot Box')
   st.write(fig_box_edo)
   with st.expander("Results"):
    st.write("""
         - The Box and Whiskers graph helps to observe the distribution and other data, in this case by city, this makes it easier to identify probable outliers and to be able to find an answer much easier
         - Outliers are caused by 2 cities; Guadalajara (3) and Monterrey (0)\n
         - Some cities like CDMX and Queretaro also show outliers, but not as many as Guadalajara and Monterrey
         - In analysis by carrier we can find that the outliers found in the general graph are caused by the Interexpress
         - In general the distribution by carrier looks good
         - If we analyze by driver_experience we see that most of the outliers are caused by the Rookie category
         - Analyzing by cycle_flag, category C1 is the one with the greatest number of outliers, but Not planned has the largest body of the box
    """)

with tab3:
    st.caption('Bar Plot')
    st.write(fig1)
    with st.expander("Results"):
     st.write("""
        - Only the city of Saltillo achieves the goal
    """)

with tab4:
    st.caption('Variable correlation')
    st.write('The closer to 1 the correlation is direct, while the closer to -1 the correlation is inverse.')
    st.dataframe(df.corr(method='pearson'))

    with st.expander("Results"):
     st.write("""
        No variable shows any direct correlation with DS, so it can be deduced that modifying these variables would not have a great impact on our objective.
    """)
     


st.write('Next step for DS analysis')

with st.expander("Results"):
     st.write("""
       - According to the graph of boxes by city, the values of cities with SD less than 92 will be taken, where the largest number of atypicals are found, discarding Guadalajara and Merida \n
       - According to the chart of boxes by carrier, the values of carriers with values less than 88 will be taken, where the greatest number of outliers are found. \n
    """)


#Datos importantes
st.subheader('SPR Indicators')
st.markdown('The SPR (Shipments per Route) is the total number of packages with which a route left and are found in the shipments column')

spr = df[['route','deliveries']]
spr_mean = spr.groupby('route').mean().sort_values(by = 'deliveries')
kpi_spr_min = spr_mean.min()
kpi_spr_max = spr_mean.max()
kpi_spr_mean = spr_mean.mean()

col1, col2, col3, col4 = st.columns(4)


with col1:
    st.metric(label="SPR MIN ", value = kpi_spr_min)
with col2:
     st.metric(label='SPR MAX', value = kpi_spr_max)
with col3:
    st.metric(label='SPR AVG', value = kpi_spr_mean.round(2))
with col4:
    st.metric(label="Total Rutas", value = df[['route']].count())


    #grafica de caja
fig_box_ship = px.box(df, x = filtro , y = 'shipments')
    #grafica de Barras Estado
df_fig1_shipments = df.groupby(by=filtro).mean()
df_fig1_shipments= df_fig1_shipments.sort_values(by='shipments', ascending = False)
df_fig1_shipments = df_fig1_shipments.reset_index()
fig1_shipments = px.bar(df_fig1_shipments, x=filtro, y='shipments')


st.subheader('SPR analysis')
st.write('Your are seeing: ', filtro)
df_ciudad = df.groupby(by=[filtro]).mean()

tab1, tab2, tab3, tab4= st.tabs(['DGeneral Info',"Box Plot", "Bar Plot", 'Variable Correlation'])

with tab1:
   st.caption('General Info')
   st.dataframe(df_ciudad)


with tab2:
   st.caption('Box Plot')
   st.write(fig_box_ship)

with tab3:
    st.caption('Bar Graph')
    st.write(fig1_shipments)


with tab4:
    st.caption('Variable Correlation')
    st.write('The closer to 1 the correlation is direct, while the closer to -1 the correlation is inverse.')
    st.dataframe(df.corr(method='pearson'))







