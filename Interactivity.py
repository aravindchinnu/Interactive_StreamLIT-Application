import streamlit as st
import pandas as pd
import altair as alt
import numpy as np

who_data = pd.read_csv('WHO_data.csv')

st.write(who_data)

st.sidebar.header("Pick Two variables for your scatterplot")

x_var = st.sidebar.selectbox("Pick your X-Axis",who_data.select_dtypes(include = np.number).columns.tolist())
y_var = st.sidebar.selectbox("Pick your Y-Axis",who_data.select_dtypes(include = np.number).columns.tolist())

scatter = alt.Chart(who_data,title = f"Correlation between {x_var} and {y_var}").mark_point(size = 100,opacity=0.9,fill='green',color = 'green').encode(
    alt.X(x_var,title = f"{x_var}"),
    alt.Y(y_var,title = f"{y_var}"), 
    tooltip=[x_var,y_var]).properties(width=500, height=500)

st.altair_chart(scatter.interactive(), use_container_width=True)

#Correlation Calculation
corr = round(who_data[x_var].corr(who_data[y_var]),2)

st.write(f"correlation between {x_var} and {y_var} is {corr}")