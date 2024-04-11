import pandas as pd
import json
import os
import streamlit as st
import plotly.express as px
from sqlalchemy import create_engine

engine = create_engine('postgresql+psycopg2://postgres:123456@localhost/phonepe_pulse')



#1 aggregated/transaction
path="C:\\Users\\Saravanan\\OneDrive\\Desktop\\PhonePe\\pulse\\data\\aggregated\\transaction\\country\\india\\state\\"
state_list=os.listdir(path)

agg_trans_clm={'States':[], 'Years':[],'Quater':[],'Transaction_type':[], 'Transaction_count':[], 'Transaction_amount':[]}

for state in state_list:
    p_s=path+state+"/"
    years_list=os.listdir(p_s)
    for year in years_list:
        p_y=p_s+year+"/"
        quater_list=os.listdir(p_y)
        for quater in quater_list:
            p_q=p_y+quater
            Data=open(p_q,'r')
            D=json.load(Data)
            for i in D['data']['transactionData']:
              Name=i['name']
              count=i['paymentInstruments'][0]['count']
              amount=i['paymentInstruments'][0]['amount']
              agg_trans_clm['Transaction_type'].append(Name)
              agg_trans_clm['Transaction_count'].append(count)
              agg_trans_clm['Transaction_amount'].append(amount)
              agg_trans_clm['States'].append(state)
              agg_trans_clm['Years'].append(year)
              agg_trans_clm['Quater'].append(int(quater.strip('.json')))

agg_trans=pd.DataFrame(agg_trans_clm)

agg_trans['States']=agg_trans['States'].str.replace('andaman-&-nicobar-islands','andaman & nicobar')
agg_trans['States']=agg_trans['States'].str.replace('jammu-&-kashmir', 'jammu & kashmir')
agg_trans['States']=agg_trans['States'].str.replace('dadra-&-nagar-haveli-&-daman-&-diu','dadra and nagar haveli and daman and diu')
agg_trans['States']=agg_trans['States'].str.replace("-"," ")
agg_trans['States']=agg_trans['States'].str.title()



#2 aggregated/user
path="C:\\Users\Saravanan\\OneDrive\\Desktop\\PhonePe\\pulse\\data\\aggregated\\user\\country\\india\\state\\"
state_list=os.listdir(path)

agg_user_clm={'States':[], 'Years':[],'Quater':[],'Brands':[], 'Reg_user_count':[], 'Reg_percentage':[]}

for state in state_list:
    p_s=path+state+"/"
    years_list=os.listdir(p_s)
    for year in years_list:
        p_y=p_s+year+"/"
        quater_list=os.listdir(p_y)
        for quater in quater_list:
            p_q=p_y+quater
            Data=open(p_q,'r')
            D=json.load(Data)
            try:
                for i in D['data']['usersByDevice']:
                    Brand=i['brand']
                    count=i['count']
                    percentage=i['percentage']
                    agg_user_clm['Brands'].append(Brand)
                    agg_user_clm['Reg_user_count'].append(count)
                    agg_user_clm['Reg_percentage'].append(percentage)
                    agg_user_clm['States'].append(state)
                    agg_user_clm['Years'].append(year)
                    agg_user_clm['Quater'].append(int(quater.strip('.json')))
            except:
                pass

agg_users=pd.DataFrame(agg_user_clm)

agg_users['States']=agg_users['States'].str.replace('andaman-&-nicobar-islands','andaman & nicobar')
agg_users['States']=agg_users['States'].str.replace('jammu-&-kashmir', 'jammu & kashmir')
agg_users['States']=agg_users['States'].str.replace('dadra-&-nagar-haveli-&-daman-&-diu','dadra and nagar haveli and daman and diu')
agg_users['States']=agg_users['States'].str.replace("-"," ")
agg_users['States']=agg_users['States'].str.title()



#3 map/transaction
path="C:\\Users\\Saravanan\\OneDrive\\Desktop\\PhonePe\\pulse\\data\\map\\transaction\\hover\\country\\india\\state\\"
state_list=os.listdir(path)


map_trans_clm={'States':[], 'Years':[],'Quater':[],'District_name':[], 'Transaction_count':[], 'Transaction_amount':[]}

for state in state_list:
    p_s=path+state+"/"
    years_list=os.listdir(p_s)
    for year in years_list:
        p_y=p_s+year+"/"
        quater_list=os.listdir(p_y)
        for quater in quater_list:
            p_q=p_y+quater
            Data=open(p_q,'r')
            D=json.load(Data)
            try:
              for i in D['data']['hoverDataList']:
                Name=i['name']
                count=i['metric'][0]['count']
                amount=i['metric'][0]['amount']
                map_trans_clm['District_name'].append(Name)
                map_trans_clm['Transaction_count'].append(count)
                map_trans_clm['Transaction_amount'].append(amount)
                map_trans_clm['States'].append(state)
                map_trans_clm['Years'].append(year)
                map_trans_clm['Quater'].append(int(quater.strip('.json')))
            except Exception as e:
              print(f"Error processing file '{p_q}': {e}")

map_trans=pd.DataFrame(map_trans_clm)

map_trans['States']=map_trans['States'].str.replace('andaman-&-nicobar-islands','andaman & nicobar')
map_trans['States']=map_trans['States'].str.replace('jammu-&-kashmir', 'jammu & kashmir')
map_trans['States']=map_trans['States'].str.replace('dadra-&-nagar-haveli-&-daman-&-diu','dadra and nagar haveli and daman and diu')
map_trans['States']=map_trans['States'].str.replace("-"," ")
map_trans['States']=map_trans['States'].str.title()



#4 map/User
path="C:\\Users\\Saravanan\\OneDrive\\Desktop\\PhonePe\\pulse\\data\\map\\user\\hover\\country\\india\\state\\"
state_list=os.listdir(path)

map_User_clm={'States':[], 'Years':[],'Quater':[],'District_name':[], 'Reg_users':[], 'App_opens':[]}

for state in state_list:
    p_s=path+state+"/"
    years_list=os.listdir(p_s)
    for year in years_list:
        p_y=p_s+year+"/"
        quater_list=os.listdir(p_y)
        for quater in quater_list:
            p_q=p_y+quater
            Data=open(p_q,'r')
            D=json.load(Data)
            for i in D['data']['hoverData'].items():
              district=i[0]
              regusers=i[1]['registeredUsers']
              appopens=i[1]['appOpens']
              map_User_clm['District_name'].append(district)
              map_User_clm['Reg_users'].append(regusers)
              map_User_clm['App_opens'].append(appopens)
              map_User_clm['States'].append(state)
              map_User_clm['Years'].append(year)
              map_User_clm['Quater'].append(int(quater.strip('.json')))

map_users=pd.DataFrame(map_User_clm)

map_users['States']=map_users['States'].str.replace('andaman-&-nicobar-islands','andaman & nicobar')
map_users['States']=map_users['States'].str.replace('jammu-&-kashmir', 'jammu & kashmir')
map_users['States']=map_users['States'].str.replace('dadra-&-nagar-haveli-&-daman-&-diu','dadra and nagar haveli and daman and diu')
map_users['States']=map_users['States'].str.replace("-"," ")
map_users['States']=map_users['States'].str.title()



#5 Top transaction
path="C:\\Users\\Saravanan\\OneDrive\\Desktop\\PhonePe\\pulse\\data\\top\\transaction\\country\\india\\state\\"
state_list=os.listdir(path)

top_trans_clm={'States':[], 'Years':[],'Quater':[],'Pincodes':[], 'Transaction_count':[], 'Transaction_amount':[]}

for state in state_list:
    p_s=path+state+"/"
    years_list=os.listdir(p_s)
    for year in years_list:
        p_y=p_s+year+"/"
        quater_list=os.listdir(p_y)
        for quater in quater_list:
            p_q=p_y+quater
            Data=open(p_q,'r')
            D=json.load(Data)
            for i in D['data']['pincodes']:
                Entity_name=i['entityName']
                count=i['metric']['count']
                amount=i['metric']['amount']
                top_trans_clm['Pincodes'].append(Entity_name)
                top_trans_clm['Transaction_count'].append(count)
                top_trans_clm['Transaction_amount'].append(amount)
                top_trans_clm['States'].append(state)
                top_trans_clm['Years'].append(year)
                top_trans_clm['Quater'].append(int(quater.strip('.json')))

top_trans=pd.DataFrame(top_trans_clm)

top_trans['States']=top_trans['States'].str.replace('andaman-&-nicobar-islands','andaman & nicobar')
top_trans['States']=top_trans['States'].str.replace('jammu-&-kashmir', 'jammu & kashmir')
top_trans['States']=top_trans['States'].str.replace('dadra-&-nagar-haveli-&-daman-&-diu','dadra and nagar haveli and daman and diu')
top_trans['States']=top_trans['States'].str.replace("-"," ")
top_trans['States']=top_trans['States'].str.title()



#6 top/user
path="C:\\Users\\Saravanan\\OneDrive\\Desktop\\PhonePe\\pulse\\data\\top\\user\\country\\india\\state\\"
state_list=os.listdir(path)


top_user_clm={'States':[], 'Years':[],'Quater':[],'Pincodes': [], 'Reg_users':[]}

for state in state_list:
    p_s=path+state+"/"
    years_list=os.listdir(p_s)
    for year in years_list:
        p_y=p_s+year+"/"
        quater_list=os.listdir(p_y)
        for quater in quater_list:
            p_q=p_y+quater
            Data=open(p_q,'r')
            D=json.load(Data)
            for i in D['data']['pincodes']:
                Name=i['name']
                reg_users=i['registeredUsers']
                top_user_clm['Pincodes'].append(Name)
                top_user_clm['Reg_users'].append(reg_users)
                top_user_clm['States'].append(state)
                top_user_clm['Years'].append(year)
                top_user_clm['Quater'].append(int(quater.strip('.json')))

top_user=pd.DataFrame(top_user_clm)

top_user['States']=top_user['States'].str.replace('andaman-&-nicobar-islands','andaman & nicobar')
top_user['States']=top_user['States'].str.replace('jammu-&-kashmir', 'jammu & kashmir')
top_user['States']=top_user['States'].str.replace('dadra-&-nagar-haveli-&-daman-&-diu','dadra and nagar haveli and daman and diu')
top_user['States']=top_user['States'].str.replace("-"," ")
top_user['States']=top_user['States'].str.title()



#SQL

agg_trans.to_sql('agg_trans', engine, if_exists='replace', index=False)
agg_users.to_sql('agg_users', engine, if_exists='replace', index=False)
map_trans.to_sql('map_trans', engine, if_exists='replace', index=False)
map_users.to_sql('map_users', engine, if_exists='replace', index=False)
top_trans.to_sql('top_trans', engine, if_exists='replace', index=False)
top_user.to_sql('top_user', engine, if_exists='replace', index=False)


# all datframe
agg_trans_df = pd.read_sql('agg_trans', engine)
agg_users_df = pd.read_sql('agg_users', engine)
map_trans_df = pd.read_sql('map_trans', engine)
map_users_df = pd.read_sql('map_users', engine)
top_trans_df = pd.read_sql('top_trans', engine)
top_user_df = pd.read_sql('top_user', engine)


#"Analysis of State-wise Financial Transactions in India: Visualizing Trends and Patterns Based on Transaction Types"
def agg_trans():

    agg_trans_df = pd.read_sql('agg_trans', engine)

    states = agg_trans_df['States'].unique()
    excluded_columns = ['States', 'Transaction_count', 'Transaction_amount']
    
    row1 = st.columns(2)
    row2 = st.columns(2)
    row3 = st.columns(2)
    row4 = st.columns(2)
    row5 = st.columns(2)
    row6 = st.columns(2)

    with row1[1]:
        sub_columns = st.columns(2)
        
        with sub_columns[0]:
            coloum1 = [col for col in agg_trans_df.columns if col not in excluded_columns]
            selected_coloum1 = st.selectbox("Choose the 1st coloum", coloum1) 
        
        with sub_columns[1]:
            if selected_coloum1:
                coloum2 = [col for col in coloum1 if col != selected_coloum1]
            selected_coloum2 = st.selectbox("Choose the 2nd coloum", coloum2) 

    with row2[0]:
        agg_trans_fig1 = px.sunburst(agg_trans_df, path=[selected_coloum1, selected_coloum2], values='Transaction_count')
        agg_trans_fig1.update_layout(title='Transaction Count', title_x=0.35)
        st.plotly_chart(agg_trans_fig1)

    with row2[1]:
        agg_trans_fig2 = px.sunburst(agg_trans_df, path=[selected_coloum1, selected_coloum2], values='Transaction_amount')
        agg_trans_fig2.update_layout(title='Transaction Amount', title_x=0.35)
        st.plotly_chart(agg_trans_fig2)

    with row3[0]:
        selected_state = st.selectbox("Select the state", ['All states'] + list(states))
        if selected_state == 'All states':
            stateAT = agg_trans_df
        else:
            stateAT = agg_trans_df.query('States == @selected_state')

    with row4[0]:
        agg_trans_fig3 = px.scatter(stateAT, x='Transaction_count', y='Transaction_amount', color='Transaction_type',
                        facet_col='Years', facet_col_wrap=3,
                        title='Transaction Count vs Transaction Amount by Transaction Type and Year')
        agg_trans_fig3.update_layout(width=1500, height=600, xaxis_title='Transaction Count', yaxis_title='Transaction Amount')
        st.plotly_chart(agg_trans_fig3)
  
    with row5[1]:
        sub_columns = st.columns(2)
     
        with sub_columns[1]:
            coloum1 = agg_trans_df["Years"].unique()
            selected_year = st.selectbox("Select the year", coloum1)

    with row6[0]:
        agg_trans_yr = agg_trans_df[agg_trans_df["Years"]==selected_year]
        agg_trans_State = agg_trans_yr.groupby('States')[['Transaction_count', 'Transaction_amount']].sum()
        agg_trans_State.reset_index(inplace = True)

        agg_trans_fig4 = px.choropleth(
            agg_trans_State,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='States',
            color='Transaction_count',
            color_continuous_scale='turbo',
            range_color = (agg_trans_State['Transaction_count'].min(), agg_trans_State['Transaction_count'].max()),
            title = 'Transacion count'
            )

        agg_trans_fig4.update_geos(fitbounds="locations", visible=False)

        st.plotly_chart(agg_trans_fig4)

    with row6[1]:
        agg_trans_yr = agg_trans_df[agg_trans_df["Years"]==selected_year]
        agg_trans_State = agg_trans_yr.groupby('States')[['Transaction_count', 'Transaction_amount']].sum()
        agg_trans_State.reset_index(inplace = True)

        agg_trans_fig5 = px.choropleth(
            agg_trans_State,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='States',
            color='Transaction_amount',
            color_continuous_scale='turbo',
            range_color = (agg_trans_State['Transaction_amount'].min(), agg_trans_State['Transaction_amount'].max()),
            title = 'Transacion amount'
            )

        agg_trans_fig5.update_geos(fitbounds="locations", visible=False)

        st.plotly_chart(agg_trans_fig5)




#"Analyzing Regional Financial Transactions in India: Insights from State and District-Level Data"
def map_trans():
    map_trans_df = pd.read_sql('map_trans', engine)

    states = map_trans_df['States'].unique()
    
    row1 = st.columns(2)
    row2 = st.columns(2)
    row3 = st.columns(2)
    row4 = st.columns(3)
    row5 = st.columns(2)
    

    with row1[0]:
        selected_state = st.selectbox("Select the state", ['All states'] + list(states))
    
    with row1[1]:
        sub_columns = st.columns(2)
        
        with sub_columns[1]:
            coloum1 = map_trans_df["Years"].unique()
            selected_year = st.selectbox("Select the year", coloum1)

    with row2[0]:
        map_trans_yr = map_trans_df[map_trans_df["Years"]==selected_year]

        map_trans_state = map_trans_yr.groupby('States')[['Transaction_count', 'Transaction_amount']].sum()
        map_trans_state.reset_index(inplace = True)

        if selected_state == 'All states':
            stateMT = map_trans_state
        else:
            stateMT = map_trans_state[map_trans_state['States'] == selected_state]
                
        map_trans_fig1 = px.choropleth(
            stateMT,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='States',
            color='Transaction_count',
            color_continuous_scale='turbo',
            range_color = (map_trans_state['Transaction_count'].min(), map_trans_state['Transaction_count'].max()),
            title = 'Transacion count'
            )

        map_trans_fig1.update_geos(fitbounds="locations", visible=False)

        st.plotly_chart(map_trans_fig1)

    with row2[1]:
        map_trans_yr = map_trans_df[map_trans_df["Years"]==selected_year]

        map_trans_state = map_trans_yr.groupby('States')[['Transaction_count', 'Transaction_amount']].sum()
        map_trans_state.reset_index(inplace = True)
        if selected_state == 'All states':
            stateMT = map_trans_state
        else:
            stateMT = map_trans_state[map_trans_state['States'] == selected_state]
                

        map_trans_fig2 = px.choropleth(
            stateMT,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='States',
            color='Transaction_amount',
            color_continuous_scale='turbo',
            range_color = (map_trans_state['Transaction_amount'].min(), map_trans_state['Transaction_amount'].max()),
            title = 'Transacion amount'
            )

        map_trans_fig2.update_geos(fitbounds="locations", visible=False)

        st.plotly_chart(map_trans_fig2)

    if selected_state == 'All states':
            pass

    else:
        with row3[0]:

                map_trans_dis = map_trans_df.query('States == @selected_state and Years == @selected_year')


                map_trans_fig3 = px.bar(map_trans_dis, y=map_trans_dis['District_name'].apply(lambda x: x.replace("district", "")), 
                                x=['Transaction_count'],
                                color='Quater',
                                barmode='stack', orientation='h',
                                title='Transaction Count by District',
                                labels={'value': 'Transaction', 'variable': 'Type'})

                map_trans_fig3.update_layout(xaxis_title='Transaction count', title_x=0.35, yaxis_title='Districts', legend_title='Type', height= 700)

                st.plotly_chart(map_trans_fig3)
        
        with row3[1]:
            
                map_trans_dis_M = map_trans_df.query('States == @selected_state and Years == @selected_year')


                map_trans_fig4 = px.bar(map_trans_dis_M, y=map_trans_dis_M['District_name'].apply(lambda x: x.replace("district", "")), 
                                x=['Transaction_amount'],
                                color='Quater',
                                barmode='stack', orientation='h',
                                title='Transaction amount by District',
                                labels={'value': 'Transaction', 'variable': 'Type'})

                map_trans_fig4.update_layout(xaxis_title='Transaction amount', title_x=0.35, yaxis_title='Districts', legend_title='Type', height= 700)

                st.plotly_chart(map_trans_fig4)

        with row4[1]:
            selected_dic = st.selectbox("Select the district", sorted(map_trans_dis_M['District_name'].unique()))

            map_trans_dis_bar = map_trans_dis_M.query('District_name == @selected_dic')
        
        with row5[0]:
            map_trans_fig5 = px.bar(map_trans_dis_bar, y='Transaction_count', 
                                x='Quater',
                                color='Quater',
                                barmode='stack',
                                title='Transaction count by District',
                                labels={'value': 'Transaction', 'variable': 'Type'})

            map_trans_fig5.update_layout(xaxis_title='Quater', title_x=0.35, yaxis_title='Transaction count', legend_title='Type')

            st.plotly_chart(map_trans_fig5)
            

        with row5[1]:
            map_trans_fig6 = px.bar(map_trans_dis_bar, y='Transaction_amount', 
                                x='Quater',
                                color='Quater',
                                barmode='stack',
                                title='Transaction amount by District',
                                labels={'value': 'Transaction', 'variable': 'Type'})

            map_trans_fig6.update_layout(xaxis_title='Quater', title_x=0.35, yaxis_title='Transaction amount', legend_title='Type')

            st.plotly_chart(map_trans_fig6)
            




#"Exploring Regional Financial Transactions in India: A Deep Dive into Top Transactions by State, Quarter and Pincode"
def top_trans():
    top_trans_df = pd.read_sql('top_trans', engine)

    states = top_trans_df['States'].unique()

    row1 = st.columns(2)
    row2 = st.columns(2)
    row3 = st.columns(4)
    row4 = st.columns(2)
    

    with row1[0]:
        selected_state = st.selectbox("Select the state", ['All states'] + list(states))
    
    with row1[1]:
        sub_columns = st.columns(2)
        
        with sub_columns[1]:
            coloum1 = top_trans_df["Years"].unique()
            selected_year = st.selectbox("Select the year", coloum1)

    with row2[0]:
        top_trans_yr = top_trans_df[top_trans_df["Years"]==selected_year]

        top_trans_state = top_trans_yr.groupby('States')[['Transaction_count', 'Transaction_amount']].sum()
        top_trans_state.reset_index(inplace = True)

        if selected_state == 'All states':
            stateTT = top_trans_state
        else:
            stateTT = top_trans_state[top_trans_state['States'] == selected_state]
                
        top_trans_fig1 = px.choropleth(
            stateTT,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='States',
            color='Transaction_count',
            color_continuous_scale='turbo',
            range_color = (top_trans_state['Transaction_count'].min(), top_trans_state['Transaction_count'].max()),
            title = 'Transacion count'
            )

        top_trans_fig1.update_geos(fitbounds="locations", visible=False)

        st.plotly_chart(top_trans_fig1)

    with row2[1]:
        top_trans_yr = top_trans_df[top_trans_df["Years"]==selected_year]

        top_trans_state = top_trans_yr.groupby('States')[['Transaction_count', 'Transaction_amount']].sum()
        top_trans_state.reset_index(inplace = True)
        if selected_state == 'All states':
            stateTT = top_trans_state
        else:
            stateTT = top_trans_state[top_trans_state['States'] == selected_state]
                

        top_trans_fig2 = px.choropleth(
            stateTT,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='States',
            color='Transaction_amount',
            color_continuous_scale='turbo',
            range_color = (top_trans_state['Transaction_amount'].min(), top_trans_state['Transaction_amount'].max()),
            title = 'Transacion amount'
            )

        top_trans_fig2.update_geos(fitbounds="locations", visible=False)

        st.plotly_chart(top_trans_fig2)

        if selected_state == 'All states':
            pass

        else:

            with row3[1]:
                selected_quater = st.selectbox("Select the quater", top_trans_df['Quater'].unique())

                
            with row4[0]:

                    top_trans_Pin = top_trans_df.query('States == @selected_state and Years == @selected_year and Quater == @selected_quater').reset_index(drop=True)
                    top_trans_Pin['Pincodes']=top_trans_Pin['Pincodes'].apply(lambda x: x + " -")

                    top_trans_fig3 = px.bar(top_trans_Pin, x ='Transaction_count',
                                            y= 'Pincodes',
                                            color='Transaction_count',
                                            orientation='h',
                                            title='Top 10 Transaction count'
                                            )
                   
                    top_trans_fig3.update_layout(xaxis_title='Transaction_count',title_x=0.35,  yaxis_title='Pincodes')

                    st.plotly_chart(top_trans_fig3)

                    #st.write(top_trans_Pin[['Pincodes', 'Transaction_count']])
            
            with row4[1]:
                
                    top_trans_Pin = top_trans_df.query('States == @selected_state and Years == @selected_year and Quater == @selected_quater').reset_index(drop=True)
                    top_trans_Pin['Pincodes']=top_trans_Pin['Pincodes'].apply(lambda x: x + " -")

                    top_trans_fig4 = px.bar(top_trans_Pin, y='Pincodes', 
                                x='Transaction_amount',
                                color='Transaction_amount',
                                barmode='stack',
                                title='Top 10 Transaction amount',
                                labels={'value': 'Transaction', 'variable': 'Type'}
                                )

                    

                    top_trans_fig4.update_layout(xaxis_title='Transaction amount', title_x=0.35, yaxis_title='Pincodes')

                    st.plotly_chart(top_trans_fig4)

                    #st.write(top_trans_Pin[['Pincodes', 'Transaction_amount']])
    
    

#"Exploring User Registration Trends Across States and Brands in India"
def agg_user():
    agg_users_df = pd.read_sql('agg_users', engine)

    states = agg_users_df['States'].unique()
        
    row1 = st.columns(2)
    row2 = st.columns(2)
    row3 = st.columns(2)
    

    with row1[0]:
        selected_state = st.selectbox("Select the state", states)
    
    with row1[1]:
        sub_columns = st.columns(3)
        
        with sub_columns[0]:
            selected_year = st.selectbox("Select the year", ['2018', '2019', '2020', '2021'])
        
        with sub_columns[1]:
            selected_quater = st.selectbox("Select the quater", agg_users_df['Quater'].unique()) 
        
        with sub_columns[2]:
            agg_users_B = agg_users_df.query(' States == @selected_state and Years == @selected_year')
            selected_brand = st.selectbox("Select the brand", agg_users_B["Brands"].unique())

    with row2[0]:
        agg_users_Brand = agg_users_df.query(' States == @selected_state and Years == @selected_year and Quater == @selected_quater ')

        agg_users_fig1 = px.bar(agg_users_Brand, y='Reg_user_count', 
                                x='Brands',
                                color='Brands',
                                barmode='stack',
                                title=f'Registered count of Brands for the {selected_quater} quater of year {selected_year}',
                                labels={'value': 'Transaction', 'variable': 'Type'})

        agg_users_fig1.update_layout(xaxis_title='Brands', yaxis_title='Count', legend_title='Type')

        st.plotly_chart(agg_users_fig1)


    with row2[1]:
        agg_users_Brand = agg_users_df.query(' States == @selected_state and Years == @selected_year and Brands == @selected_brand ')

        agg_users_fig2 = px.bar(agg_users_Brand, y='Reg_percentage', 
                                x='Quater',
                                color='Quater',
                                barmode='stack',
                                title=f'Analysis of \"{selected_brand}\" for the year {selected_year} in Percentage',
                                labels={'value': 'Transaction', 'variable': 'Type'})

        agg_users_fig2.update_layout(xaxis_title=f'{selected_brand}', title_x=0.1, yaxis_title='Percentage', legend_title='Type')

        st.plotly_chart(agg_users_fig2)

        
    with row3[0]:
        agg_users_yr = agg_users_df[agg_users_df["Years"]==selected_year]
        agg_users_state = agg_users_yr.groupby('States')[['Reg_user_count', 'Reg_percentage']].sum()
        agg_users_state.reset_index(inplace = True)

        agg_users_fig3 = px.choropleth(
            agg_users_state,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='States',
            color='Reg_user_count',
            color_continuous_scale='turbo',
            range_color = (agg_users_state['Reg_user_count'].min(), agg_users_state['Reg_user_count'].max()),
            title = f'Registered count for {selected_year}'
            )

        agg_users_fig3.update_geos(fitbounds="locations", visible=False)

        st.plotly_chart(agg_users_fig3)

    with row3[1]:
        agg_users_yr = agg_users_df[agg_users_df["Years"]==selected_year]
        agg_users_state = agg_users_yr.groupby('States')[['Reg_user_count', 'Reg_percentage']].sum()
        agg_users_state.reset_index(inplace = True)
        stateAU = agg_users_state[agg_users_state['States'] == selected_state]

        agg_users_fig4 = px.choropleth(
            stateAU,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='States',
            color='Reg_user_count',
            color_continuous_scale='turbo',
            range_color = (agg_users_state['Reg_user_count'].min(), agg_users_state['Reg_user_count'].max()),
            title = f'Registered count of {selected_state} in {selected_year}'
            )

        agg_users_fig4.update_geos(fitbounds="locations", visible=False)

        st.plotly_chart(agg_users_fig4)


#"Mapping User Engagement and Registration Patterns: Analyzing District-level Data in India"
def map_user():
    map_users_df = pd.read_sql('map_users', engine)

    states = map_users_df['States'].unique()
        
    row1 = st.columns(2)
    row2 = st.columns(2)
    row3 = st.columns(2)
    row4 = st.columns(3)
    row5 = st.columns(2)
    

    with row1[0]:
        selected_state = st.selectbox("Select the state", ['All states'] + list(states))
        
    
    with row1[1]:
        sub_columns = st.columns(2)
        
        with sub_columns[0]:
            pass
        
        with sub_columns[1]:
            coloum1 = map_users_df["Years"].unique()
            selected_year = st.selectbox("Select the year", coloum1)

    with row2[0]:
        map_users_yr = map_users_df[map_users_df["Years"]==selected_year]

        map_users_state = map_users_yr.groupby('States')[['Reg_users', 'App_opens']].sum()
        map_users_state.reset_index(inplace = True)

        if selected_state == 'All states':
            stateMU = map_users_state
        else:
            stateMU = map_users_state[map_users_state['States'] == selected_state]
                
        map_users_fig1 = px.choropleth(
            stateMU,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='States',
            color='Reg_users',
            color_continuous_scale='turbo',
            range_color = (map_users_state['Reg_users'].min(), map_users_state['Reg_users'].max()),
            title = 'Registered users'
            )

        map_users_fig1.update_geos(fitbounds="locations", visible=False)

        st.plotly_chart(map_users_fig1)

    with row2[1]:
        map_users_yr = map_users_df[map_users_df["Years"]==selected_year]

        map_users_state = map_users_yr.groupby('States')[['Reg_users', 'App_opens']].sum()
        map_users_state.reset_index(inplace = True)
        if selected_state == 'All states':
            stateMU = map_users_state
        else:
            stateMU = map_users_state[map_users_state['States'] == selected_state]
                

        map_users_fig2 = px.choropleth(
            stateMU,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='States',
            color='App_opens',
            color_continuous_scale='turbo',
            range_color = (map_users_state['App_opens'].min(), map_users_state['App_opens'].max()),
            title = 'Number of app open'
            )

        map_users_fig2.update_geos(fitbounds="locations", visible=False)

        st.plotly_chart(map_users_fig2)

    if selected_state == 'All states':
            pass

    else:
        with row3[0]:

                map_users_dis = map_users_df.query('States == @selected_state and Years == @selected_year')


                map_users_fig3 = px.bar(map_users_dis, y=map_users_dis['District_name'].apply(lambda x: x.replace("district", "")), 
                                x=['Reg_users'],
                                color='Quater',
                                barmode='stack', orientation='h',
                                title='Registered users by District',
                                labels={'value': 'Transaction', 'variable': 'Type'})

                map_users_fig3.update_layout(xaxis_title='Registered users', title_x=0.35, yaxis_title='Districts', legend_title='Type', height= 700)

                st.plotly_chart(map_users_fig3)
        
        with row3[1]:
            
                map_users_dis_M = map_users_df.query('States == @selected_state and Years == @selected_year')


                map_users_fig4 = px.bar(map_users_dis_M, y=map_users_dis_M['District_name'].apply(lambda x: x.replace("district", "")), 
                                x=['App_opens'],
                                color='Quater',
                                barmode='stack', orientation='h',
                                title='Number of app open by District',
                                labels={'value': 'Transaction', 'variable': 'Type'})

                map_users_fig4.update_layout(xaxis_title='Number of app open', title_x=0.35, yaxis_title='Districts', legend_title='Type', height= 700)

                st.plotly_chart(map_users_fig4)

        with row4[1]:
            selected_dic = st.selectbox("Select the district", sorted(map_users_dis_M['District_name'].unique()))

            map_users_dis_bar = map_users_dis_M.query('District_name == @selected_dic')
        
        with row5[0]:
            map_users_fig5 = px.bar(map_users_dis_bar, y='Reg_users', 
                                x='Quater',
                                color='Quater',
                                barmode='stack',
                                title='Registered users by District',
                                labels={'value': 'Transaction', 'variable': 'Type'})

            map_users_fig5.update_layout(xaxis_title='Quater', title_x=0.35, yaxis_title='Registered users', legend_title='Type')

            st.plotly_chart(map_users_fig5)

        with row5[1]:
            map_users_fig6 = px.bar(map_users_dis_bar, y='App_opens', 
                                x='Quater',
                                color='Quater',
                                barmode='stack',
                                title='Number of app open by District',
                                labels={'value': 'Transaction', 'variable': 'Type'})

            map_users_fig6.update_layout(xaxis_title='Quater', title_x=0.35, yaxis_title='Number of app open', legend_title='Type')

            st.plotly_chart(map_users_fig6)





#Top User Registration Patterns Analyzing
def top_user():
    top_user_df = pd.read_sql('top_user', engine)

    states = top_user_df['States'].unique()

    row1 = st.columns(2)
    row2 = st.columns(2)
    row3 = st.columns(4)
    row4 = st.columns(2)
    
    

    with row1[0]:
        selected_state = st.selectbox("Select the state", ['All states'] + list(states))
        
    
    with row1[1]:
        sub_columns = st.columns(2)
     
        with sub_columns[1]:
            coloum1 = top_user_df["Years"].unique()
            selected_year = st.selectbox("Select the year", coloum1)

    with row2[0]:
        top_user_yr = top_user_df[top_user_df["Years"]==selected_year]

        top_user_state = top_user_yr.groupby('States')['Reg_users'].sum()
        top_user_state = top_user_state.to_frame().reset_index()

        top_user_fig1 = px.choropleth(
            top_user_state,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey='properties.ST_NM',
            locations='States',
            color='Reg_users',
            color_continuous_scale='turbo',
            range_color = (top_user_state['Reg_users'].min(), top_user_state['Reg_users'].max()),
            title = 'Registered users'
            )

        top_user_fig1.update_geos(fitbounds="locations", visible=False)

        st.plotly_chart(top_user_fig1)

    if selected_state == 'All states':
        pass

    else:

        with row2[1]:
            top_user_yr = top_user_df[top_user_df["Years"]==selected_year]

            top_user_state = top_user_yr.groupby('States')['Reg_users'].sum()
            top_user_state = top_user_state.to_frame().reset_index()
            
            stateTU = top_user_state[top_user_state['States'] == selected_state]
                    

            top_user_fig2 = px.choropleth(
                stateTU,
                geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                featureidkey='properties.ST_NM',
                locations='States',
                color='Reg_users',
                color_continuous_scale='turbo',
                range_color = (top_user_state['Reg_users'].min(), top_user_state['Reg_users'].max()),
                title = 'Top number of app open in state'
                )

            top_user_fig2.update_geos(fitbounds="locations", visible=False)

            st.plotly_chart(top_user_fig2)

        

            with row3[3]:
                selected_quater = st.selectbox("Select a quater", top_user_df['Quater'].unique())

                
            with row3[0]:

                    top_user_Pin = top_user_df.query('States == @selected_state and Years == @selected_year and Quater == @selected_quater').reset_index(drop=True)
                    top_user_Pin['Pincodes']=top_user_Pin['Pincodes'].apply(lambda x: x + " -")

                    top_user_fig3 = px.bar(top_user_Pin, x ='Reg_users',
                                            y= 'Pincodes',
                                            orientation='h',
                                            title='Top 10 Transaction count'
                                            )
                   
                    top_user_fig3.update_layout(xaxis_title='Reg_users',title_x=0.35,  yaxis_title='Pincodes')

                    st.plotly_chart(top_user_fig3)

                    #st.write(top_user_Pin[['Pincodes', 'Reg_users']])



#streamlit

st.set_page_config(
    page_title="Phonepe Pulse Data Visualization",
    page_icon="📱",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'About': """Welcome to the Phonepe Pulse Data Visualization project!"""
    }
)

def styled_text(text, color="black", font_size=None, alignment="left", bold=False, background_color=None, bullet_points=False):
    style = ""
    if color:
        style += f"color: {color};"
    if font_size:
        style += f"font-size: {font_size}px;"
    if alignment:
        style += f"display: block; text-align: {alignment};"
    if bold:
        style += "font-weight: bold;"
    if background_color:
        style += f"background-color: {background_color};"

    if bullet_points:
        text = "<ul>" + "".join([f"<li>{line}</li>" for line in text.split("\n")]) + "</ul>"

    if style:
        text = f'<span style="{style}">{text}</span>'
    return text

def home_page():

    st.markdown(styled_text("Phonepe Pulse Data Visualization", 
                            color="violet", font_size="50", alignment="center", bold = True), unsafe_allow_html=True)

    st.header("About :")
    st.write("We look at how people use Phonepe to send money and buy things.")

    st.header("Get Our Information:")
    st.write("We get our information from Phonepe's github.")

    st.header("Technologies Used :")
    st.write("Github Cloning, Python, Pandas, PostgreSQL, Streamlit, and Plotly.")

    st.header("How to Use:")
    st.write("You can pick which place, year, or thing you want to see more about. Just click on the sidebar to learn more.")

page = st.sidebar.selectbox("", ["Home page", "Transacions", "Users"])

if page == "Home page":
    home_page()
    
if page == "Transacions":

    st.title("Understanding Money Flow Across India: Examining Trends, Patterns and Regional Differences")

    choice1 = st.selectbox("", [
                        "Visualizing Trends and Patterns Based on Transaction Types",
                        "Insights from State and District-Level Data",
                        "A Deep Dive into Top Transactions by State, Quarter and Pincode"
    ] )

    if choice1 == "Visualizing Trends and Patterns Based on Transaction Types":
        agg_trans()

    if choice1 == "Insights from State and District-Level Data":
        map_trans()

    if choice1 == "A Deep Dive into Top Transactions by State, Quarter and Pincode":
        top_trans()


if page == "Users":

    st.title("Analyzing User Registration Trends in India: State, Brand  and District-Level Insights")

    choice2 = st.selectbox("", [
                        "Checking User Sign-Up Trends Across States and Brands in India",
                        "Analyzing District-level Data of User Registration Patterns in India",
                        "Top User Registration Patterns Analyzing"
                             ] )

    if choice2 == "Checking User Sign-Up Trends Across States and Brands in India":
        agg_user()

    if choice2 == "Analyzing District-level Data of User Registration Patterns in India":
        map_user()

    if choice2 == "Top User Registration Patterns Analyzing":
        top_user()
    