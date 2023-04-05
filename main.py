import smtplib
from email.message import EmailMessage
import configparser

config = configparser.ConfigParser()
config.read('../CONFIG/config_my_mail.ini')

# Variables containing your email address and password
EMAIL_ADDRESS = config['info']['account']
EMAIL_PASSWORD = config['info']['key']

def mail(subject_string, to_mail_address, content_string):

    msg = EmailMessage()
    msg['Subject'] = subject_string
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to_mail_address
    msg.set_content(content_string)

    #with open('image.jpg', 'rb') as attach:
    #    msg.add_attachment(attach.read(), maintype='application', subtype='octet-stream', filename=attach.name)


    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)


if __name__ == '__main__':
    subject_string = 'My second Python email'
    to_mail_address = EMAIL_ADDRESS
    content_string = 'Hello world!'

    mail(subject_string, to_mail_address, content_string)




