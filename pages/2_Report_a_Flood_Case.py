import streamlit as st
import sqlite3



st.set_page_config(page_title='REPORT', 
                   page_icon=':smiley:',
                   initial_sidebar_state="auto",
                   layout='centered'
                   )
st.title("Flood Report Form")
conn = sqlite3.connect('flood_reports.db')


with st.form('floodform',clear_on_submit=True):
    street_name = st.text_input("Street The Flood occur")
    city = st.text_input("City The Flood occur")
    state = st.text_input("State The Flood occur")
    country = st.text_input("Country The Flood occur")

    # Severity of the flood
    severity = st.selectbox("Severity of the flood", options=["High", "Medium", "Low"])

    # Date and time of the flood
    date = st.date_input("Date of the flood")
    time = st.time_input("Time of the flood")

    # Injuries or fatalities resulting from the flood
    injuries = st.number_input("Number of injuries resulting from the flood", min_value=0)
    fatalities = st.number_input("Number of fatalities resulting from the flood", min_value=0)

    # Damage to property or infrastructure caused by the flood
    property_damage = st.number_input("Estimated damage to property caused by the flood", min_value=0)
    infrastructure_damage = st.number_input("Estimated damage to infrastructure caused by the flood", min_value=0)

    # Potential hazards or safety concerns related to the flood
    hazards = st.text_area("Potential hazards or safety concerns related to the flood")

    # Actions taken to mitigate the effects of the flood
    mitigation_actions = st.text_area("Actions taken to mitigate the effects of the flood")
    
    submitted = st.form_submit_button()

def insert_data(street_name, city, state, country, severity, date, time, injuries, fatalities, property_damage, infrastructure_damage, hazards, mitigation_actions):
    conn.execute(f'''INSERT INTO flood_reports
                    (street_name, city, state, country, severity, date, time, injuries, fatalities, property_damage, infrastructure_damage, hazards, mitigation_actions)
                    VALUES
                    ('{street_name}', '{city}', '{state}', '{country}', '{severity}', '{date}', '{time}', {injuries}, {fatalities}, {property_damage}, {infrastructure_damage}, '{hazards}', '{mitigation_actions}')''')
    conn.commit()
    st.success("Data added successfully.")

# Add a button to submit the form data
if submitted:
    insert_data(street_name, city, state, country, severity, date, time, injuries, fatalities, property_damage, infrastructure_damage, hazards, mitigation_actions)
    st.success("Flood report submitted successfully!")
# Close the connection to the database
conn.close()

