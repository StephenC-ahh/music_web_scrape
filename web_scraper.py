from xmlrpc.client import SERVER_ERROR
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from urllib import response
from urllib3 import PoolManager
import requests #http requests
from bs4 import BeautifulSoup #webscraping
#Send the mail
import smtplib
# email body
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# system date and time manipulation
import datetime

now = datetime.datetime.now()

# email content placeholder

content = ''

def extract_news(url):
    print('Extracting Udiscover Music ReDiscovered Albums...')
    cnt = ''
    cnt +=('<b>Udiscover Rediscovered Albums:<b>\n'+'<br>'*50+'<br>')
    response = requests.get(url, verify=False)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    for i, tag in enumerate(soup.find_all('div', attrs={'class':'mvp-blog-story-text', 'h2':''})):
        cnt += ((str(i+1)+' :: '+tag.text + "\n" + '<br>') if tag.text!='More' else '')
        # print(tag.pretify) #find all('span', attrs={'class':'sitestr'})
    return(cnt)

cnt = extract_news('https://www.udiscovermusic.com/genre/rediscovered-albums/')
content += cnt
content += ('<br>------<br>')
content += ('<br><br>End of Message')

print('Composing Email...')

SERVER = 'smtp.gmail.com' # your smtp server
PORT = 587 #your port number
FROM = '' #your email id
TO = '' # recipient email, can be a list
PASS = input('Enter your Email password') #your email id password'

msg = MIMEMultipart()

msg['Subject'] = 'UDiscover Music Rediscovered Albums' + ' ' + ' ' + str(now.day) + '_' + str(now.month) + '_' + str(now.year)

msg['From'] = FROM

msg['To'] = TO

msg.attach(MIMEText(content, 'html'))

print('Intiating Server...')

server = smtplib.SMTP(SERVER, PORT)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.login(FROM)
server.send_message(TO)

print('Email Sent')