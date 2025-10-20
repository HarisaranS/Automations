from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
import os

smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.ehlo()
smtp.starttls()

smtp.login('kakashihatakninja@gmail.com', 'ehme bebc yshk kmtq')  


send = input('Enter recipient email(s), separated by spaces: ').split()
sub = input("Enter the subject: ")
body = input("Enter the body of the email: ")
img = input("Enter the image file path (or leave empty): ").strip()
file = input("Enter the attachment file path (or leave empty): ").strip()


def sendEmail(subject, text, img=None, attachment=None):

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = 'kakashihatakninja@gmail.com'
    msg['To'] = ", ".join(send)

  
    msg.attach(MIMEText(text, 'plain'))

   
    if img:
        with open(img, 'rb') as f:
            img_data = f.read()
        msg.attach(MIMEImage(img_data, name=os.path.basename(img)))

 
    if attachment:
        with open(attachment, 'rb') as f:
            file_data = f.read()
        part = MIMEApplication(file_data, Name=os.path.basename(attachment))
        part['Content-Disposition'] = f'attachment; filename="{os.path.basename(attachment)}"'
        msg.attach(part)

    return msg


msg = sendEmail(sub, body, img if img else None, file if file else None)

smtp.sendmail('kakashihatakninja@gmail.com', send, msg.as_string())

smtp.quit()


print("Email sent successfully!")
