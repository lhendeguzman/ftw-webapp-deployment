import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px


import streamlit as st
import joblib

st.title('Forecasting Sales')
st.write('We demonstrate how we can forecast advertising sales based on ad expenditure.')


data=pd.read_csv('data/advertising_regression.csv')


#Add sliders and assign them to variables
st.sidebar.subheader('Advertising Costs')

TV = st.sidebar.slider('TV Advertising Cost', 0, 300, 150)

radio = st.sidebar.slider('Radio Advertising Cost', 0, 50, 25)
 
newspaper = st.sidebar.slider('Newspaper Advertising Cost', 0, 250, 125)


saved_model = joblib.load('advertising.sav')

# Predict sales using variables/features
predicted_sales = saved_model.predict([[TV, radio, newspaper]])[0]


'\n'
'\n'

# Print prediction
st.subheader(f"Predicted sales is {int(predicted_sales*1000)} dollars.")


'\n'
'\n'
'\n'
'\n'


st.write('Here is the data that we used:')

data


# Histogram
st.subheader('TV Ad Cost Distribution')

# Use numpy to generate bins for age
hist_values = px.histogram(data, x="TV", nbins=300, color_discrete_sequence=['indianred'])
st.plotly_chart(hist_values)

st.subheader('Radio Ad Cost Distribution')
# Use numpy to generate bins for age
hist_values = px.histogram(data, x="radio", nbins=300, color_discrete_sequence=['indianred'])
st.plotly_chart(hist_values)


st.subheader('Newspaper Ad Cost Distribution')
hist_values = px.histogram(data, x="TV", nbins=300, color_discrete_sequence=['indianred'])
st.plotly_chart(hist_values)



