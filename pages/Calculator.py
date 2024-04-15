import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
st.set_page_config(layout="wide", page_title="Person Carbon Calculator")

air_travel=None
amount_renewable=0
gas_pipeline=0
domestic=0
gas_cylinder=0
international=0
private_travel=None
mileage=0
age=0
total_distance=0
train_travel=0
bus_travel=0
mealperday=0

conn=st.connection("gsheets", type=GSheetsConnection)
# data2=conn.read(worsheet="Rural",ttl=5)
                   
st.title(f"Welcome,")
st.title("Personal Carbon Calculator App")

region=st.selectbox("Select",['Urban','Rural'])
st.subheader("⚡Electricity used per month(KWh)")
val = st.number_input('',value = 0,min_value=0,max_value=1000)
electricity=st.slider('',0,1000,value=val,key='electricity')
electricity_bill=st.file_uploader("Upload a clear image of Electricity Bill")

st.subheader('')
st.subheader("🧯Gas Connection")
gas_connection=st.selectbox("Type of Gas Connection",['None','Gas Cylinder','Gas Pipeline'])
if gas_connection=='Gas Cylinder':
     gas_cylinder=st.number_input('Number of gas cylinders used in a month',step=1,value=0)   
elif gas_connection=='Gas Pipeline':
     gas_pipeline=st.number_input('Gas Usage per month(cubic metre)',step=1,value=0)
st.subheader('')
st.subheader("🚚Transport")
transport=st.multiselect("Transport (one or more)",['Air Travel','Train','Bus','Private Vehicle'])
if "Air Travel" in transport:
    air_travel=st.selectbox("Type of air travel",['None','Domestic','International'])
if air_travel=='Domestic':
    domestic=st.number_input("No. of one-way domestic flights per month",step=1,value=0)
if air_travel=='International':
    international=st.number_input("No. of one-way international flights per month",step=1,value=0)
if "Train" in transport:
        train_travel=st.number_input("Distance traveled by train in a week",value=0)
        
if "Bus" in transport:
    bus_travel=st.number_input('Distance traveled by Bus(Km) weekly',step=1,value=0)
if "Private Vehicle" in transport:  
       private_travel=st.selectbox("Fuel Type",['Petrol','Diesel'])
       mileage=st.number_input('Mileage',step=1,value=0)
       age=st.number_input('How old is your vehicle?',step=1,value=0)
       total_distance=st.number_input('Distance driven per day',step=1,value=0)
       PUC=st.file_uploader("Upload a clear image of PUC")

st.subheader("🗑️Waste Generated")
val1 = st.number_input('Waste Generated(Kg) per week', value = 0)
val1=max(val1,0)
waste=st.slider('',0,100,value=val1,key='waste')
val1=max(val1,0)
st.subheader('')
st.subheader("🍽️Meal")
food_type=st.selectbox("Meal preference",['Vegeterian','Non-Vegeterian'])
mealperday=st.number_input("Number of Meals per Day",step=1,value=0)
st.subheader('')
st.subheader("♻️Natural Resources")
renewable=st.selectbox("Any type of renewable energy generated",["No","Yes"])
if renewable=="Yes":
    amount_renewable=st.number_input("Amount of Energy Renewed(KWh)",step=1,value=0)
val2 = st.number_input('Wood used weekly(kg)', value = 0)
val2=st.slider('',0,100,value=val2,key='wood')
val2=max(val2,0)

if(val>0):
    val=round(((val*0.82-(float)(amount_renewable))*12)/1000,2)
if(gas_connection!=None):
    if(gas_cylinder):
        gas_cylinder=round((gas_cylinder*100*12)/1000,2)
    if(gas_pipeline):
        gas_pipeline=round((gas_pipeline*22.73*12)/1000,2)
if(domestic>0):
    domestic=round((domestic*348.5*12)/1000,2)
if(international>0):
    international=round((international*532.7*12)/1000,2)
if(train_travel):
    train_travel=round((train_travel*2.49*12)/1000,2)
if(bus_travel):
    bus_travel=round((bus_travel*0.1*52)/1000,2)
if(private_travel!=None):
    if(private_travel=="Petrol"):
        total_distance=round((total_distance*mileage*2.2*365)/1000,2)
    if(private_travel=="Diesel"):
        total_distance=round((total_distance*mileage*2.6*365)/1000,2)
if(val2>0):
    val2=round((val2*1.6*52)/1000,2)
if(waste>0):
    waste=round((waste*1.49*52)/1000,2)
if(food_type!=None):
    if(food_type=="Vegeterian"):
        mealperday=round((mealperday*0.776*365)/1000,2)
    if(food_type=="Non-Vegeterian"):
        mealperday=round((mealperday*1.552*365)/1000,2)



submit_button=st.button("Calculate the CO₂ Emission")

total_emmision=val+gas_cylinder+gas_pipeline+domestic+international+train_travel+bus_travel+total_distance+val2+waste+mealperday

if submit_button:
    st.header("Results")

    col1, col2=st.columns(2)
    with col1:
        st.info(f"Electricity : {val} tonnes of CO₂ produced")
        st.info(f"Gas Connection : {gas_cylinder+gas_pipeline} tonnes of CO₂ produced")
        st.info(f"Air travel : {domestic+international} tonnes of CO₂ produced")
        st.info(f"Train travel : {train_travel} tonnes of CO₂ produced")
        st.info(f"Bus Travel : {bus_travel} tonnes of CO₂ produced")
    with col2:
        st.info(f"Private Travel : {total_distance} tonnes of CO₂ produced")
        st.info(f"Wood used : {val2} tonnes of CO₂ produced")
        st.info(f"Waste generated : {waste} tonnes of CO₂ produced")
        st.info(f"Food : {mealperday} tonnes of CO₂ produced")
    if(age>15):
        st.warning("The age of vehicle is above 15, Please check the local laws if driving this vehicle is legal or not")
    st.subheader("Your Total Carbon Emission(in tonnes of CO₂ produced)")
    st.info(f"Your Total Carbon Emission: {total_emmision} tonnes of CO₂ produced")
    if(region=='Urban'):
        if(total_emmision>2.5):
            st.warning(f"Your average CO₂ consumption is {((total_emmision-2.5)/2.5)*100}% above Average")
        else:
            st.info(f"Your average CO₂ consumption is {((2.5-total_emmision)/2.5)*100}% below Average")
        st.warning("Urban area average CO₂ consumption is 2.5 tonnes of CO₂")

        data=conn.read(worksheet="Urban",usecols=list(range(10)),ttl=5)
        data=data.dropna(how="all")
        urban_data=pd.DataFrame(
        [
            {
                "Electricity": val,
                "Gas Connection": gas_cylinder+gas_pipeline,
                "Air Travel": domestic+international,
                "Train Travel": train_travel,
                "Bus Travel": bus_travel,
                "Private Travel": total_distance,
                "Wood Used": val2,
                "Waste": waste,
                "Food": mealperday,
                "Total": total_emmision,
            }
        ]
     )
        updated_urban=pd.concat([data,urban_data],ignore_index=True)
        conn.update(worksheet="Urban",data=updated_urban)
        st.success("All Details are recorded in our records")
    if(region=='Rural'):
        if(total_emmision>0.85):
            st.warning(f"Your average CO₂ consumption is {round(((total_emmision-0.85)/0.85)*100,2)}% above Average")
        else:
            st.info(f"Your average CO₂ consumption is {((round(0.85-total_emmision)/0.85)*100,2)}% below Average")
        st.warning("Rural area average CO₂ consumption is 0.85 tonnes of ")
        
        data=conn.read(worksheet="Rural",usecols=list(range(10)),ttl=5)
        data=data.dropna(how="all")
        rural_data=pd.DataFrame(
        [
            {
                "Electricity": val,
                "Gas Connection": gas_cylinder+gas_pipeline,
                "Air Travel": domestic+international,
                "Train Travel": train_travel,
                "Bus Travel": bus_travel,
                "Private Travel": total_distance,
                "Wood Used": val2,
                "Waste": waste,
                "Food": mealperday,
                "Total": total_emmision,
            }
        ]
        )
        updated_rural=pd.concat([data,rural_data],ignore_index=True)
        conn.update(worksheet="Rural",data=updated_rural)
        st.success("All Details are recorded in our records")

    #upload data
    
