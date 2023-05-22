# Dzień 90 E -mail
import smtplib

from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email import encoders

# Tworzenie wiadomości e-mail
msg = MIMEMultipart()
msg['From'] = 'koncewicztomek@gmail.com'
msg['To'] = 'odbiorca@example.com'
msg['Subject'] = 'Temat wiadomości'

# Dodanie treści do wiadomości
tekst = 'Cześć! Oto przykładowa wiadomość e-mail z załącznikiem obrazka.'
msg.attach(MIMEText(tekst, 'plain'))

# Wczytanie obrazka i dodanie jako załącznik
with open('obrazek.jpg', 'rb') as file:
    img = MIMEImage(file.read(), name='obrazek.jpg')
    msg.attach(img)


from email.mime.application import MIMEApplication

# Konfiguracja serwera SMTP i wysłanie wiadomości
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('twoj_adres_email@example.com', 'Fijolek5')
server.send_message(msg)
server.quit()

# Zadanie - wyślij plik PDF przez e-mail

from email.mime.application import MIMEApplication

# Wczytanie pliku PDF I DODANIE GO JAKO ZAŁĄCZNIK
with open('dokument.pdf', 'rb') as file:
    pdf = MIMEApplication(file.read(), _subtype='pdf')
    pdf.add_header('Content-Disposition', 'attachment', filename='dokument.pdf')
msg.attach(pdf)

