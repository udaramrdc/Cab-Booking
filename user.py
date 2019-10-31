import EmailHandler
import random
import pymongo
from pymongo import MongoClient

#to generate Random OTP
def generateOTP():
    otp= random.randrange(1000,9999, 51)
    return str(otp)

#checking database for availability of vehicle
def VehicleAvailability(vehicleType):
    client = MongoClient("mongodb+srv://ramvilas:dyLpbazez8QuFxUk@cluster0-chgdf.mongodb.net/test?retryWrites=true&w=majority")
    db = client.CabData #database name
    coll = db.CabCollection #collections in database
    #checking for vehicle in Database
    vehicle_details = coll.find_one({'Type': vehicleType,'Status':0})
    if vehicle_details is not None:
        #update database
        coll.update_one({'_id':vehicle_details['_id']},{"$set":{'Status':1}})
        return vehicle_details 
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


#customer_Details = {"Name":"mangal murmu","pickup_location":"ccfdsdf","Destination":"Jammu","vehicleType":"MINI","mobile_no":"123456789","CUSTOMER_EMAIL":"2017ucs0057@iitjammu.ac.in"}
#Customer_info(customer_Details)

#status= {"Driver Name":"Ramvilas Babera","Vehicle No.":"12541552","Contact No.":"7051303387","Type":"SUV","Model":"Bolero","Price":"Rs. 500","Email":"2017uee0078@iitjammu.ac.in"}  
