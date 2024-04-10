import streamlit as st
import pandas as pd
import psycopg2
import plotly.express as px
from streamlit_option_menu import option_menu



p_db= psycopg2.connect(host='localhost', user='postgres', password='123456', database='phonepe_pulse', port=5432)
cursor= p_db.cursor()


st.set_page_config(page_title= "Phonepe Pulse Data Visualization",
                   layout= "wide",
                   initial_sidebar_state= "expanded",
                  )

import streamlit as st

# Custom CSS for the title
title_html = """
    <style>
        /* Styling for the title */
        .title {
            color: white; /* Text color */
            background-color: #6F36AD; /* Background color */
            padding: 10px 20px; /* Padding */
            border-radius: 10px; /* Rounded corners */
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Box shadow */
        }
    </style>
    <h1 class="title">PhonePe Pulse Data Visualization</h1>
"""

# Display the title with custom CSS
st.markdown(title_html, unsafe_allow_html=True)

#sidebar option set up
with st.sidebar:
    
    select_page= option_menu("Phonepe Pulse",["Home", "Explore Data", "Insights"],
                  icons=["house","graph-up-arrow","bar-chart-line", "exclamation-circle"],
                  menu_icon= "menu-button-wide",
                  default_index=0,
                  styles={"nav-link": {"font-size": "20px", "text-align": "left", "margin": "-2px", "--hover-color": "#6F36AD"},
                        "nav-link-selected": {"background-color": "#6F36AD"}})


#setting up home page
if select_page == "Home":

    col1,col2= st.columns(2)
    
    with col1:
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.markdown("#")
        st.markdown("##")
        st.markdown("######")
        st.write("------")
        st.markdown(":violet[*PhonePe is an Indian digital payments and financial technology company*]")
        st.download_button("DOWNLOAD THE APP NOW", "https://www.phonepe.com/app-download/")
        

                
    with col2:
        st.title(":violet[Phonepe Pulse Data visualization with plotly]")
        st.write(":violet[Technologies used :] Github Cloning, Python, Pandas, PostgreSQL, Streamlit, and Plotly.")
        st.write(":violet[Overview :] In this streamlit web app you can visualize the phonepe pulse data and gain lot of insights on transactions, number of users, top 10 state, district, pincode and which brand has most number of users and so on. Bar charts, Pie charts and Geo map visualization are used to get some insights.")
        st.write("---")
       
        
        st.markdown(":violet[*Download transformed pulse data file below for reference*]")
        
        col3,col4,col5=st.columns(3)
        
        with col3:
            st.download_button("agg_trans","C:\\Users\\Saravanan\\OneDrive\\Desktop\\PhonePe\\pulse\\data\\aggregated\\transaction\\country\\india\\state\\")
            st.download_button("agg_user","C:\\Users\Saravanan\\OneDrive\\Desktop\\PhonePe\\pulse\\data\\aggregated\\user\\country\\india\\state\\")

        with col4:
            st.download_button("map_trans","C:\\Users\\Saravanan\\OneDrive\\Desktop\\PhonePe\\pulse\\data\\map\\transaction\\hover\\country\\india\\state\\")
            st.download_button("map_user","C:\\Users\\Saravanan\\OneDrive\\Desktop\\PhonePe\\pulse\\data\\map\\user\\hover\\country\\india\\state\\")

        with col5:
            st.download_button("top_trans","C:\\Users\\Saravanan\\OneDrive\\Desktop\\PhonePe\\pulse\\data\\top\\transaction\\country\\india\\state\\")
            st.download_button("top_user","C:\\Users\\Saravanan\\OneDrive\\Desktop\\PhonePe\\pulse\\data\\top\\user\\country\\india\\state\\")

# # setting up menu - explore data
if select_page == "Explore Data":
    Type = st.sidebar.selectbox("*Type*", ("Transactions", "Users","Insurance"))
    Year = st.sidebar.slider("*Year*", min_value=2018, max_value=2023)
    Quarter = st.sidebar.slider("*Quarter*", min_value=1, max_value=4)
    
    col1,col2 = st.columns(2)

# transaction data exploration
    if Type == "Transactions":
        
        # Overall State Data - TRANSACTIONS AMOUNT - INDIA MAP 
        with col1:
            st.markdown("## :blue[State Data - Transactions Amount]")
            cursor.execute(f"select state, sum(transaction_count) as Total_Transactions, sum(transaction_amount) as Total_amount from map_transaction where year = {Year} and quater = {Quarter} group by state order by state")
            df1 = pd.DataFrame(cursor.fetchall(),columns= ['State', 'Total_Transactions', 'Total_amount'])
            
        #geojson- geoJSON data source for indias state boundaries
            fig = px.choropleth(df1,geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                      featureidkey='properties.ST_NM',   #key in geoJSON file for thr state names
                      locations='State',
                      color='Total_amount',
                      color_continuous_scale='sunset')
              
        #update_geos- updates props of geo layout, fitbounds- adjust the state boundaries and ensures all locations given are visible within viewport
            fig.update_geos(fitbounds="locations", visible=False)
            st.plotly_chart(fig,use_container_width=True)
            
        # Overall State Data - TRANSACTIONS COUNT - INDIA MAP
        with col2:
            
            st.markdown("## :blue[State Data - Transactions Count]")
            cursor.execute(f"select state, sum(transaction_count) as Total_Transactions, sum(transaction_amount) as Total_amount from map_transaction where year = {Year} and quater = {Quarter} group by state order by state")
            df1 = pd.DataFrame(cursor.fetchall(),columns= ['State', 'Total_Transactions', 'Total_amount'])
            df1.Total_Transactions = df1.Total_Transactions.astype(float)
            

            fig = px.choropleth(df1,geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                      featureidkey='properties.ST_NM',
                      locations='State',
                      color='Total_Transactions',
                      color_continuous_scale='sunset')

            fig.update_geos(fitbounds="locations", visible=False)
            st.plotly_chart(fig,use_container_width=True)
            