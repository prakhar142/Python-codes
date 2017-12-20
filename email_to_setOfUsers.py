from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

host='smtp.gmail.com'
port=587
username='mintsnpjs@gmail.com'
password='crystal$me'

from_email=username

to_list=['mintsnpjs@gmail.com','mintsnpjs@gmail.com','mintsnpjs@gmail.com']

try:
  email_conn=smtplib.SMTP(host,port)
  email_conn.ehlo()
  email_conn.starttls()
  email_conn.login(username,password)

  the_msg=MIMEMultipart("alternative") # This is standard  way of calling an html message. When server will receive this it will understand what we are doing
  the_msg['Subject']='Learning'
  the_msg['From']=from_email
#the_msg['To']=to_list
  plain_txt='Testing the message'
  html_txt="""\
<html>
  <head></head>
    <body>
      <p>Hey!<br>
      Testing this email <b>message</b>.Made by <a href='www.google.com'>google</a>
      </p>
    </body>
</html>
"""
    
  part_1=MIMEText(plain_txt,'plain')
  part_2=MIMEText(html_txt,'html')
  the_msg.attach(part_1)
  the_msg.attach(part_2)
  print(the_msg.as_string())
  for mail in to_list:
    email_conn.sendmail(from_email,mail,the_msg.as_string())
  email_conn.quit()
except smtplib.SMTPException:
     print('error sending message')
       
