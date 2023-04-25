import streamlit as st
import pandas as pd
import sqlite3

st.set_page_config(page_title='DATABASE', 
                   page_icon=':smiley:',
                   initial_sidebar_state="auto",
                   layout='centered'
                   )
st.title("Flood DataBase")
# Connect to the database
conn = sqlite3.connect('flood_reports.db')
cursor = conn.cursor()

# Query the database and create a DataFrame
df = pd.read_sql_query("SELECT * from flood_reports", conn)

# Display the DataFrame in the Streamlit app
st.dataframe(df)
