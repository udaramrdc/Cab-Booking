import streamlit as st
import user

st.title('Cab Booking')

Name = st.text_input("Name")
st.write("You Entered : ",Name) 

pic_location =  st.text_input("Pick Up Location")
st.write("Location : ",pic_location)

destination =  st.text_input("Destination Loction")
st.write("Dest. Location : ",destination)

email = st.text_input("E-mail")
st.write("E-mail : ",email)

phone = st.text_input("Contact No.")
st.write("You Entered : ",phone)

Vehicle = st.selectbox("Choose the Vehicle Type:",["","SUV","MINI","LUX","MICRO"])

if st.button('SUBMIT'):
    if(Name !=None and pic_location!=None and destination!=None and email!=None and phone!=None and Vehicle!=None):
        customer_Details = {"Name":Name,"pickup_location":pic_location,"Destination":destination,"vehicleType":Vehicle,"mobile_no":phone,"CUSTOMER_EMAIL":email}
        if(user.VehicleAvailability(Vehicle) is not None):
            user.Customer_info(customer_Details)
            st.balloons()
            st.write('You will Recieve Booking status soon on your email\nRefresh for new Booking')
        else:
            mess = "Sorry!!! This Vehicle type is not Available currently. Try with another"    
            st.write(mess) 
    else:
        st.write('Some Fields are Empty!!')

