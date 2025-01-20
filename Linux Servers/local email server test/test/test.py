import smtplib

sender = 'sap.alert@expro.com'
receivers = ['kasuna1@johnkeellsit.com', 'tharindur2@johnkeellsit.com']

message = 'Subject:Expro DV3 SAP system down\n\nThis is a test email form Expro dev server. send to multiple users'

try:
   smtpObj = smtplib.SMTP("10.101.3.5", port=25)
   smtpObj.sendmail(sender,receivers, message)         
   print ("Successfully sent email")
except SMTPException:
   print ("Error: unable to send email")
