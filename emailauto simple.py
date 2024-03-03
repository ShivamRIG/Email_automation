import smtplib
import credentatial as cd
from email.mime.multipart import MIMEMultipart


address_from="pythonemailauto80@gmail.com"  #from or the sender email
to_add=["shivamsingh8461@outlook.com"] #specified the email to sende to 
msg=MIMEMultipart()
msg['from']=address_from
msg['to']=" ".join(to_add)
msg['subject']='just check'
body='hello world'
email=cd.email #email specified in the credential as string as variable
passw=cd.passow #password specified in the credential as string as variable
print(passw)
mail = smtplib.SMTP_SSL("smtp.gmail.com",465)
mail.ehlo()
mail.login(email,passw)
text=msg.as_string()
mail.sendmail(address_from,to_add)
mail.quit()