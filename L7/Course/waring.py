import smtplib
from email.mime.text import MIMEText

def waring_message():
    #enter your gmail account and password!!
    gmail_user     = 'Donald J. Trump'
    gmail_password = 'MAGA2020!'    

    msg = MIMEText('someone fall !!!')
    msg['Subject'] = 'A mail from MLVD'
    msg['From']    = gmail_user
    msg['To']      = 'YouShouldEnterYourAccountHere@gmail.com'

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.send_message(msg)
    server.quit()
    print('Email sent!')
    #允許程式進行存取
    #https://accounts.google.com/DisplayUnlockCaptcha
    #低安全性應用程式存取權
    #https://myaccount.google.com/lesssecureapps