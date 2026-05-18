import streamlit as st
import pandas as pd
import plotly.express as px

st.title("COVID-19 Trends Dashboard")

df = pd.read_csv('worldometer_coronavirus_daily_data.csv')

# Sidebar filter
countries = df['country'].unique().tolist()
selected_country = st.selectbox("Select a country", sorted(countries))

# Filter data
filtered = df[df['country'] == selected_country]

# Line chart
fig = px.line(filtered, x='date', y='cumulative_total_cases',
              title=f'Total COVID cases in {selected_country}')
st.plotly_chart(fig)

# Deaths chart
fig2 = px.line(filtered, x='date', y='cumulative_total_deaths',
               title=f'Total deaths in {selected_country}')
st.plotly_chart(fig2)
#daily_new_cases
fig3=px.line(filtered,x='date',y='daily_new_cases',title=f'Daily new cases in {selected_country}')
st.plotly_chart(fig3)