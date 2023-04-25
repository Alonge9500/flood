import streamlit as st
import os
from PIL import Image




st.set_page_config(page_title='FLOOD', 
                   page_icon=':smiley:',
                   initial_sidebar_state="auto",
                   layout='centered'
                   )

image_path = os.path.join(os.getcwd(), 'flood.png')
image = Image.open(image_path)

st.title('Disaster and Emergencies (A Case Study of Flood)')

st.markdown("""
            Flooding is a temporary overflow of water onto land that is normally dry. Floods are the most common natural disaster in the United States. Failing to evacuate flooded areas or entering flood waters can lead to injury or death.
[Report A Flood Case](/Report_a_Flood_Case)
Floods may:

Result from rain, snow, coastal storms, storm surges and overflows of dams and other water systems.
Develop slowly or quickly. Flash floods can come with no warning.
Cause outages, disrupt transportation, damage buildings and create landslides.""")
st.subheader('If you are under a flood warning:')
st.image(image, caption='Flood Warning')

st.markdown("""* Find safe shelter right away.
            
* Do not walk, swim or drive through flood waters. Turn Around, Don’t Drown!
* Remember, just six inches of moving water can knock you down, and one foot of moving water can sweep your vehicle away.
* Stay off bridges over fast-moving water.
* Depending on the type of flooding

    + Evacuate if told to do so.
    + Move to higher ground or a higher floor.
    + Stay where you are.""")


st.subheader('Preparing for a Flood')
st.markdown("""+ Know Your Risk for Floods
Visit FEMA's Flood Map Service Center to know types of flood risk in your area.  Sign up for your community’s warning system. The Emergency Alert System (EAS) and National Oceanic and Atmospheric Administration (NOAA) Weather Radio also provide emergency alerts.

+ Purchase Flood Insurance
Purchase or renew a flood insurance policy. Homeowner’s insurance policies do not cover flooding. It typically takes up to 30 days for a policy to go into effect so the time to buy is well before a disaster. Get flood coverage under the National Flood Insurance Program (NFIP).

+ Preparing for a Flood
Make a plan for your household, including your pets, so that you and your family know what to do, where to go, and what you will need to protect yourselves from flooding. Learn and practice evacuation routes, shelter plans, and flash flood response. Gather supplies, including non-perishable foods, cleaning supplies, and water for several days, in case you must leave immediately or if services are cut off in your area.

+ In Case of Emergency
Keep important documents in a waterproof container. Create password-protected digital copies. Protect your property. Move valuables to higher levels. Declutter drains and gutters. Install check valves. Consider a sump pump with a battery.

""")

st.subheader('Staying Safe During a Flood')
image_path2 = os.path.join(os.getcwd(), 'flood2.png')
image2 = Image.open(image_path2)

st.image(image2, caption='Flood Warning')

st.markdown("""
            + Evacuate immediately, if told to evacuate. 

            + Never drive around barricades. 
            
            + Local responders use them to safely direct traffic out of flooded areas.
            
            + Contact your healthcare provider If you are sick and need medical attention. Wait for further care instructions and shelter in place, if possible. If you are experiencing a medical emergency, call 9-1-1.
            
            + Listen to EAS, NOAA Weather Radio or local alerting systems for current emergency information and instructions regarding flooding.
            
            + Do not walk, swim or drive through flood waters. Turn Around. Don’t Drown!
            
            + Stay off bridges over fast-moving water. Fast-moving water can wash bridges away without warning.
            
            + Stay inside your car if it is trapped in rapidly moving water. Get on the roof if water is rising inside the car.
            
            + Get to the highest level if trapped in a building. Only get on the roof if necessary and once there signal for help. Do not climb into a closed attic to avoid getting trapped by rising floodwater.""")



st.subheader('Staying Safe After a Flood')
image_path3 = os.path.join(os.getcwd(), 'flood3.png')
image3 = Image.open(image_path3)

st.image(image3, caption='Flood Warning')

st.markdown("""
            + Pay attention to authorities for information and instructions. Return home only when authorities say it is safe.
            + Avoid driving except in emergencies.
            + Wear heavy work gloves, protective clothing and boots during clean up and use appropriate face coverings or masks if cleaning mold or other debris. 
            + People with asthma and other lung conditions and/or immune suppression should not enter buildings with indoor water leaks or mold growth that can be seen or smelled. Children should not take part in disaster cleanup work.
            + Be aware that snakes and other animals may be in your house.
            + Be aware of the risk of electrocution. Do not touch electrical equipment if it is wet or if you are standing in water. Turn off the electricity to prevent electric shock if it is safe to do so.
            + Avoid wading in floodwater, which can be contaminated and contain dangerous debris. Underground or downed power lines can also electrically charge the water.
            + Use a generator or other gasoline-powered machinery ONLY outdoors and away from windows.""")

with st.sidebar:
    st.title("Flood Helpful Tips")

    # Create a list of all the markdown links
    markdown_links = [f"[Report A Flood Case](/Report_a_Flood_Case)",
                      "[If you are under a flood warning](/#disaster-and-emergencies-a-case-study-of-flood)",
                      "[Prparing For a Flood](/#preparing-for-a-flood)",
                      "[Staying Safe During A Flood](/#staying-safe-during-a-flood)",
                      "[Staying Safe During A Flood](/#staying-safe-during-a-flood)",
                      "[Staying Safe After a Flood](/#staying-safe-after-a-flood)"]
    

    # Use the `st.markdown()` function to display the list of links
    for markdown_link in markdown_links:
        st.markdown(markdown_link, unsafe_allow_html=True)
        

st.markdown("[Report A Flood Case](/Report_a_Flood_Case)")
