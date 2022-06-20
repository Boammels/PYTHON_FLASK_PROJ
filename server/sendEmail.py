import smtplib

def sendEmail(content, reciever):
    #check 587 if this doesn't work
    mail = smtplib.SMTP('smtp.gmail.com',587) 
    mail.ehlo()
    mail.starttls()
    # Email has been set up with these credentials
    mail.login('h11ajbls@gmail.com', "passw0rd@123")
    mail.sendmail('h11ajbls@gmail.com', reciever, content)
    mail.close()
