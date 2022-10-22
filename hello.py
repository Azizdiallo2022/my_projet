from __future__ import annotations
#from st_aggrid import AgGrid, GridOptionsBuilder
import streamlit as st
import time
import pandas as pd
import numpy as np
import seaborn as sns
#from st_aggrid.shared import GridUpdateMode
import base64  #to open .gif files in streamlit app
from pandas.api.types import is_numeric_dtype
from streamlit_option_menu import option_menu
import plotly.express as px
import json
import requests  # pip install requests
import streamlit as st  # pip install streamlit
from streamlit_lottie import st_lottie  # pip install streamlit-lottie
import matplotlib.pyplot as plt
import os
import altair as alt
from PIL import Image
import emoji
from matplotlib.figure import Figure
from datetime import datetime
from datetimerange import DateTimeRange
import plotly.io as pio
import plotly.graph_objects as go
import math
from ctypes import sizeof
from genericpath import exists
from pickle import TRUE
#from turtle import color, fillcolor
from streamlit_plotly_events import plotly_events
import _tkinter as TK

linkedinlink = '[Github](https://github.com/Azizdiallo2022)'
covidlink='[Kaggle](https://www.kaggle.com/datasets/yamqwe/omicron-covid19-variant-daily-cases?select=covid-variants.csv)'
bubbleCovid = '[opendata.ecdc.europa.eu](https://opendata.ecdc.europa.eu/covid19/casedistribution/csv)'
GDPCovid = '[Kaggle](https://www.kaggle.com/code/thejeswar/gdp-population-analysis-of-the-world-countries/notebook)'

st.set_page_config(
    page_title="A Dashboard Template",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)


@st.cache()
def fake_data():
    """some fake data"""

    dt = pd.date_range("2021-01-01", "2021-03-01")
    df = pd.DataFrame(
        {"datetime": dt, "values": np.random.randint(0, 10, size=len(dt))}
    )

    return df

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
           
            footer {visibility: hidden;}
          
            </style>

"""
st.markdown(hide_st_style, unsafe_allow_html=True)


st.sidebar.image('covid_cell.jpeg')
st.sidebar.title("DATASET ON COVID-19")

@st.cache(suppress_st_warning=True)
def get_fvalue(val):
    feature_dict = {"No":1,"Yes":2}
    for key,value in feature_dict.items():
        if val == key:
            return value

def get_value(val,my_dict):
    for key,value in my_dict.items():
        if val == key:
            return value


    
#app_mode = st.sidebar.selectbox('Select Work',['HOME','',]) #tree pages

# 1. as sidebar menu
with st.sidebar:
    app_mode= option_menu("Main Menu", ['','Home','Data_Exploring','Data_Visualization','Contact'], 
        icons=["hou",'house','list-task',"list-task",'envelope'],menu_icon="cast", default_index=1)
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "green"},
    }    
    app_mode
    
if app_mode=='Home':
        
        def load_lottiefile(filepath: str):
            with open(filepath, "r") as f:
                return json.load(f)
        def load_lottieurl(url: str):
            r = requests.get(url)
            if r.status_code != 200:
                return None
            return r.json()
        
        lottie_coding = load_lottiefile("welcome.json")  # replace link to local lottie file
        lottie_hello = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_69HH48.json")

        st_lottie(
            lottie_hello,
            speed=1,
            reverse=False,
            loop=True,
            quality="low", # medium ; high
            #renderer="svg", # canvas
            height=None,
            width=None,
            key=None,
        )
        st.balloons()

        st.write(emoji.emojize("""# COVID-19 PandeMap """))
        st.write("""## How it works""")
        st.write("This tool will enable users to quickly visualize COVID-19 global evolution, "
        "track the development of the virus and its variants and measure the correlation "
        "between the development of a country and the number of COVID-19 cases.")
        st.write("##### For viewing the Sourcecode, click here:", linkedinlink)
        st.write("""## Navigating the app""")
        st.write("The app consists of 4 pages, including this introduction page. "
        " To navigate to the other pages, click on the options in the sidebar. "
        "Given below is a short description of what each page shows.")
        st.write("##### 1: Covid by Variants ")
        st.write("The first page is a view of the covid spread by variants. We can "
        "compare covid spreads in different locations at different times at the "
        "variant level of granularity ")
        st.write("##### 2: How Covid Spread")
        st.write("In the second page, we go deeper into understanding the spread of covid. "
        "We see the evolution of covid over time and also, make a comparison of regions by GDP "
        "and infant mortalities and covid cases to see if there is some trend that is observable. ")
        st.write("##### 3: Monthly covid evolution")
        st.write("Here, we have a monthly view of how covid spread by location "
        "and variants ")
        st.write("###### We have taken the covid data from", covidlink,"(1), ", GDPCovid, "(2) and ",bubbleCovid)

        
elif app_mode=='Data_Exploring':
        
        @st.cache()
        def fake_data():
            """some fake data"""

            dt = pd.date_range("2021-01-01", "2021-03-01")
            df = pd.DataFrame(
                {"datetime": dt, "values": np.random.randint(0, 10, size=len(dt))}
            )

            return df
    
        st.sidebar.header('All_Dataset')
        ds = st.sidebar.radio('',['Covid_by_Variants','Covid_in_a_Geographical_Context','Monthly_covid_evolution'])
        if ds == 'Covid_by_Variants':
              
            a=st.sidebar.slider('Enter a number of head', 5, 10)
            b=st.sidebar.slider('Enter a number of tail', 5, 10)

            st.title('Exploration of Dataset :')     
            with st.spinner('Wait for it...'):
                time.sleep(15)

            data = pd.read_csv("data.csv")
            data=data.drop(["Unnamed: 0"], axis=1)
            #AgGrid(data)
            st.markdown('Display the head of Dataset')
            st.write(data.head())
            st.markdown('Display the tail of Dataset')
            st.write(data.tail())


            app_mod = st.sidebar.selectbox('Statistic Describetive',['Shape of Dataset','Vue a Sample', 'Summe of Duplications','Type of Dataset','Nomber of Columns','Miss_value','Summary','Covariate','Correlation',])

            if app_mod=='Type of Dataset':
                     st.markdown('The Type of the Dataset')
                     st.write(type(data))

            elif app_mod=='Shape of Dataset':
                      st.markdown('The Shape of the Dataset')
                      st.write(data.shape)
            elif app_mod=='Vue a Sample':
                        st.markdown('Display the sample of Dataset')
                        c=st.sidebar.slider('Enter a number of sample', 1, 20)
                        st.write(data.sample(c))
  
            elif app_mod=='Summe of Duplications':
                      st.markdown('The Summe of all Duplication')
                      st.write(data.duplicated().sum())

            elif app_mod=='Nomber of Columns':
                      st.markdown('The Nomber of Columns')
                      st.write(data.columns)

            elif app_mod=='Miss_value':    
                      st.markdown('Display the Miss value in Dataset')
                      st.write(data.isna().sum())

            elif app_mod=='Summary': 
                      st.markdown('Display a Summary of Dataset')
                      st.write(data.describe())

            elif app_mod=='Covariate':
                      st.markdown('Summary for the covariate')
                      st.write(data.cov())

            elif app_mod=='Correlation':
                      st.markdown('Summary for the corelation')
                      st.write(data.corr())
                    
        elif ds == 'Covid_in_a_Geographical_Context':
          
           #a=st.sidebar.slider('Enter a number of head', 5, 10)
           #b=st.sidebar.slider('Enter a number of tail', 5, 10)

            st.title('Exploretion of Dataset :')     
            with st.spinner('Wait for it...'):
                time.sleep(10)

            data = pd.read_csv("data_gdp.csv")
            data=data.drop(["Unnamed: 0"], axis=1)
            data
            #AgGrid(data)
           #st.markdown('Display the head of Dataset')
          # st.write(data.head(a))
           #st.markdown('Display the tail of Dataset')
          # st.write(data.tail(b))


            app_mod = st.sidebar.selectbox('Statistic Describetive',['Shape of Dataset','Vue a Sample', 'Summe of Duplications','Type of Dataset','Nomber of Columns','Miss_value','Summary','Covariate','Correlation',])
        
        

            if app_mod=='Type of Dataset':
                     st.markdown('The Type of the Dataset')
                     st.write(type(data))

            elif app_mod=='Shape of Dataset':
                
                st.markdown('The Shape of the Dataset')
                st.write(data.shape)
            elif app_mod=='Vue a Sample':
                    st.markdown('Display the sample of Dataset')
                    c=st.sidebar.slider('Enter a number of sample', 1, 20)
                    st.write(data.sample(c))

            elif app_mod=='Summe of Duplications':
                      st.markdown('The Summe of all Duplication')
                      st.write(data.duplicated().sum())

            elif app_mod=='Nomber of Columns':
                      st.markdown('The Nomber of Columns')
                      st.write(data.columns)

            elif app_mod=='Miss_value':    
                    st.markdown('Display the Miss value in Dataset')
                      
                    st.write(data.isna().sum())

            elif app_mod=='Summary': 
                      st.markdown('Display a Summary of Dataset')
                      #data=data.drop(["Unnamed: 0"], axis=1)
                      st.write(data.describe())

            elif app_mod=='Covariate':
                      st.markdown('Summary for the covariate')
                      #data=data.drop(["Unnamed: 0"], axis=1)
                      st.write(data.cov())

            elif app_mod=='Correlation':
                      st.markdown('Summary for the corelation')
                      #data=data.drop(["Unnamed: 0"], axis=1)
                      st.write(data.corr())
                
        elif ds == 'Monthly_covid_evolution':
                
                a=st.sidebar.slider('Enter a number of head', 5, 10)
                b=st.sidebar.slider('Enter a number of tail', 5, 10)

                st.title('Exploretion of Dataset :')     
                with st.spinner('Wait for it...'):
                     time.sleep(10)

                data = pd.read_csv("cases_evolution.csv")
                data=data.drop(["Unnamed: 0"], axis=1)
                #AgGrid(data)
                st.markdown('Display the head of Dataset')
                st.write(data.head(a))
                st.markdown('Display the tail of Dataset')
                st.write(data.tail(b))


                app_mod = st.sidebar.selectbox('Statistic Describetive',['Shape of Dataset','Vue a Sample', 'Summe of Duplications','Type of Dataset','Nomber of Columns','Miss_value','Summary','Covariate','Correlation',])

                if app_mod=='Type of Dataset':
                     st.markdown('The Type of the Dataset')
                     st.write(type(data))

                elif app_mod=='Shape of Dataset':
                      st.markdown('The Shape of the Dataset')
                      st.write(data.shape)
                elif app_mod=='Vue a Sample':
                      st.markdown('Display the sample of Dataset')
                      c=st.sidebar.slider('Enter a number of sample', 1, 20)
                      st.write(data.sample(c))

                elif app_mod=='Summe of Duplications':
                      st.markdown('The Summe of all Duplication')
                      st.write(data.duplicated().sum())

                elif app_mod=='Nomber of Columns':
                      st.markdown('The Nomber of Columns')
                      st.write(data.columns)

                elif app_mod=='Miss_value':    
                      st.markdown('Display the Miss value in Dataset')
                      st.write(data.isna().sum())

                elif app_mod=='Summary': 
                      st.markdown('Display a Summary of Dataset')
                      st.write(data.describe())

                elif app_mod=='Covariate':
                      st.markdown('Summary for the covariate')
                      st.write(data.cov())

                elif app_mod=='Correlation':
                      st.markdown('Summary for the corelation')
                      st.write(data.corr())

elif app_mode=='Data_Visualization':
        #Bring in the data
      data = pd.read_csv('data.csv')
        #st.write("## THE DATA BEING USED")
      data=data.drop(["Unnamed: 0","Climate"], axis=1)

        #Transformation of Date column
      def date_change(date_str):
            format_str = '%Y-%m-%d' # The format
            datetime_obj = datetime.strptime(date_str, format_str)
            # print(datetime_obj.date())
            return datetime_obj.date()

      data["date"] = data["date"].apply(date_change)

      variants=data['variant_grouped'].unique()
      variants=variants[variants!='non-who']
      locations=data['Country'].unique()
      chosen_variants = data.groupby('variant_grouped')['num_sequences'].sum().sort_values(ascending=False)[:5]


        #Create and name sidebar
      st.sidebar.header('Filter the Graphs')
      g=st.sidebar.radio('',['Visual','Covid by Variants','Covid in a Geographical Context','Overall Development'])
      if g =='Visual':
          def load_lottiefile(filepath: str):
            with open(filepath, "r") as f:
                                return json.load(f)
          def load_lottieurl(url: str):
                r = requests.get(url)
                if r.status_code != 200:
                    return None
                return r.json()

          lottie_coding = load_lottiefile("dat.json")
          lottie_hello = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_qp1q7mct.json")

          st_lottie(
                lottie_hello,
                speed=1,
                reverse=False,
                loop=True,
                quality="low", # medium ; high
                #renderer="svg", # canvas
                height=None,
                width=None,
                key=None,
           )
      elif g =='Covid by Variants':
                  st.write(emoji.emojize("""# COVID-19 - A study by variants:"""))
        #st.write("""## How it works""")
                  st.write("This tool will enable users to quickly visualize COVID-19 global evolution, "
        "track the development of the virus and its variants and measure the correlation "
        "between the development of a country and the number of COVID-19 cases.")
            
                    #st.sidebar.write("""#### Choose your SG bias""")
                  variants=data['variant_grouped'].unique()
                  variants=variants[variants!='non-who']
                  locations=data['Country'].unique()
                  country_list = sorted(set(data["Continent"]))
                  country_list.insert(0,'All')
                  sorted(country_list)

                  def user_input_features():
                        time_1,time_2 = st.sidebar.date_input("Choose a Range in Time:", value = (data.date.min(),data.date.max()), min_value =data.date.min(), max_value=data.date.max())
                        variant_filter = st.sidebar.multiselect('Variant', variants,variants)
                        country_filter = st.sidebar.selectbox("Select a region:", country_list)
                        return time_1, time_2, variant_filter,country_filter

                  time_1, time_2, variant_filter, country_filter = user_input_features()

                  if st.sidebar.checkbox("Display all Data"):
                        data1=data
                        all_data_textbox = True
                  else:
                        all_data_textbox = False
                        if country_filter == 'All':
                            data1=data[(data.variant_grouped.isin(variant_filter)) & (time_1<=data.date) & (time_2>=data.date)]
                        else:
                            data1 = data[data.Continent == country_filter]
                            data1 = data1[(data1.variant_grouped.isin(variant_filter)) & (time_1<=data1.date) & (time_2>=data1.date)]
                  data1


                  st.write("## Chosen Filters: ")
                  if all_data_textbox == True:
                        st.write("All Data is chosen")
                  else:
                        st.write("Timeframe: " +str(time_1) + " to " + str(time_2))
                        str_val = ", ".join(variant_filter)
                        st.write("Chosen Variants: " + str(str_val))
                        st.write("Chosen country: " + str(country_filter))


                    #Output rankings based on users selections
                  st.write(
                        """
                        ## Overview of the Variants :chart_with_upwards_trend:
                        """
                  )

                  def block1(data):

                      def total_cases(data, click):
                        '''
                        Expects data.csv or its subsets as input
                        Returns the horizontal bar chart showing the total cases by variant
                        '''

                        #Data manipulation: simple sum of cases by variant
                        total_sum_variant = data[["variant_grouped", "num_sequences"]]
                        total_sum_variant.columns = ["Variant", "Total Cases"]

                        graph = alt.Chart(total_sum_variant).mark_bar(
                            opacity=0.7).properties(
                            title='Total Cases by Variant').encode(
                            x=alt.X('sum(Total Cases):Q',
                                title="Total Cases (log scale)",
                                scale=alt.Scale(type="log")),
                            y=alt.Y('Variant:N',
                                title=None),
                            color=alt.Color('Variant:N',
                                scale=alt.Scale(scheme='category20c')),
                            tooltip = [alt.Tooltip('Variant:N'),alt.Tooltip('sum(Total Cases):Q')],
                            opacity = alt.condition(click, alt.value(0.9), alt.value(0.1))).add_selection(
                            click
                        )

                        return graph

                      def cum_cases(data, click):
                        '''
                        Expects data.csv or its subsets as input
                        Returns the graph showing cumulative cases by variant over time
                        '''

                        # Data manipulation: cumulative counts of cases by date and variant
                        cumsum_variant = data.groupby(["variant_grouped", "date"])["num_sequences"].sum().groupby(level=0).cumsum().reset_index()
                        cumsum_variant.columns = ["Variant", "date", "Cumulative Cases"]

                        # Define interaction (needs to be global variable for cross-chart interaction)
                        # click = alt.selection_single(encodings=['color'], on="mouseover")

                        # Create plot
                        graph = alt.Chart(cumsum_variant).mark_area(
                            opacity=0.7,
                            interpolate='basis',
                            line=True).properties(
                            title='Cumulative Cases by Variant over time').encode(
                            x=alt.X("date:T",
                                title="Time Horizon",),
                            y=alt.Y("Cumulative Cases:Q"),
                            color=alt.Color('Variant:N',
                                scale=alt.Scale(scheme='category20c')),
                            tooltip = [alt.Tooltip('Variant:N'),alt.Tooltip('Cumulative Cases:Q')],
                            opacity = alt.condition(click, alt.value(0.9), alt.value(0.1))).add_selection(
                            click
                        )

                        return graph

                      def waves(data, click):
                        '''
                        Expects data.csv or its subsets as input
                        Returns the graph showing cumulative cases by variant over time
                        '''

                        # Data manipulation: cumulative counts of cases by date and variant
                        sum_variant = data.groupby(["variant_grouped", "date"])["num_sequences"].sum().reset_index()
                        sum_variant.columns = ["Variant", "date", "Cases"]

                        # Define interaction (needs to be global variable for cross-chart interaction)
                        # click = alt.selection_single(encodings=['color'], on="mouseover")

                        # Create plot
                        graph = alt.Chart(sum_variant).mark_area(
                          opacity=0.7,
                          interpolate='basis',
                          line=True).properties(
                          title='Cases by Variant over time').encode(
                          x=alt.X("date:T", title="Time Horizon",),
                          y=alt.Y("Cases:Q", stack=None),
                          color=alt.Color('Variant:N', scale=alt.Scale(scheme='category20c')),
                          tooltip = [alt.Tooltip('Variant:N'),alt.Tooltip('Cases:Q')],
                          opacity = alt.condition(click, alt.value(0.9), alt.value(0.1))).add_selection(
                          click
                        )

                        return graph

                      def cases_countries(data, click):
                        '''
                        Expects data.csv or its subsets as input
                        Returns the graph showing cumulative cases by variant over time
                        '''

                        # Data manipulation: cumulative counts of cases by date and variant
                        variantsum = data.groupby(["variant_grouped", "Country"])["num_sequences"].sum().reset_index()
                        variantsum.columns = ["Variant", "Country", "Total Cases"]

                        # Define interaction
                        #click = alt.selection_single(encodings=['color'], on="mouseover")
                        # Create plot

                        graph = alt.Chart(variantsum).mark_bar(
                          opacity=0.7,
                          interpolate='basis',
                          line=True).properties(
                          title='Cases by Variant').encode(
                          x=alt.X('Total Cases:Q', stack = 'normalize'),
                          y=alt.Y("Country:N", title=None),
                          color=alt.Color('Variant:N', scale=alt.Scale(scheme='category20c'),legend=alt.Legend(title="Variants")),
                          tooltip = [alt.Tooltip('Country:N'), alt.Tooltip('Variant:N'), alt.Tooltip('Total Cases:Q')],
                          opacity = alt.condition(click, alt.value(0.9), alt.value(0.1))
                        ).add_selection(
                          click
                        )#.properties(width=600)

                        return graph

                      click = alt.selection_single(encodings=['color'], on="mouseover", resolve="global")

                      return (total_cases(data,click) & (waves(data, click) & cum_cases(data, click)) | cases_countries(data, click))

                  st.altair_chart(block1(data1))


                    #################    

      elif g == 'Covid in a Geographical Context':
        
        st.write(emoji.emojize("""##  Dynamic World Map & GDP vs Infant Mortality Index """))

        st.write("""This section features the lates COVID-19 data from a global and economical perspective: the first visalisation will provide a
        overview of the evolution of Covid cases across the globe, while the second one will compare the GDP vs Infant Mortality index, an insightful index for the health status of a country, to the number of
        Covid cases in that country.""")

        # Importing first plot
        st.write("""#### World COVID-19 Cases - Evolution Over Time :earth_africa: """)

        #st.write("""##### The dataset used:""")
        df = pd.read_csv('cases_evolution.csv', index_col=0)
        #df
        st.write("###### Additional data for these insights was taken from", bubbleCovid, "and", GDPCovid )




        fig_1 = px.scatter_geo(
            df,
            locations='countryCode',
            color='continent',
            hover_name='country',
            projection='orthographic',
            size='cases',
            title=f'World COVID-19 Cases - Evolution Over Time',
            animation_frame="date"
        )

        st.plotly_chart(fig_1)


        st.write("""#### GDP :moneybag: vs Infant Mortality  :baby_bottle: & Total Cases""")

        #st.write("""##### The dataset used:""")
        ## Importing GDP vs Infant mortality dataframe
        data = pd.read_csv('data_gdp.csv', index_col=0)
        #data

        # Plot 2
        bubble_fig = px.scatter(data, x='Infant mortality (per 1000 births)',
                                        y='GDP ($ per capita)',
                                        color='Continent',
                                        size='Tot number of cases',
                                        log_x=True,
                                        hover_name="Country",
                                        hover_data=['GDP ($ per capita)', 'Infant mortality (per 1000 births)'],
                                        size_max=70)


        #bubble_fig.update_layout(hovermode='closest')
        st.plotly_chart(bubble_fig)
        # hovertemplaye=None
        # hovermode="x unified"

      elif g == 'Overall Development':
                        data = pd.read_csv('data.csv')
                        data=data.drop(["Unnamed: 0","Climate"], axis=1)
                        def date_change(date_str):
                                    format_str = '%Y-%m-%d' # The format
                                    datetime_obj = datetime.strptime(date_str, format_str)
                                    # print(datetime_obj.date())
                                    return datetime_obj.date()

                        data["date"] = data["date"].apply(date_change)

                        variants=data['variant_grouped'].unique()
                        variants=variants[variants!='non-who']
                        locations=data['Country'].unique()
                        chosen_variants = data.groupby('variant_grouped')['num_sequences'].sum().sort_values(ascending=False)[:5]


                        #Create and name sidebar
                        st.sidebar.header('Filter the Graphs')
                        #st.sidebar.write("""#### Choose your SG bias""")
                        variants=data['variant_grouped'].unique()
                        variants=variants[variants!='non-who']
                        locations=data['Country'].unique()
                        country_list = sorted(set(data["Continent"]))
                        country_list.insert(0,'All')
                        sorted(country_list)

                        def user_input_features():
                                    time_filter = st.sidebar.slider('Time', 2020, 2021, 2020, 1)
                                    variant_filter = st.sidebar.multiselect('Variant', variants,variants)
                                    country_filter = st.sidebar.selectbox("Select a region:", country_list)
                                    return time_filter, variant_filter,country_filter

                        time_filter, variant_filter, country_filter = user_input_features()
                        st.write(emoji.emojize("""#  COVID-19 Cases by month:"""))
                        st.write("This interactive plot gives an overview of the monthly trends in covid evolution. "
                        "The filters on the left give the option of choosing the year, region and variant we wish "
                        "to study. On choosing any of the filters, both the plots will adjust accordingly. ")

                        st.write("""### Click on any of the months on the first visualization to see the variant distribution """
                        "of the total cases in that month. """)
                        data['year']=pd.DatetimeIndex(data['date']).year
                        data['month']=pd.DatetimeIndex(data['date']).month
                        data['month']=pd.to_datetime(data['month'], format='%m').dt.month_name()
                        #data

                        #print(data)
                        if st.sidebar.checkbox("Display all Data"):
                            data1=data
                            all_data_textbox = True
                        else:
                            all_data_textbox = False
                            data=data[data.year==time_filter]
                            if country_filter == 'All':
                                data1=data[data.variant_grouped.isin(variant_filter)]
                            else:
                                data1 = data[data.Continent == country_filter]
                                data1 = data1[data1.variant_grouped.isin(variant_filter)]
                        #data1

                        sum_month = data1.groupby(["month"])["num_sequences"].sum().reset_index()

                        NEW=['January','February','March','April', 'May','June', 'July','August', 'September','October','November','December' ]

                        r_cord=[]

                        for i in NEW:
                            if i not in np.array(sum_month['month']):
                                r_cord.append(0)
                            else:
                                r_cord.append(int(sum_month[sum_month['month']==i].num_sequences))

                        D=[]
                        for i in range(len(r_cord)):
                            D.append([NEW[i],r_cord[i]])

                        Cases=pd.DataFrame(D, columns=["Month","Number of cases"])

                        col1, col2 =st.columns(2)
                        col1.metric("Year: ", time_filter)
                        col2.metric("Region: ", country_filter)

                        col1, col2 = st.columns(2)

                        theta =np.linspace(90,450,13)
                        theta=theta[0:12]
                        selected_points={}
                        with col1:
                            fig = go.Figure()
                            circle=np.linspace(0,360,60)
                            circle_r=np.empty(len(circle))
                            circle_r.fill(0.1)
                            marker_size=r_cord/np.linalg.norm(r_cord)
                            marker_size=marker_size*100
                            fig.add_trace(go.Scatterpolar(
                                    r = circle_r,
                                    theta = circle,
                                    mode = 'lines',
                                    #hoverinfo='skip',
                                    line_color = 'green',
                                    #hoverinfo=None,
                                    hoverinfo='skip',
                                    showlegend = False
                                ))
                            a=str(np.sum(r_cord))

                            fig.add_trace(go.Barpolar(
                                r=r_cord,
                                theta=theta,
                                width=[1,1,1,1,1,1,1,1,1,1,1,1,],
                                #marker_color=["#E4FF87", '#709BFF', '#709BFF', '#FFAA70', '#FFAA70', '#FFDF70', '#B6FFB4'],
                                marker_line_color="green",
                                text=['January','February','March','April', 'May','June', 'July','August', 'September','October','November','December' ],
                                marker_line_width=1,
                                opacity=0.8,
                                #text=r_cord,
                                #hoverinfo='text',
                                hovertemplate ='Total no of cases<br>%{r:.2f}'

                            )
                            )
                            fig.add_trace(go.Scatterpolar(
                                r=[5,5,5,5,5,5,5,5,5,5,5,5],
                                theta=theta,
                                mode='markers + text',
                                text=['January','February','March','April', 'May','June', 'July','August', 'September','October','November','December' ],
                                fillcolor='green',
                                marker_size=marker_size,
                                customdata = [[NEW[i],r_cord[i]] for i in range(len(r_cord))],
                                #name=r_cord,
                                textposition="middle center",
                                #hoverinfo='name',
                                hovertemplate= '%{customdata[0]}<br>Total no of cases:<br>%{customdata[1]:.3f}'
                            ))

                            fig.add_trace(go.Scatterpolar(
                                r=r_cord,
                                theta=theta,
                                mode='markers',
                                fillcolor='green',
                                marker_size=r_cord
                            ))

                            fig.update_layout(showlegend=False,
                                template=None,
                                polar = dict(
                                    radialaxis = dict(range=[-4, 5], showline=False, showgrid=False,showticklabels=False, ticks=''),
                                    angularaxis = dict(showline=False,showticklabels=False, showgrid=False, ticks='')
                                )
                            )

                            selected_points = plotly_events(fig)

                        month='All'
                        if len(selected_points)!=0:
                            month=selected_points[0]['pointNumber']
                            month=NEW[month]
                            data2=data1[data1['month']==month]
                        else:
                            data2=data1

                        df  = data2.groupby(["variant_grouped"])["num_sequences"].sum().reset_index()
                        df=df.rename(columns={"variant_grouped":"Variants", "num_sequences":"Total No. of cases"})
                        df=df.sort_values(by=['Variants'],ascending=True)
                        with col2:
                            fig2= px.bar(df, x="Total No. of cases", y="Variants", orientation='h', color="Variants")
                            fig2

                        #st.write("The first plot represents total number of ")


                        if month!='All':
                            st.write("#### Month chosen: "+ month)

                        st.write("The first visualization encodes the number of covid cases in each month through the marker size. "
                        "For quantitative understanding, the values are given in the hover table as well. The second visualization "
                        "is a representation of the covid cases during the time period (year/month if selected) by variants. ")
                        st.write("Given below is also the data table for covid cases in each month." )
                        Cases

        

else:
    
      def load_lottiefile(filepath: str):
            with open(filepath, "r") as f:
                return json.load(f)
      def load_lottieurl(url: str):
            r = requests.get(url)
            if r.status_code != 200:
                return None
            return r.json()

      lottie_coding = load_lottiefile("h.json")
      lottie_hello = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_M9p23l.json")

      st_lottie(
            lottie_hello,
            speed=1,
            reverse=False,
            loop=True,
            quality="low", # medium ; high
            #renderer="svg", # canvas
            height=None,
            width=None,
            key=None,
       )
    
        
      st.title("PAN AFRICAN UNIVERSITY ")
      st.header("INSTITUTE FOR BASIC SCIENCES TECHNOLOGY AND INNOVATION")
      st.header("PROGRAMME : Msc Data Science")
      st.header("COURSE : PAU 3106 DATA VISUALIZATION AND VISUAL ANALYTICS")
      st.header("NAME : Abdoul Aziz Diallo")
      st.header('REG,NO : MD300-0006/2021')
      st.header("LECTURER : Dr.L.NDERU")
      
      st.header('EMAIL:dialloa513@gmail.com')
    
        
