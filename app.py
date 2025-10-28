import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Medals Visualization", layout="wide")
st.title("Medals Visualization")

#Dropdown Menu
medal = st.selectbox("Medal type", ["gold", "silver", "bronze"])

#Checkboxes
show_bar = st.checkbox("Show Bar Chart", Value=True) #building a checkbox to allow if you want to show the bar chart
show_pie = st.checkbox("Show Pie Chart", Value=True) #building a checkbox to allow if you want to show the pie chart

#two-col structure

col1,col2 = st. columns(2) #creating 2 cols

#To load the medal wide dataset
df = px.data.medals_wide()

#plot the bar chart
if show_bar:
    fig_bar = px.bar(df, 
                     x="nation", 
                     y= f"{medal}", #the value will be based on the medal type
                     title = f"Medals count ({medal})"
                     )
    
    fig_bar.update_layout(
        title_x = 0.5,
        xaxis_title = "Country",
        yaxis_title = "Count",
        height = 300
        )

    col1.plotly_chart(fig_bar, use_container_width=True) #in col 1, I'll include a ploty chart 


#plot the pie chart
if show_pie:
    fig_pie = px.pie(df, 
                     values= f"{medal}", 
                     names="Country", 
                     title = f"Medals count ({medal})"
                     )
    
    fig_pie.update_layout(
        title_x = 0.5,
        height = 300
        )

    col2.plotly_chart(fig_pie, use_container_width=True) #in col 2
