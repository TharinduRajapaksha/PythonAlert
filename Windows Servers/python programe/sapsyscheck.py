####################### email sending methord - Google ##################################
def sendemail(stamp):
    import os
    from email.message import EmailMessage
    import smtplib
    import ssl

    #print(stamp)
    ctx = ssl.create_default_context()
    password = "oendzqkqecuzqipw"    # Your app password goes here have to active app password specialy form google
    sender = "expro.sap.alert@gmail.com"    # Your e-mail address
    receiver = "tharindur2@johnkeellsit.com" # Recipient's address
    #message = "SAP System down at please act immediatly "
    

    print("Programe came here without error to sent the email")

    with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=ctx) as server:
         server.login(sender, password)
         #print(message)

         server.sendmail(sender, receiver, stamp)


####################### email sending methord - locl mail server ###########################


    
####################### email grafting methord ###########################################
        

def emailgraft():

    global appdbstatus

    message = ""

    if appdbstatus["app"] == "Up" and appdbstatus["db"] == "Down":
        message = "Expro SAP System went down now due to Databse down.Please act immediatly."
    
    elif appdbstatus["app"] == "Down" and appdbstatus["db"] == "Up":
        message = "Expro SAP System went down now due to Application down.Please act immediatly."

    elif appdbstatus["app"] == "Down" and appdbstatus["db"] == "Down":
        message = "Expro SAP System went down now due to both Application, Database down.Please act immwediatly."

    return message
        

################################### File handaling methords ####################

def modefileread():
    fm = open("mode.txt", "r")
    text = fm.readline()
    return text
    fm.close()

def modefilewrite(txt):
    fm = open("mode.txt", "w")
    fm.write(txt)
    fm.close()

def countfileread():
    fc = open("count.txt", "r")
    text = fc.readline()
    print(text)
    number = int(text)
    return number
    fc.close()

def countfilewrite(number):
    txt = str(number)
    fc = open("count.txt", "w")
    fc.write(txt)
    fc.close()

    
        
        
        

###################### SAP System Checking methord ##############################

def sysstatuscheck():

    global appdbstatus



        
    ################################## sapcontrol command for app ##########################################

    sapcontrolresults = ["tharindu","","","","","","",""]

    f = open("sapcontrolresult.txt", "r")
    x = 0
    #print(sapcontrolresults[0])
    for l in f:
        sapcontrolresults[x] = l
        x = x+1
        #print(l)
    #print(sapcontrolresults[5])
    f.close()

    status1 = sapcontrolresults[4].strip(" ").split(",")
    status2 = sapcontrolresults[5].strip(" ").split(",")
    #print(status1)
    #print(status2)
    #print(status1[2])
    #print(status2[2])

    if status1[2] == " GREEN" and status2[2] == " GREEN":
        #print("SAP System app is up and running")
        appdbstatus["app"] = "Up"
    else:
        #print("SAP System app is down")
        appdbstatus["app"] = "Down"
        modefilewrite("silent")
        #sendemail(stamp)


        
    ################################# R3trans -d command for DB ############################################

    R3transdresults = ["tharindu","","","","","","",""]
    
    f2 = open("R3trans-dresult.txt", "r")
    x = 0
    #print(R3transdresults[0])
    for l2 in f2:
        R3transdresults[x] = l2
        x = x+1
        #print(l2)
    #print(R3transdresults[4])
    f2.close()

    statusdb =   R3transdresults[4].strip(" ").split(" ")
        
    print(statusdb)
    #print(statusdb[1])
    #print(statusdb[2])

    if statusdb[1] == 'finished' and statusdb[2] == '(0000).':
        #print("SAP System DB up and running")
        appdbstatus["db"] = "Up"
            
    else:
        print("SAP System DB down")
        appdbstatus["db"] = "Down"
        modefilewrite("silent")
            


    if appdbstatus["app"] == "Up" and appdbstatus["db"] == "Up":
            
        modefilewrite("active")
        countfilewrite(0)
        #print("programe came here")

        
    elif modefileread() == "silent" and countfileread() <= 3:
        
        number = countfileread()
        countfilewrite(number+1)
        
        print("programe came here")

        message = emailgraft()
        print(message)
        sendemail(message)
    
        

    
        

    #print(appdbstatus["db"])
    #print(appdbstatus["app"])
        

        
        
        

####################### main programe ############################################

import os
from email.message import EmailMessage
import smtplib
import ssl
import subprocess

#subprocess.call([r'C:\Users\tharindur2\Desktop\R&D- Test\sapcontrol&R3transexecute-batscript.bat'])

mode = ""
count = 0
appdbstatus = {"app":"","db":""}


sysstatuscheck()#This is for get update "appdbstatus" dictionary.

print(mode)

#print(appdbstatus["app"])





