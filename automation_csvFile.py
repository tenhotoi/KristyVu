# https://zapier.com/blog/python-automation/
# 5. Read a CSV
import csv

#replace 'customers.csv' with your filename or path to file (i.e. /Desktop/folder/file.csv)

with open('customers.csv', newline='') as csvfile:
    # cust_reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    cust_reader = csv.reader(csvfile, delimiter=' ')

    for row in cust_reader:

        print(', '.join(row))

# 6. Modify a CSV
import csv


Row = ['James Smith', 'james@smith.com', 200000]

# Make sure 'customers.csv' is in your root directory, or provide path to open() method.
# pass in 'a' to append new row or 'w' to overwrite CSV file
with open('customers.csv', 'a', newline='') as csvfile:

    cust_writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

    cust_writer.writerow(Row)

# 7. Sending personalized emails to multiple people
import csv, smtplib, ssl

from datetime import date


today = date.today().strftime('%B %d, %Y')


message = '''Subject: Your evaluation


Hi {name}, the date of your Q1 evaluation is {date}. Your score is: {score}'''

from_address = 'YOUR EMAIL ADDRESS'

# You may need to create an app password for Gmail here: https://myaccount.google.com/apppasswords

password = input('Enter password: ')


context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:

    server.login(from_address, password)

    # use a customers.csv file with name, email, and score columns

    with open('customers.csv') as file:

        reader = csv.reader(file)

        for name, email, score in reader:

            server.sendmail(

                from_address,

                email,

                message.format(name=name,date=today, score=score),

            )