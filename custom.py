# Importing built in module smtplib
import smtplib

host='smtp.gmail.com'
port=587
#Python to send email with gmail
username='mintsnpjs@gmail.com'
password='crystal$me'

from_email=username

to_list=['mintsnpjs@gmail.com']

email_conn =  smtplib.SMTP(host,port)
email_conn.ehlo()
email_conn.starttls()
email_conn.login(username,password)
email_conn.sendmail(from_email,to_list,'Hello. I did this')
email_conn.quit()
 
#importing only SMTP class from module
from smtplib import SMTP

email_conn2= SMTP(hot,port)
email_conn2.ehlo()
email_conn2.starttls()
email_conn2.login(username,password)
email_conn2.sendmail(from_email,to_list,'Hello. I did this')
email_conn2.quit()

#Exception handling in mail 

from smtplib import SMTP,SMTPAuthenticationError,SMTPException

pass_wrong= SMTP(host,port)
pass_wrong.ehlo()
pass_wrong.starttls()

try:
     pass_wrong.login(username,'wrong_password')
     pass_wrong.sendmail(from_email,to_list,'Hello. I did this')
except SMTPAuthenticationError:
         print('could not login')
except:
       print('An error occcured')
pass_wrong.quit()
