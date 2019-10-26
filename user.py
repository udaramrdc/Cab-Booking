import pandas as pd
import EmailHandler
import random

#to generate Random OTP
def generateOTP():
    otp= random.randrange(1000,9999, 51)
    return str(otp)

#checking database for availability of vehicle
def VehicleAvailability(vehicleType):
    vehicle_details = pd.read_excel("Database/CABDATA.xlsx")
    output_columns=["Name", "NUMBER PLATE","TYPE","EMAIL","CONTACT","MODEL","Status"]
    for i in vehicle_details.index:
        if vehicle_details["TYPE"][i] == vehicleType and vehicle_details["Status"][i]==0:
            vehicle_details["Status"][i] = 1
            status = {"Driver Name":vehicle_details["Name"][i],"Vehicle No.":str(vehicle_details["NUMBER PLATE"][i]),"Contact No.":str(vehicle_details["CONTACT"][i]),"Type":vehicleType,"Model": vehicle_details["MODEL"][i],"Price":"500" ,"Email" : vehicle_details["EMAIL"][i] }  
            #update database
            writer = pd.ExcelWriter("CABDATA.xlsx")
            vehicle_details.to_excel(writer,"changed", index=False, columns=output_columns)
            writer.save()
            return status 
    return None
            
def Customer_info(customer_Details):
    #to check vehicle availability and if available then get details 
    status = VehicleAvailability(customer_Details["vehicleType"])
    
    if(status is None):
        EmailHandler.sendStatus(customer_Details,None,None)
    else:
        OTP = generateOTP()
        #Email to customer and Driver
        EmailHandler.sendStatus(customer_Details,status,OTP)


customer_Details = {"Name":"Raju Jat","pickup_location":"Delhi","Destination":"jaipur","vehicleType":"MICRO","mobile_no":"454464646","CUSTOMER_EMAIL":"2017ucs0057@iitjammu.ac.in"}
Customer_info(customer_Details)

#status= {"Driver Name":"Ramvilas Babera","Vehicle No.":"12541552","Contact No.":"7051303387","Type":"SUV","Model":"Bolero","Price":"Rs. 500","Email":"2017uee0078@iitjammu.ac.in"}  
