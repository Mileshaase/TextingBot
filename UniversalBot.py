import smtplib

#email must be gmail and have less secure sign on turned on
gmail_user = input("Enter your email: ")
gmail_password = input("Enter your password: ") 

number = input("Enter the number you intend to text: ")

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

email_text = f"""
    #Here is where you write the body to your message
"""

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
