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
    return ((df[ColA] / df[ColB]) * 100).mean().round(1)

def color_delivery_success(val):
  color = '#5DE23C' if val >= 99.5 else '#e94f58'
  return f'background-color: {color}'

def color_shipments_route(val):
  color = '#5DE23C' if val >= 125 else '#e94f58'
  return f'background-color: {color}'

#Page Setup
st.set_page_config(
	page_title = 'Supply Chain',
	page_icon = '🔎',
	)

st.title('📊 Supply Chain Case Analysis 📈')

st.divider()

st.subheader('Description')
st.markdown('**This Python project aims to achieve the following objectives:**')

with st.expander("Click"):
    st.write("""
        - **Enable iterative execution with dynamic data updates and automation:** This objective emphasizes the project's ability to handle repeated analysis with fresh data sets in an automated fashion.
        - **Overcome data volume limitations:** This replaces the Excel limitation by highlighting the project's ability to handle large datasets (exceeding 1,040,000 rows).
        - **Facilitate interactive data manipulation and visualization:** This rephrases the point about manipulating information and visualizations by emphasizing an interactive environment for analysis.
    """)

st.divider()
with st.container(border=True):
    st.markdown('This app requires a file to function properly. You can download the necessary file here from GitHub:')

    st.link_button("Go to the file", "https://github.com/alanv407/Data_Analyst/blob/main/data.xlsx")
    #Data Input
        #Save file in cache
    data = st.file_uploader('Drag and drop a file to continue')
    if not data:
        st.info('Drag and drop a file to generate the analysis', icon="ℹ️")
        st.stop()

    @st.cache_data()
    def load_model(model_name):
        df=pd.read_excel(data, dtype={'route': str})
        return(df)
    df=load_model(data)

    st.success('Data upload successful.', icon="✅")

st.divider()

########################################################
######################################################## DATA PROCESSING


df['DeliverySuccess'] = ((df['deliveries']/df['shipments'])*100).round(2)

#FILTER
columns = ('city','city_cluster','carrier','driver_experience','cycle_flag')
filter = st.sidebar.radio('Choose column', columns)
st.sidebar.write(f'You are seeing: **{filter}**')


#DATA
st.header("Let's take a closer look at the file.")
st.caption("For your initial review, here are the first 50 records from the file.")
st.dataframe(df.head(50))
with st.expander("Findings"):
    st.write(f"""
        The information contained in the file:
         - Dates, routes, cities, etc.
         - The file contains {len(df)} rows and {df.shape[1]} Columns.
         - Delivery Success calculation has been added.
    """)

st.divider()

st.subheader("Our task is to determine the best approach to achieve the following goals:")
with st.expander("Goals"):
    st.markdown(f"""
        - Achieve **99.5%** Delivery Success (DS)
        - Achieve **125** Shipments per Route (SPR)
    """)

#General Information
st.subheader('Current Metrics')

col1, col2= st.columns(2)

with col1:
    st.metric(label="AVG Shipments per Route ", 
              value = KPIS('route','deliveries').mean().round(1),
              delta= f"{125-(float(float(KPIS('route','deliveries').mean().round(1)))):.1f} to goal",
              delta_color="inverse")
with col2:
     st.metric(label='AVG Delivery Success', 
               value = KPI('deliveries','shipments'),
               delta= f"{99.5-(KPI('deliveries','shipments').mean()):.1f}% to goal",
              delta_color="inverse")
          
st.markdown('Descriptive statistics information')


with st.expander("Findings"):
    st.write(f"""
        - Delivery Success average is {KPI('deliveries','shipments').mean().round(1)}%, {99.5-(KPI('deliveries','shipments').mean()):.1f}% below target.
        - Shipments per Routes average is {float(KPIS('route','deliveries').mean().round(1))}, {125-(float(float(KPIS('route','deliveries').mean().round(1)))):.1f} below target. 
             """)

st.divider()

st.header('General Analysis')
st.subheader('Normal distribution')
tab1, tab2 = st.tabs(['Delivery Success','Shimpents'])

with tab1:
    st.write(GeneralDistribution('DeliverySuccess','distplot'))
    with st.expander("Findings"):
        st.write("""
            - A correct normal distribution can be observed. \n
            - 3 outliers can be seen with the following values; 0, 15.2 and 19.48
        """)

with tab2:
    st.write(GeneralDistribution('shipments','distplot'))
    with st.expander("Findings"):
        st.write("""
            - The distribution in general looks correct
        """)
st.divider()

st.subheader('Delivery Success Analysis')


col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="DS MIN ", value = KPIS('deliveries','shipments').min().round(1))
with col2:
     st.metric(label='DS MAX', value = KPIS('deliveries','shipments').max().round(1))
with col3:
    st.metric(label='DS AVG', value = KPI('deliveries','shipments').mean().round(2))
with col4:
    st.metric(label="Total Records", value = df[['route']].count())

st.write(f'You are seeing: **{filter}**')

tab1, tab2, tab3, tab4= st.tabs(['General info',"Box Plot", "Bar Graph", 'Variable Correlation'])

df_styled = df.groupby(by=[filter])['DeliverySuccess'].mean().reset_index().style.applymap(color_delivery_success, subset=['Delivery Success'])

df_to_display = df_styled.data

df_to_display = df_to_display[[filter, 'DeliverySuccess']]

with tab1:
   st.caption('General info')
   st.dataframe(df_to_display.sort_values(by = 'DeliverySuccess', ascending=False).style.applymap(color_delivery_success, subset=['DeliverySuccess']))

with tab2:
   st.caption('Plot Box')
   st.write(BoxPlot(df,'DeliverySuccess'))

with tab3:
    st.caption('Bar Plot')
    st.write(BarGraph(df,'DeliverySuccess'))

with tab4:
    st.caption('Variable correlation')
    st.write('The closer to 1 the correlation is direct, while the closer to -1 the correlation is inverse.')
    st.dataframe(df.corr(method='pearson'))

    with st.expander("Findings"):
     st.write("""
        No variable shows any direct correlation with Delivery Success, so it can be deduced that modifying these variables would not have a great impact on our objective.
    	""")

st.subheader('Next step for DS analysis')

with st.expander("Findings"):
    st.write("""
        - Only the city of Saltillo achieves the Delivery Success goal, Jalapa almost did it.
        - The only carrier that achieves the objective is Envios Express, SSJ Serv Logistica, it is very close.
        - It is proposed to review and validate the Cycle_flag data since outside of SP all have poor performance.
	- No variable shows any correlation with Delivery Success, so it is assumed that success is an external factor to this information.
       	- According to the graph of boxes by city, the values of cities with SD less than 92 will be taken, where the largest number of atypicals are found, discarding Guadalajara and Merida.
	- According to the chart of boxes by carrier, the values of carriers with values less than 88 will be taken, where the greatest number of outliers are found.
	- Experience is not a relevant variable.
 	- No city reaches the average in expected shipments.
             - The closest is CDMX, 6 shipments below the target.
             - The city with the lowest average shipments is Puebla with 61 shipments on average.
    	""")

      
st.divider()

st.subheader('SPR Indicators')
st.markdown('The SPR (Shipments per Route) is the total number of packages with which a route left and are found in the "shipments" column')

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="SPR MIN ", value = KPIS('route','deliveries').min().round(1))
with col2:
     st.metric(label='SPR MAX', value = KPIS('route','deliveries').max().round(1))
with col3:
    st.metric(label='SPR AVG', value = KPIS('route','deliveries').mean().round(2))
with col4:
    st.metric(label="Total Records", value = df[['route']].count())

st.subheader('SPR analysis')
st.write(f'Your are seeing: **{filter}**')

df_styled_shipments = df.groupby(by=[filter])['shipments'].mean().reset_index().style.applymap(color_shipments_route, subset=['shipments'])
df_to_display_shipments = df_styled_shipments.data
df_to_display_shipments = df_to_display_shipments[[filter, 'shipments']]

tab1, tab2, tab3, tab4= st.tabs(['General Information',"Box Plot", "Bar Plot", 'Variable Correlation'])

with tab1:
   st.caption('General Info')
   st.dataframe(df_to_display_shipments.sort_values(by = 'shipments', ascending=False).round(2).style.applymap(color_shipments_route, subset=['shipments']))

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

with st.expander("Findings"):
     st.write("""
       - No variable shows any correlation with SPR, so it is assumed that success is an external factor to this information.
       - No city or city_cluster have the expected performance, the city with the worst performance is Puebla.
       - Only one carrier have the expected avg performance.
       - Being a novice does affect route shipments.
       - It is proposed to review and validate the Cycle_flag data since outside of C1 all have poor performance.
       - There are cities with a low Shipment AVG
       """)



