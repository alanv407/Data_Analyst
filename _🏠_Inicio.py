#Librerias
import streamlit as st
import pandas as pd
import plotly.express as px

#Configurarción Páginas
st.set_page_config(
	page_title = 'Análisis de Caso',
	page_icon = '🛒',
	)
st.title('Inicio')

st.header('Take Home Exercise.')
st.subheader('Sobre el Panel y Presentación del Caso')
st.markdown('Para la presentación al panel se ha desarrollado esta Web App con la que se ha realizado el Análisis del Caso enviado.')
st.markdown('Para el desarrollo de esta Web App se usó el lenguaje de programación Python, se usaron las siguientes librerías; Pandas, Plotly y Streamlit')

st.subheader('Uso de la Web App')
st.markdown('Del lado izquierdo se encuentran las diferentes partes de esta presentación; Inicio, Sobre mi y Análisis Caso, en su caso tambien se encontrarán algunos filtros, en la parte inferior se encuentra el código usado para esta Web App')

st.subheader('Más información')
st.caption('En algunos casos encontraras algun recuadro como el que se muestra abajo, dando clic podrás ver más información')
with st.expander("Saber un poco más"):
    st.write("""
        Este es un ejemplo 
    """)

st.subheader('Pestañas')
st.caption('En otros casos encontrarás Pestañas, para ver la información de cada una solo tienes que hacer clic en cada una ')
tab1, tab2 = st.tabs(['Pestaña 1','Pestaña 2'])

with tab1:
   st.caption('Pestaña 1')
   st.write("""
        Información en Pestaña 1
    """)

with tab2:
   st.caption('Pestaña 2')
   st.write("""
        Información en Pestaña 2
       """)
st.title('¡Comenzemos!')


st.header('Código Inicio')
st.code("""
        #Librerias
import streamlit as st
import pandas as pd
import plotly.express as px

#Configurarción Páginas
st.set_page_config(
	page_title = 'Caso Mercado Libre',
	page_icon = '🛒',
	)
st.title('Inicio')

st.header('Take Home Exercise.')
st.subheader('Sobre el Panel y Presentación del Caso')
st.markdown('Para la presentación al panel se ha desarrollado esta Web App con la que se ha realizado el Análisis del Caso enviado.')
st.markdown('Para el desarrollo de esta Web App se usó el lenguaje de programación Python, se usaron las siguientes librerías; Pandas, Plotly y Streamlit')

st.subheader('Uso de la Web App')
st.markdown('Del lado izquierdo se encuentran las diferentes partes de esta presentación; Inicio, Sobre mi y Análisis Caso, en su caso tambien se encontrarán algunos filtros, en la parte inferior se encuentra el código usado para esta Web App')

st.subheader('Más información')
st.caption('En algunos casos encontraras algun recuadro como el que se muestra abajo, dando clic podrás ver más información')
with st.expander("Saber un poco más"):
    st.write("
        Este es un ejemplo 
    ")

st.subheader('Pestañas')
st.caption('En otros casos encontrarás Pestañas, para ver la información de cada una solo tienes que hacer clic en cada una ')
tab1, tab2 = st.tabs(['Pestaña 1','Pestaña 2'])

with tab1:
   st.caption('Pestaña 1')
   st.write(
        Información en Pestaña 1
    ")

with tab2:
   st.caption('Pestaña 2')
   st.write(''
        Información en Pestaña 2
       '')
st.title('¡Comenzemos!')
""" ,language="python")

st.header('Código Sobre Mi')
st.code(""" 

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
    st.write("
        Soy el tipo de persona que no le teme a los desafíos, me gusta aportar innovación y motivación al equipo de trabajo. \n 
        Me describo como una persona dinámica, analítica, con gran facilidad para aprender y orientado a resultados. \n
    ")


st.header('Experiencia Profesional')

with st.expander("Saber un poco más"):
    st.write("
        Cuento con experiencia en manipulación e interpretación de datos. \n 
        Las herramientas que más uso son; SQL, Power BI, Python y Excel.
    ")

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
	st.markdown('EAE BUSINESS SCHOOL / UNIVERSITAT POLITÉCNICA DE CATALUNYA')
	st.caption('2017 - 2018')

with tab6:
	st.subheader('Química')
	st.markdown('Universidad La Salle')
	st.caption('2012 - 2016')

with tab7:
	st.subheader('Big Data')
	st.markdown('Fundación Carlos Slim / SEP')
	st.caption('527 horas / 2021')

""" ,language="python"	)

st.header('Análisis Caso')
st.code("""

#Librerias
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff

#Configurarción Páginas
st.set_page_config(
  page_title = 'Caso Mercado Libre',
  page_icon = '🛒',
  )

st.title('📈📊 Análisis Caso MeLi 📈📊')

st.subheader('El objetivo de realizar el proyecto usando esta herramienta son los siguientes: ')


with st.expander("Saber un poco más"):
    st.write("
        - Poder realizar el ejercicio varias veces con data actualizada  y de forma automatizada\n 
        - El obtener datos estadísticos es mucho más fácil y rápido que en un Excel \n
        - En caso de superar más de un ±1,040,000 filas no podríamos realizar el ejercicio en Excel \n 
        - No tengo Excel ni Power BI en mi computadora 
    ")

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
st.header('Analicemos que es lo que tenemos')
st.subheader('DataFrame')
st.caption('Unicamente se muestran las primeras 100 filas')
st.dataframe(df.head(100))
st.write('Las dimensiones del Dataframe son las siguientes (Filas, Columnas): ',df.shape)
with st.expander("Resultado del análisis"):
    st.write("
        Vemos la información contenida en el Excel: \n
        - Fechas, tiempos, rutas, ciudades, etc. \n
        - Dimensión del Dataframe
        - Se agrego el cálculo de Delivery Success
    ")


st.header('Se nos pide plantear como llegar a los siguientes objetivo: \n - Lograr un 99.5% de Delivery Success \n - Lograr 125 shipments per Route')

#Preparación datos

st.subheader('Estado Actual')
tab1, tab2 = st.tabs(['Datos Generales','Datos Generales 2'])

with tab1:
   st.caption('Información de estadística descriptiva')
   st.dataframe(df.describe(include='all' ).transpose())
   st.write('Las dimensiones del DataFrame son las siguientes (filas, columnas): ', df.shape)
   with st.expander("Resultado del análisis"):
    st.write("
        - Datos únicos como: \n
            -Fechas: 111  \n
            -Rutas: 13,365  \n
            -Ciudades: 17 \n
            -City_cluster:58 \n
            -Carrier: 25
        - Rango de las fechas: del 06-04-222 a 25-07-2022 
    ")

with tab2:
   st.caption('Información de estadística descriptiva')
   st.dataframe(df.describe().transpose())
   with st.expander("Resultado del análisis"):
    st.write("
        - El promedio de DS es 98.19, 1.31% por debajo del objetivo \n
        - En este momento el promedio de Entregas por Ruta (SPR) son 108.79, 16.21 menos del objetivo
    ")


#Preparacion Data y gràficas
    #Filtro lateral
columnas = ('city','city_cluster','carrier','driver_experience','cycle_flag')
filtro = st.sidebar.radio('Escoge la columna a analizar', columnas)
st.sidebar.write('Estas viendo: ', filtro)

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

st.header('Análisis')
st.subheader('Análisis General')
tab1, tab2 = st.tabs(['Delivery Success','Shimpents'])

with tab1:
    st.caption('Gráfica de distribución DS')
    st.write(fig_displot_city)
    with st.expander("Resultado del análisis"):
        st.write("
            - La distribución en lo general se ve correcta \n
            - Se pueden ver 3 valores atípicos con los siguientes valores; 0, 15.2 y 19.48
        ")


with tab2:
    st.caption('Gráfica de distribución Shipments')
    st.write(fig_displot_ship)
    with st.expander("Resultado del análisis"):
        st.write("
            - Se observa una distribución normal
        ")

st.subheader('Análisis Delivery Success')
st.write('Estas viendo: ', filtro)
df_ciudad = df.groupby(by=[filtro]).mean()

tab1, tab2, tab3, tab4= st.tabs(['Datos generales',"Gráfica Caja", "Gráfica Barras", 'Correlación de Variables'])

with tab1:
   st.caption('Datos Generales')
   st.dataframe(df_ciudad)
   with st.expander("Resultado del análisis"):
    st.write("
        - Solo la ciudad de Saltillo logra el objetivo de Delivery Success, Jalapa casi lo logra \n
        - Ninguna ciudad logra un promedio en shipments esperado  \n
            - El más cercano es CDMX 6 shipments por debajo del objetivo
            - La ciudad con promedio más bajo en shipments es Puebla con 61 shipments en promedio
        - El único carrier que logra el objetivo es Envios Express, SSJ Serv Logistica, se enceuntra muy cerca
        - Si analizamos por cycle_flag, el grupo SP logra el obejtivo DS pero muy alejado de SPR
        - El cycle_flag que mas se acerca a SOR es C1, el que mas se aleja es SD
        - Si analizamos por experiencia, la categoría Experienced tiene el mejor indice en DS y SPR

    ")

with tab2:
   st.caption('Gráfica de Cajas')
   st.write(fig_box_edo)
   with st.expander("Resultado del análisis"):
    st.write("
        - La gráfica de Caja y Bigotes ayuda a observar la distribución y otros datos, en este caso por ciudad, esto facilita identificar probables datos atìpicos y poder buscar una respuesta mucho más fácil
        - Los atípicos son causados por 2 ciudades; Guadalajara (3) y Monterrey (0) \n
        - Algunas ciudades como CDMX y Queretaro muestran tambien atípicos, pero no tantos como Guadalajara y Monterrey
        - En análsis por carrier podemos encontrar que los atípicos encontrados en la gráfica general son causados por el Interexpress
        - En general la distribución por carrier se ve bien
        - Si analizamos por driver_experience vemos que la mayoria de los atípicos son causados por la categoría Rookie
        - Analizando por cycle_flag la categoria C1 es la que cuenta con mayor cantidad de atípicos pero Not planned tiene el mayor cuerpo de la caja
    ")

with tab3:
    st.caption('Gráfica de Barras')
    st.write(fig1)
    with st.expander("Resultado del análisis"):
     st.write("
        - Solo la ciudad de Saltillo logra el objetivo
    ")

with tab4:
    st.caption('Correlación de variables')
    st.write('Entre más cerca a 1 la correlación es directa, en cambio, entre más cerca a -1 la correlación es inversa')
    st.dataframe(df.corr(method='pearson'))

    with st.expander("Resultado del análisis"):
     st.write("
        Ninguna variable muestra alguna correlación directa con DS, por lo que se puede deducir que modificar estas variables no representaría un gran impacto en nuestro objetivo
    ")
     


st.write('Siguiente paso para el análisis DS')

with st.expander("Resultado del análisis"):
     st.write("
        - De acuerdo al gráfico de cajas por ciduad, se tomarán los valores de ciduades con DS menor a 92, donde se encuentra la mayor cantidad de atípicos descartando Guadalajara y Merida \n
        - De acuerdo al gráfico de cajas por carrier, se tomáran los valores de carriers con valores menores a 88, donde se encuentran la mayor cantidad de atípicos. \n 
    ")


#Datos importantes
st.subheader('Indicadores SPR')
st.markdown('El SPR (Shipments per Route) es la cantidad total de paquetes con los que salió una ruta y se encuentran en la columna de shipments')

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


st.subheader('Análisis SPR')
st.write('Estas viendo: ', filtro)
df_ciudad = df.groupby(by=[filtro]).mean()

tab1, tab2, tab3, tab4= st.tabs(['Datos generales',"Gráfica Caja", "Gráfica Barras", 'Correlación de Variables'])

with tab1:
   st.caption('Datos Generales')
   st.dataframe(df_ciudad)


with tab2:
   st.caption('Gráfica de Cajas')
   st.write(fig_box_ship)

with tab3:
    st.caption('Gráfica de Barras')
    st.write(fig1_shipments)


with tab4:
    st.caption('Correlación de variables')
    st.write('Entre más cerca a 1 la correlación es directa, en cambio, entre más cerca a -1 la correlación es inversa')
    st.dataframe(df.corr(method='pearson'))


	""" ,language="python")





