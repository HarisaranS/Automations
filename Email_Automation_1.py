import smtplib 

email = input("Enter a email to send :")

msg = input("Enter a msg to send :")

def sendEmail(email,msg):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('<gmail>','<password>')
    server.sendmail('<from_addr_gmail>',email,msg)
    server.close()

sendEmail(email,msg)
