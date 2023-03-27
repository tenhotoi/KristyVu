# https://mailtrap.io/blog/python-send-email/
# Sending emails with Python via Gmail

import smtplib, ssl

port = 465  
password = input("your password")
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("my@gmail.com", password)

"""
# If you tend to simplicity, then you can use Yagmail, the dedicated Gmail/SMTP. It makes email sending really easy. Just compare the above examples with these several lines of code:
import yagmail

yag = yagmail.SMTP()
contents = [
    "This is the body, and here is just text http://somedomain/image.png",
    "You can find an audio file attached.", '/local/path/to/song.mp3'
]
yag.send('to@someone.com', 'subject', contents)
"""
