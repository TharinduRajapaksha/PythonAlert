#!/usr/bin/env python3
####################### email sending methord - Google ##################################
def Gsendemail(stamp):
    import os
    from email.message import EmailMessage
    import smtplib
    import ssl

    #print(stamp)
    ctx = ssl.create_default_context()
    password = "oendzqkqecuzqipw"    # Your app password goes here have to active app password specialy form google
    sender = "expro.sap.alert@gmail.com"    # Your e-mail address
    receiver = "tharindur2@johnkeellsit.com" # Recipient's address
    #receiver = "aparnaso@johnkeellsit.com" # Recipient's address
    #message = "SAP System down at please act immediatly "
    

    print("Programe came here without error to sent the email")

    with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=ctx) as server:
         server.login(sender, password)
         #print(message)

         server.sendmail(sender, receiver, stamp)


####################### email sending methord - locl mail server ###########################

def Lsendemail(stamp):
	import smtplib

	sender = 'sap.alert@expro.com'
	receivers = ['kasuna1@johnkeellsit.com', 'tharindur2@johnkeellsit.com', 'aparnaso@johnkeellsit.com','Sahan.Angunawela@expro.com','John.Lewis@expro.com', 'Shane.Gibson@expro.com', 'joshua.blum@expro.com', 'martin.milligan@expro.com', 'Janusz.Santos@expro.com', 'Saumya.Fernando@expro.com', 'Robert.Ybarra@expro.com']
	#receivers = 'tharindur2@johnkeellsit.com'

	message = stamp

	#message = 'Subject:Expro DV3 SAP system down\n\nHi Executive, \n\nExpro Development SAP System went down due to Database down.Please act immediatly. \n\nThanks \nPython SAP Alert'

	try:
   		smtpObj = smtplib.SMTP("10.101.3.5", port=25)
   		smtpObj.sendmail(sender,receivers, message)         
   		print ("Successfully sent email")
	except SMTPException:
  		print ("Error: unable to send email from local email server switching to Gmail")
        #Gsendemail(message)
    
####################### email grafting methord ###########################################
        

def emailgraft():

    global appdbstatus

    message = ""

    if appdbstatus["app"] == "Up" and appdbstatus["db"] == "Down":
        message = "Subject:Expro S4 PRD SAP system down\n\nHi Executive, \n\nExpro S4 Production SAP System went down due to Database down.Please act immediatly. \n\nThanks\nPython SAP Alert"
    
    elif appdbstatus["app"] == "Down" and appdbstatus["db"] == "Up":
        message = "Subject:Expro S4 PRD SAP system down\n\nHi Executive \n\nExpro S4 Production SAP System went down due to Application down.Please act immediatly. \n\nThanks\nPython SAP Alert"

    elif appdbstatus["app"] == "Down" and appdbstatus["db"] == "Down":
        message = "Subject:Expro S4 PRD SAP system down\n\nHi Executive \n\nExpro S4 Production SAP System went down due to both Application, Database down.Please act immediatly. \n\nThanks\nPython SAP Alert"

    return message
        

################################### File handaling methords ####################

def modefileread():
    fm = open("/scripts/pythonalert/mode.txt", "r")
    text = fm.readline()
    return text
    fm.close()

def modefilewrite(txt):
    fm = open("/scripts/pythonalert/mode.txt", "w")
    fm.write(txt)
    fm.close()

def countfileread():
    fc = open("/scripts/pythonalert/count.txt", "r")
    text = fc.readline()
    print(text)
    number = int(text)
    return number
    fc.close()

def countfilewrite(number):
    txt = str(number)
    fc = open("/scripts/pythonalert/count.txt", "w")
    fc.write(txt)
    fc.close()

def yellowcountfileread():
    fyc = open("/scripts/pythonalert/yellowcount.txt", "r")
    text = fyc.readline()
    number = int(text)
    return number
    fyc.close()

def yellowcountfilewrite(ycnumber):
    txt = str(ycnumber)
    fyc = open("/scripts/pythonalert/yellowcount.txt", "w")
    fyc.write(txt)
    fyc.close()


    
        
        
        

###################### SAP System Checking methord ##############################

def sysstatuscheck():

    global appdbstatus



        
    ################################## sapcontrol command for app ##########################################

    sapcontrolresults = ["tharindu","","","","","","","",""]

    f = open("/scripts/pythonalert/sapcontrolresult.txt", "r")
    x = 0
    #print(sapcontrolresults[0])
    for l in f:
        sapcontrolresults[x] = l
        x = x+1
        #print(l)
    #print(sapcontrolresults[5])
    f.close()

    status1 = sapcontrolresults[5].strip(" ").split(",")
    status2 = sapcontrolresults[6].strip(" ").split(",")
    #print(status1)
    #print(status2)
    #print(status1[2])
    #print(status2[2])

    if status1[2] == " GREEN" and status2[2] == " GREEN":
        #print("SAP System app is up and running")
        appdbstatus["app"] = "Up"

    elif status1[2] == " YELLOW" or status2[2] == " YELLOW":
	#print("programe came here to yellow senario")
        ynumber = yellowcountfileread()
        yellowcountfilewrite(ynumber+1)

        if yellowcountfileread() >= 3:
        	#print("SAP System app is down")
        	appdbstatus["app"] = "Down"
        	modefilewrite("silent")
        	#sendemail(stamp)


    elif status1[2] == " GRAY" or status2[2] == " GRAY":
        #print("SAP System app is down")
        appdbstatus["app"] = "Down"
        modefilewrite("silent")
        #sendemail(stamp)


        
    ################################# R3trans -d command for DB ############################################

    R3transdresults = ["tharindu","","","","","","","",""]
    
    f2 = open("/scripts/pythonalert/R3trans-dresult.txt", "r")
    x = 0
    #print(R3transdresults[0])
    for l2 in f2:
        R3transdresults[x] = l2
        x = x+1
        #print(l2)
    #print(R3transdresults[2])
    f2.close()

    statusdb =   R3transdresults[2].strip(" ").split(" ")
        
    #print(statusdb)
    #print(statusdb[1])
    #print(statusdb[2])

    if statusdb[1] == 'finished' and statusdb[2] == '(0000).\n':
        #print("SAP System DB up and running")
        appdbstatus["db"] = "Up"
            
    else:
        print("SAP System DB down")
        appdbstatus["db"] = "Down"
        modefilewrite("silent")
            


    if appdbstatus["app"] == "Up" and appdbstatus["db"] == "Up":
    
        if modefileread() == "silent" and countfileread() >= 1:

            upmessage = "Subject:Expro S4 PRD SAP system back online\n\nHi Executive, \n\nExpro S4 Production SAP System back online. \n\nThanks\nPython SAP Alert"
            Lsendemail(upmessage)
        
        modefilewrite("active")
        yellowcountfilewrite(0)
        countfilewrite(0)
        #print("programe came here")

        
    elif modefileread() == "silent" and countfileread() <= 2:
        
        number = countfileread()
        countfilewrite(number+1)
        
        print("programe came here")

        message = emailgraft()
        print(message)
        Lsendemail(message)
    
        

    
        

    #print(appdbstatus["db"])
    #print(appdbstatus["app"])
        

        
        
        

####################### main programe ############################################

import os
from email.message import EmailMessage
import smtplib
import ssl
import subprocess

 
subprocess.call(['/scripts/pythonalert/sapcontrolR3transexecute-shellscript.sh'])#This is to run the SAP commands for system status check and write the result to files




mode = ""
count = 0
appdbstatus = {"app":"","db":""}


sysstatuscheck()#This is for analyze the SAP command results.




#print(mode)
#print(appdbstatus["app"])





