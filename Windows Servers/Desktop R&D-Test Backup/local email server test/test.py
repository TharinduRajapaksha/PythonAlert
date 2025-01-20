import os
from email.message import EmailMessage
import smtplib
import ssl

stamp = " f meeeeeeeeeeeeeee"
ctx = ssl.create_default_context()
#password = "oendzqkqecuzqipw"    # Your app password goes here have to active app password specialy form google
password = "23aprJKIt#"
#sender = "expro.sap.alert@gmail.com"    # Your e-mail address
sender = "tharindur2@johnkeellsit.com"
receiver = "kasuna1@johnkeellsit.com" # Recipient's address
#message = "SAP System down at please act immediatly "
    

print("Programe came here without error to sent the email")

with smtplib.SMTP_SSL("smtp.keells.lk", port=25, context=ctx) as server:
    server.login(sender, password)
    #print(message)

    server.sendmail(sender, receiver, stamp)
    print("sent the email")
