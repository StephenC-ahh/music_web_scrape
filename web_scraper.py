import urllib3
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
    print('Extrating Udiscover Music ReDiscovered Albums...')
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

import sys
print(content) 
original_stdout = sys.stdout
with open('filename.txt', 'w') as f:
    sys.stdout = f
    print(content)
    sys.stdout = original_stdout
