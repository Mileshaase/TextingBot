from ast import Delete
import smtplib
import requests

gmail_user = "bigfiles666@gmail.com"
gmail_password = "MHmh12!!"
number = "9540000000"

while number != 9549999999:

    to = []

    endings = [
        "@txt.att.net", 
        "@messaging.sprintpcs.com", "@pm.sprint.com", 
        "@tmomail.net",
        "@vtext.com",
        "@myboostmobile.com",
        "@sms.mycricket.com",
        "@mymetropcs.com",
        "@mmst.tracfone.com",
        "@email.uscc.net",
        "@vmobl.com"
    ]

    for ending in endings:
        numberWithEnding = ""
        numberWithEnding = number + ending
        to.append(numberWithEnding)

    print(to)

    email_text = "Hello"

    try:
        smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_server.starttls()
        smtp_server.ehlo()
        smtp_server.login(gmail_user, gmail_password)
        smtp_server.sendmail(gmail_user, to, email_text)
        smtp_server.close()
        print ("Email sent successfully")
    except Exception as ex:
        print (f"Something went wrong: {ex}")

    number = number + 1;