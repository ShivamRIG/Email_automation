# this python script send the image or docs over the internet
import os
import smtplib
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders

def email_send(img):
    Email_address= os.environ.get('EMAIL_USER') #specified the email address in enviroment 
    Email_PASS='pyfr nfwr wtxa vcaf '    #specified the email address in enviroment password


    msg=MIMEMultipart()
    msg['Subject']="Security issue"
    msg['From']=Email_address
    msg['To']='shivamsingh8461@outlook.com'
    filename = img
    with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)

# Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

# Add attachment to message and convert message to string
    msg.attach(part)
    with smtplib.SMTP_SSL('smtp.gmail.com',465)as smtp:     
        smtp.login(Email_address,Email_PASS)
        smtp.send_message(msg)
        print("email send")

email_send("./ronaldo.jpg")