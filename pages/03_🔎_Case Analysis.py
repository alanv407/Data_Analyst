#Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff

#Functions

    #Normal distribution
def GeneralDistribution(x_GeneralDistribution, GL_GeneralDistribution):
    x = df[x_GeneralDistribution]
    HistData = [x]
    GroupLables = [GL_GeneralDistribution]
    return ff.create_distplot(HistData,GroupLables)

    #Box Plot
def BoxPlot(df_BoxPlot, y_BoxPlot):
    return px.box(df_BoxPlot, x = filter, y = y_BoxPlot)

    #Bar Graph
def BarGraph(df_BarGraph, by_BarGraph):
    df_fig1 = df_BarGraph.groupby(by=filter).mean() \
    .sort_values(by= by_BarGraph, ascending = False) \
    .reset_index()
    return px.bar(df_fig1, x=filter, y=by_BarGraph)

def KPIS(groupby_KPIS, by_KPIS):
    df_KPIS = df[[groupby_KPIS, by_KPIS]].groupby(groupby_KPIS)\
    .mean() \
    .sort_values(by = by_KPIS) 
    return df_KPIS

def KPI(ColA, ColB):
    return ((df[ColA] / df[ColB]) * 100).round(1)

#Page Setup
st.set_page_config(
	page_title = 'Supply Chain',
	page_icon = '🛒',
	)

st.title('📈📊 Supply Chain Cases Analysis 📈📊')

st.subheader('The objectives of develop the project coding in Python are as follows:')

with st.expander("Know a little more"):
    st.write("""
        - Being able to perform the exercise several times with updated data and in an automated way.
        - In case of exceeding more than ±1,040,000 rows, we could not perform the exercise in Excel.
        - Have a place where the information and visualizations can be manipulated, with automatic updates.
    """)

#Data Input
	#Save file in cache
data = st.file_uploader('Drag and drop a file to continue')
if not data:
     st.warning('You can find the Excel file in: https://github.com/alanv407/Data_Analyst/blob/main/data.xlsx')
     st.stop()

@st.cache(allow_output_mutation=True)
def load_model(model_name):
     df=pd.read_excel(data, dtype={'route': str})
     return(df)
df=load_model(data)

df['DeliverySuccess'] = ((df['deliveries']/df['shipments'])*100).round(2)

#Filter
columns = ('city','city_cluster','carrier','driver_experience','cycle_flag')
filter = st.sidebar.radio('Choose column', columns)
st.sidebar.write('You are seeing: ', filter)

#DATA
st.header('What we have here?')
st.subheader('DataFrame')
st.caption('Only the first 50 rows are displayed')
st.dataframe(df.head(50))
with st.expander("Results"):
    st.write(f"""
        The information contained in the file:
         - Dates, routes, cities, etc.
         - Dataframe dimension: {df.shape} (Rows, Columns).
         - Delivery Success calculation has been added.
    """)

st.header('We are asked to consider how to reach the following goals')
with st.expander("Goals"):
    st.write(f"""
        - Achieve 99.5% Delivery Success (DS)
        - Achieve 125 Shipments per Route (SPR)
    """)

#General Information
st.header('Currently')
st.write('Indicators')
col1, col2= st.columns(2)

with col1:
    st.metric(label="AVG Shipments per Route ", value = KPIS('route','deliveries').mean().round(1))
with col2:
     st.metric(label='AVG Delivery Success', value = KPI('deliveries','shipments').mean().round(1))
st.caption('Descriptive statistics information')
st.dataframe(df.describe().transpose())
with st.expander("Results"):
    st.write(f"""
        - Delivery Success average is {KPI('deliveries','shipments').mean().round(1)}%, {99.5-(KPI('deliveries','shipments').mean()):.1f}% below target.
        - Shipments per Routes average is {float(KPIS('route','deliveries').mean().round(1))}, {125-(float(float(KPIS('route','deliveries').mean().round(1)))):.1f} below target. 
             """)

st.header('Analysis')
st.subheader('Normal distribution')
tab1, tab2 = st.tabs(['Delivery Success','Shimpents'])

with tab1:
    st.write(GeneralDistribution('DeliverySuccess','distplot'))
    with st.expander("Results"):
        st.write("""
            - The distribution in general looks correct \n
            - 3 outliers can be seen with the following values; 0, 15.2 and 19.48
        """)

with tab2:
    st.write(GeneralDistribution('shipments','distplot'))
    with st.expander("Results"):
        st.write("""
            - The distribution in general looks correct
        """)

st.subheader('Delivery Success Analysis')
st.write('You are seeing ', filter)

tab1, tab2, tab3, tab4= st.tabs(['General info',"Box Plot", "Bar Graph", 'Variable Correlation'])

with tab1:
   st.caption('General info')
   st.dataframe(df.groupby(by = [filter]).mean())
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
   st.write(BoxPlot(df,'DeliverySuccess'))
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
    st.write(BarGraph(df,'DeliverySuccess'))
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
        No variable shows any direct correlation with Delivery Success, so it can be deduced that modifying these variables would not have a great impact on our objective.
    """)

st.subheader('Next step for DS analysis')

with st.expander("Results"):
     st.write("""
       - No variable shows any correlation with Delivery Success, so it is assumed that success is an external factor to this information.
       - According to the graph of boxes by city, the values of cities with SD less than 92 will be taken, where the largest number of atypicals are found, discarding Guadalajara and Merida \n
       - According to the chart of boxes by carrier, the values of carriers with values less than 88 will be taken, where the greatest number of outliers are found. \n
    """)

#Datos importantes
st.subheader('SPR Indicators')
st.markdown('The SPR (Shipments per Route) is the total number of packages with which a route left and are found in the shipments column')

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="SPR MIN ", value = KPIS('route','deliveries').min().round(1))
with col2:
     st.metric(label='SPR MAX', value = KPIS('route','deliveries').max().round(1))
with col3:
    st.metric(label='SPR AVG', value = KPIS('route','deliveries').mean().round(2))
with col4:
    st.metric(label="Total Rutas", value = df[['route']].count())

st.subheader('SPR analysis')
st.write('Your are seeing: ', filter)
df_ciudad = df.groupby(by=[filter]).mean()

tab1, tab2, tab3, tab4= st.tabs(['General Information',"Box Plot", "Bar Plot", 'Variable Correlation'])

with tab1:
   st.caption('General Info')
   st.dataframe(df_ciudad)

with tab2:
   st.caption('Box Plot')
   st.write(BoxPlot(df, 'shipments'))

with tab3:
    st.caption('Bar Graph')
    st.write(BarGraph(df, 'shipments'))


with tab4:
    st.caption('Variable Correlation')
    st.write('The closer to 1 the correlation is direct, while the closer to -1 the correlation is inverse.')
    st.dataframe(df.corr(method='pearson'))

with st.expander("Results"):
     st.write("""
       - No variable shows any correlation with Delivery Success, so it is assumed that success is an external factor to this information.
       - Being a rookie if it impacts shipments by route.
       - There are cities with a low Shipment AVG
       """)


