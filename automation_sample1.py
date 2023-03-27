# https://zapier.com/blog/python-automation/

# 1. Pull live traffic data
# pip or pip3 install requests
# Which one you use (pip or pip3) depends on the version of Python and the package manager pip you're using
"""
py -m pip install requests
Collecting requests
  Downloading requests-2.28.2-py3-none-any.whl (62 kB)
   ..........
"""
import requests


url_api = 'https://api.midway.tomtom.com/ranking/liveHourly/USA_los-angeles'

usa_req = requests.get(url_api)

usa_json = usa_req.json()


# Do something with the json response to prove it works. 

print(usa_json)

# 2. Compile data from a webpage
# pip or pip3 install beautifulsoup4
"""
py -m pip install beautifulsoup4
Collecting beautifulsoup4
  Downloading beautifulsoup4-4.11.2-py3-none-any.whl (129 kB)
     ---------------------------------------- 129.4/129.4 kB 1.9 MB/s eta 0:00:00
Collecting soupsieve>1.2
  Downloading soupsieve-2.4-py3-none-any.whl (37 kB)
Installing collected packages: soupsieve, beautifulsoup4
Successfully installed beautifulsoup4-4.11.2 soupsieve-2.4
"""
import requests

response = requests.get('https://www.bbc.com/news')

print(response.status_code)

from bs4 import BeautifulSoup                          

soup = BeautifulSoup(response.content, 'html.parser') 

print(soup)
print(soup.find_all('h2'))

# 3. Convert PDF to audio file
"""
The below script takes a PDF, removes spaces and lines that would impede Pyttsx3's ability to read the text naturally, and converts the PDF to an audio file. If you were to implement some web scraping script, you could also use PyPDF and Pyttsx3 to convert a webpage into an audio file.
"""
import pyttsx3,PyPDF2

#Replace file.pdf' with path to your PDF file (i.e. /Desktop/Contracts/file.pdf)

pdfreader = PyPDF2.PdfFileReader(open('file.pdf','rb'))

reader = pyttsx3.init()

for page in range(pdfreader.numPages):   

    text = pdfreader.getPage(page).extractText()

    legible_text = text.strip().replace('\n',' ')

    print(legible_text)

    reader.say(legible_text)

    reader.save_to_file(legible_text,'file.mp3')

    reader.runAndWait()

reader.stop()

# 4. Convert a JPG to a PNG
# pip or pip3 install Pillow
import os, sys

from PIL import Image


# Make sure original image ('test.png') is in root directory

images = ['test.png']


for infile in images:

    f, e = os.path.splitext(infile)

    outfile = f + '.jpg'

    if infile != outfile:

        try:

            with Image.open(infile) as image:

                in_rgb = image.convert('RGB')

                in_rgb.save(outfile, 'JPEG')

        except OSError:

            print('Conversion failed for', infile)

# 5. Read a CSV
import csv

#replace 'customers.csv' with your filename or path to file (i.e. /Desktop/folder/file.csv)


with open('customers.csv', newline='') as csvfile:

    cust_reader = csv.reader(csvfile, delimiter=' ', quotechar='|')

    for row in cust_reader:

        print(', '.join(row))

# 6. Modify a CSV
import csv


Row = ['James Smith', 'james@smith.com', 200000]


# Make sure 'customers.csv' is in your root directory, or provide path to open() method.

# pass in 'a' to append new row or 'w' to overwrite CSV file

with open('customers.csv', 'a', newline='') as csvfile:

    cust_writer = csv.writer(csvfile, delimiter=',',

                            quotechar='|', quoting=csv.QUOTE_MINIMAL)

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
# 8. Bulk uploading files to a cloud-based platform
# pip or pip3 install pydrive
from pydrive.auth import GoogleAuth

from pydrive.drive import GoogleDrive


google_auth = GoogleAuth()

drive_app = GoogleDrive(google_auth)


# Make sure files are in your root directory

upload_list = ['test.png', 'test.jpg']


for file_to_upload in upload_list:
    # Navigate to your desired Google Drive folder and grab custom ID from URL path

    file = drive_app.CreateFile({'parents': [{'id': 'FOLDER_ID_FROM_GOOGLE_DRIVE'}]})

    file.SetContentFile(file_to_upload)

    file.Upload()

# 9. Cleaning up your computer
import os, shutil

lis=[]

i=1

destinationdir='/Users/NAME/Desktop/Everything'

while os.path.exists(destinationdir):

    destinationdir+=str(i)

    i+=1

os.makedirs(destinationdir)


lis=os.listdir('/Users/NAME/Desktop')

for x in lis:

    print(x)

    if x == __file__:

        continue

    shutil.move(x,destinationdir)


