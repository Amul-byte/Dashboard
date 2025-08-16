import streamlit as st

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go 
import nbformat

df = pd.read_csv('/Users/amulpoudel/Developer/Dashboard/Data.csv')
df = df.rename(columns={"Latitude": "lat", "Longitude": "lon"})
map_list=['basic', 'carto-darkmatter', 'carto-darkmatter-nolabels', 'carto-positron', 'carto-positron-nolabels', 'carto-voyager', 'carto-voyager-nolabels', 'dark', 'light', 'open-street-map', 'outdoors', 'satellite', 'satellite-streets', 'streets', 'white-bg']
st.title("Dashboard for Indian Census")

state_list = df['State'].unique().tolist()
state_list.insert(0,'Overall')
state = st.sidebar.selectbox('Select State',state_list)

map = st.sidebar.selectbox('Select State',map_list)
if state:
    if state == 'Overall':
        fig = px.scatter_map(df, lat='lat',
                     lon='lon',
                     text="District", # which column to use to set the color of markers # column added to hover information
                     size="Population", # size of markers
                     color='State',
                     hover_name='literacy_rate',
                     zoom=3,
                     width=800,
                     height=550,
                     center={'lat':22,
                             'lon':79}
                     ,map_style=map
                     )
        # Zoom to INDIA only not whole has paramster visible which helps!!
        fig.update_geos(fitbounds="locations",visible = False)
        st.plotly_chart(fig)
        
        
        
    else:
        temp_df = df[df['State']==state]
        fig = px.scatter_map(temp_df, lat='lat',
                        lon='lon',
                        text="District", # which column to use to set the color of markers # column added to hover information
                        size="Population", # size of markers
                        color='State',
                        hover_name='literacy_rate',
                        zoom=3,
                        width=800,
                        height=550,
                        center={'lat':22,
                                'lon':79}
                        ,map_style=map
                        )
    # Zoom to INDIA only not whole has paramster visible which helps!!
        fig.update_geos(fitbounds="locations",visible = False)
        st.plotly_chart(fig)