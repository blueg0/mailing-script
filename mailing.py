import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart



server= smtplib.SMTP('smtp.gmail.com',25)
server.ehlo()



server.login('email@email.com', 'password')

msg = MIMEMultipart()
msg['From'] = 'sender'
msg['To'] = 'email2@email2.com'
msg['Subject'] = 'It\'s just a tset'

msg.attach(MIMEText('Hello world', 'plain'))

filename='test.jpg'
attachment= open(filename, 'rb') 

p= MIMEBase('application', 'octet-streams')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachement; filename{filename}')

msg.attach(p)

text=msg.as_string()

server.sendmail('email@email.com','email2@email2.com', text)