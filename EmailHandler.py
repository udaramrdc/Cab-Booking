import smtplib 
import Admin

def sendStatus(customer_Details,status,OTP):  
    # creates SMTP session 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    

    s.starttls() 
    
    # Authentication 
    s.login(Admin.SENDER_EMAIL,Admin.SENDER_PASS) 
    if status is None:
        subject = "Cab Booking Status"
        body = "Dear Customer \nThe vehicle class which you want to book is currently not available please try another vehicle or visit later \n Thanks and Regards \nTeam Bajarang Dal"
        message = f'Subject: {subject}\n\n{body}'
        s.sendmail(Admin.SENDER_EMAIL, customer_Details["CUSTOMER_EMAIL"], message) 
    else:
        #mail to driver
        subject = "Booking"
        body = "Dear "+status["Driver Name"] +"\nYou got a new booking for your cab. Details of Customer are below"+"\nName: "+customer_Details["Name"]+"\nConatact No.: "+customer_Details["mobile_no"]+"\nEmail Id: "+customer_Details["CUSTOMER_EMAIL"]+"\nPick UP Location: "+customer_Details["pickup_location"]+"\nDestination: "+customer_Details["Destination"]+"\nto start ride please confirm with this OTP:"+str(OTP)+"\n Thanks and Regards \nTeam Bajarang Dal"
        message = f'Subject: {subject}\n\n{body}'
        s.sendmail(Admin.SENDER_EMAIL, status["Email"], message) 
    
        #mail to Customer 
        subject = "Cab Booking Status"
        body = "Dear Custmer \nYour Booking for Vehicle has been confirmed.The details of Driver & vehicle are given below"+"\nDriver Name: "+status["Driver Name"]+"\nVehicle No: "+status["Vehicle No."]+" ("+status["Type"]+")"+"\nContact No.: "+status["Contact No."]+"\nPrice : "+status["Price"]+"\nSee you at your given location "+customer_Details["pickup_location"] +". For More Details you can contact driver."+"\nto start ride please confirm with this OTP:"+str(OTP)+"\nRegards\nTeam Bajrang Dal"
        message = f'Subject: {subject}\n\n{body}'
        # sending the mail 
        s.sendmail(Admin.SENDER_EMAIL, customer_Details["CUSTOMER_EMAIL"], message) 
    
    # terminating the session 
    s.quit()

#status= {"Driver Name":"Ramvilas Babera","Vehicle No.":"12541552","Contact No.":"7051303387","Type":"SUV","Model":"Bolero","Price":"Rs. 500","Email":"2017uee0078@iitjammu.ac.in"}  
#OTP = "1234"
#customer_Details = {"Name":"Raju Jat","pickup_location":"Delhi","Destination":"jaipur","vehicleType":"SUV","mobile_no":"454464646","CUSTOMER_EMAIL":"rajivdudi7877@gmail.com"}

#sendStatus(customer_Details,status,OTP)
