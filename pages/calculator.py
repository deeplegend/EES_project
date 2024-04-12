import streamlit as st

st.set_page_config(layout="wide", page_title="Person Carbon Calculator")
                   
st.title(f"Welcome,")
st.title("Personal Carbon Calculator App")

region=st.selectbox("Select",['None','Urban','Rural'])

if region=='Urban':
    val = st.number_input('Electricity used per month(KWh)', value = 0)
    val=max(0,val)
    electricity=st.slider('',0,100,value=val,key='electricity')
    val=max(0,val)
    gas_connection=st.selectbox("Type of Gas Connection",['None','Gas Cylinder','Gas Pipeline'])
    if gas_connection=='Gas Cylinder':
        gas_cylinder=st.number_input('Number of gas cylinders used in a month',step=1,value=None)
        gas_cylinder=max(0,gas_cylinder)
    elif gas_connection=='Gas Pipeline':
        gas_pipeline=st.number_input('Gas Usage per month(cubic metre)',step=1,value=None)

    transport=st.multiselect("Transport (one or more)",['Air Travel','Train','Bus','Private Vehicle'])
    if "Air Travel" in transport:
        air_travel=st.selectbox("Type of air travel",['None','Domestic','International'])
        if air_travel=='Domestic':
            domestic=st.number_input("No. of one-way domestic flights per month",step=1,value=None)
        if air_travel=='International':
            international=st.number_input("No. of one-way international flights per month",step=1,value=None)
    if "Train" in transport:
        train_travel=st.selectbox("Time traveled per month in train",['Less than 12hrs','between 12 and 24 hrs','More than 24 hrs'])
        
    if "Bus" in transport:
        bus_travel=st.number_input('Distance traveled by Bus(Km) weekly',step=1,value=None)
    if "Private Vehicle" in transport:  
        private_travel=st.selectbox("Fuel Type",['Petrol','Diesel'])
        mileage=st.number_input('Mileage',step=1,value=None)
        age=st.number_input('How old is your vehicle?',step=1,value=None)
        total_distance=st.number_input('Distance driven per day',step=1,value=None)

    food_type=st.selectbox("Meal preference",['Vegeterian','Non-Vegeterian'])
    val1 = st.number_input('Waste Generated(Kg) per week', value = 0)
    val1=max(val1,0)
    waste=st.slider('',0,100,value=val1,key='waste')
    val1=max(val1,0)
    mealperday=st.number_input("Number of Meals per Day",step=1,value=None)
    renewable=st.selectbox("Any type of renewable energy generated",["No","Yes"])
    if renewable=="Yes":
        amount_renewable=st.number_input("Amount of Energy Renewed(KWh)",step=1,value=None)


    

elif region=='Rural':
    val = st.number_input('Electricity used per month(KWh)', value = 0)
    val=max(0,val)
    electricity=st.slider('',0,100,value=val,key='electricity')
    val=max(0,val)
    gas_connection=st.selectbox("Type of Gas Connection",['None','Gas Cylinder','Gas Pipeline'])
    if gas_connection=='Gas Cylinder':
        gas_cylinder=st.number_input('Number of gas cylinders used in a month',step=1,value=None)
    elif gas_connection=='Gas Pipeline':
        gas_pipeline=st.number_input('Gas Usage per month(cubic metre)',step=1,value=None)
        
    val2 = st.number_input('Wood used weekly(kg)', value = 0)
    val2=st.slider('',0,100,value=val2,key='wood')
    val2=max(val2,0)

    transport=st.multiselect("Transport (one or more)",['Air Travel','Train','Bus','Private Vehicle'])
    if "Air Travel" in transport:
        air_travel=st.multiselect("Type of air travel",['None','Domestic','International'])
        if "Domestic" in air_travel:
            domestic=st.number_input("No. of one-way domestic flights per month",step=1,value=None)
        if "International" in air_travel:
            international=st.number_input("No. of one-way international flights per month",step=1,value=None)
    if "Train" in transport:
        train_travel=st.selectbox("Time traveled per month in train",['Less than 12hrs','between 12 and 24 hrs','More than 24 hrs'])
        
    if "Bus" in transport:
        bus_travel=st.number_input('Distance traveled by Bus(Km) weekly',step=1,value=None)
    if "Private Vehicle" in transport:  
        private_travel=st.selectbox("Fuel Type",['Petrol','Diesel'])
        mileage=st.number_input('Mileage',step=1,value=None)
        age=st.number_input('How old is your vehicle?',step=1,value=None)
        total_distance=st.number_input('Distance driven per day',step=1,value=None)

    food_type=st.selectbox("Meal preference",['Vegeterian','Non-Vegeterian'])
    val1 = st.number_input('Waste Generated(Kg) per week', value = 0)
    waste=st.slider('',0,100,value=val1,key='waste')
    mealperday=st.number_input("Number of Meals per Day",step=1,value=None)
    renewable=st.selectbox("Any type of renewable energy generated",["No","yes"])
    if renewable=="yes":
        amount_renewable=st.number_input("Amount of Energy Renewed(KWh)",step=1,value=None)

submit_button=st.button("Calculate the CO₂ Emission")

if submit_button:
    st.header("Results")
    

# def get_query_params():
#     return st.query_params


# EMISSION_FACTORS = {
        
#     "India":{
#         "Transportation": 0.225, #kgCO2/km(Average)
#         "Electricity": 1.0, #kgCO2/Kwh (Average)
#         "Diet": 1.325, #kgCO2/meal
#         "Waste": 0.4 #kgCO2/kg
#     },
#     "SriLanka":{
#          "Transportation": 0.14, #kgCO2/km
#         "Electricity": 0.82, #kgCO2/Kwh
#         "Diet": 1.25, #kgCO2/meal
#         "Waste": 0.1 #kgCO2/kg
#     },
#     "United States of America":{
#         "Transportation": 0.225, #kgCO2/km
#         "Electricity": 1.0, #kgCO2/Kwh
#         "Diet": 1.325, #kgCO2/meal
#         "Waste": 0.4 #kgCO2/kg
#     },
#     "China": {
#         "Transportation": 0.18,   # kgCO2/km
#         "Electricity": 0.95,      # kgCO2/Kwh
#         "Diet": 1.2,              # kgCO2/meal
#         "Waste": 0.3              # kgCO2/kg
#     },
#     "Brazil": {
#         "Transportation": 0.175,  # kgCO2/km
#         "Electricity": 0.45,      # kgCO2/Kwh
#         "Diet": 1.15,             # kgCO2/meal
#         "Waste": 0.2              # kgCO2/kg
#     },
#     "Russia": {
#         "Transportation": 0.2,    # kgCO2/km
#         "Electricity": 0.8,       # kgCO2/Kwh
#         "Diet": 1.3,              # kgCO2/meal
#         "Waste": 0.35             # kgCO2/kg
#     },
#     "Canada": {
#         "Transportation": 0.22,   # kgCO2/km
#         "Electricity": 0.7,       # kgCO2/Kwh
#         "Diet": 1.35,             # kgCO2/meal
#         "Waste": 0.45             # kgCO2/kg
#     },
#     "Australia": {
#         "Transportation": 0.19,   # kgCO2/km
#         "Electricity": 0.9,       # kgCO2/Kwh
#         "Diet": 1.25,             # kgCO2/meal
#         "Waste": 0.35             # kgCO2/kg
#     },
#     "Japan": {
#         "Transportation": 0.17,   # kgCO2/km
#         "Electricity": 0.75,      # kgCO2/Kwh
#         "Diet": 1.4,              # kgCO2/meal
#         "Waste": 0.25             # kgCO2/kg
#     }
    
        
# }


# st.markdown(
#     """
#     <style>
#     #MainMenu {visibility: hidden;}
#     footer {visibility: hidden;}
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# st.markdown(
#     r"""
#     <style>
#     .stDeployButton {
#             visibility: hidden;
#         }
#     [data-testid="stStatusWidget"] {
#     visibility: hidden;
# }
#     </style>
#     """, unsafe_allow_html=True
    
    
# )


# query_params = get_query_params()
# user_name = query_params.get("user_name", "")

# st.title(f"Welcome, {user_name}")
# st.title("Personal Carbon Calculator App")


# #user inputs
# st.subheader("🌎 Your Country")
# country = st.selectbox("Select", ["SriLanka","India", "United States of America", "China", "Brazil", "Russia", "Canada", "Australia", "Japan"])

# col1 , col2 = st.columns(2)

# with col1:
#     st.subheader("🚗 Daily Commute Distance (in KM)")
#     distance = st.slider("Distance", 0, 100, key="distance_input")
    
#     st.subheader("💡 Monthly Electricity Consumption (in Kwh)")
#     electricity = st.slider("Electricity", 0.0, 1000.0, key="electricity_input")
    
# with col2:

#     st.subheader("🗑 Waste generated per week (in KG)")
#     meals = st.slider("Waste", 0, 100, key="waste_input")
    
#     st.subheader("🍮 Number of meals per-day")
#     waste = st.number_input("Meals", 0, 10, key="meals_input")

# #Normalized

# if distance > 0:
#     distance = distance * 365 #convert daily to yearly
    
# if electricity > 0:
#     electricity = electricity * 12
    
# if meals > 0:
#     meals = meals * 365

# if waste > 0:
#     waste = waste * 52
    
# #calculate carbon emissions

# transportation_emission = EMISSION_FACTORS[country]["Transportation"] * distance
# electricity_emission = EMISSION_FACTORS[country]["Electricity"] * electricity
# diet_emission = EMISSION_FACTORS[country]["Diet"] * meals
# waste_emission = EMISSION_FACTORS[country]["Waste"] * waste

# transportation_emission = round(transportation_emission / 1000, 2)
# electricity_emission = round(electricity_emission / 1000, 2)
# diet_emission = round(diet_emission / 1000, 2)
# waste_emission = round(waste_emission / 1000, 2)


# #convert emissions to tonnes and round off to 3 decimal points
# total_emissions = round(transportation_emission + electricity_emission + diet_emission + waste_emission, 2)

# if st.button("Calculate CO2 Emissions"):
    
#     st.header("Results")
    
#     col3, col4 = st.columns(2)
    
#     with col3:
#         st.subheader("Carbon Emission by Catagories")
#         st.info(f"🚗 Tranportation: {transportation_emission} tonnes CO2 per year")
#         st.info(f"💡 Electricity: {electricity_emission} tonnes CO2 per year" )
#         st.info(f"🍮 Diet: {diet_emission} tonnes CO2 per year" )
#         st.info(f"🗑 Waste: {waste_emission} tonnes CO2 per year" )
        
#     with col4:
#         st.subheader("Total Carbon Emissions")
#         st.info(f"🌎 Your Total Carbon Footprint is: {total_emissions} tonnes CO2 per year")
        
#         if country == "India":
#             st.warning("Per capita carbon dioxide (CO₂) emissions in India have soared in recent decades, climbing from 0.39 metric tons in 1970 to a high of 1.91 metric tons in 2022. This was an increase of 5.5 percent in comparison to 2021 levels. Total CO₂ emissions in India also reached a record high in 2022.")
#         elif country == "SriLanka":
#             st.warning("Per capita carbon dioxide (CO₂) emissions in Sri Lanka have been steadily increasing over the years.")
#         elif country == "United States of America":
#             st.warning("Per capita carbon dioxide (CO₂) emissions in the United States of America have remained high, contributing significantly to global emissions.")
#         elif country == "China":
#             st.warning("Per capita carbon dioxide (CO₂) emissions in China are among the highest in the world, primarily due to its large population and rapid industrialization.")
#         elif country == "Brazil":
#             st.warning("Per capita carbon dioxide (CO₂) emissions in Brazil are mainly driven by deforestation, agriculture, and energy production.")
#         elif country == "Russia":
#             st.warning("Per capita carbon dioxide (CO₂) emissions in Russia are influenced by its vast natural resources and heavy reliance on fossil fuels.")
#         elif country == "Canada":
#             st.warning("Per capita carbon dioxide (CO₂) emissions in Canada are primarily attributed to its energy-intensive industries and transportation sector.")
#         elif country == "Australia":
#             st.warning("Per capita carbon dioxide (CO₂) emissions in Australia are among the highest globally, mainly due to its reliance on coal for electricity generation.")
#         elif country == "Japan":
#             st.warning("Per capita carbon dioxide (CO₂) emissions in Japan are significant, with the country heavily reliant on imported fossil fuels for energy production.")
                
# st.markdown(
#     """
#     <style>
#     .right-aligned {
#         display: flex;
#         justify-content: flex-end;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )
