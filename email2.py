import csv
import ssl
import smtplib

import email.utils

message = """Subject: Your grade

Hi {name}, your grade is {grade}"""
from_address = "shreyasgup21@gmail.com"
# turn on access to local device via security feature of google account
password = input("Type your password and press enter: ")

context = ssl.create_default_context()
# for sending from different servers change the server name in smtp.gmail.com
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(from_address, password)
    with open("ntacts_file.csv") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for name, email, grade in reader:
            server.sendmail(
                from_address,
                email,
                message.format(name=name,grade=grade),
            )
