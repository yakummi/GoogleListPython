import requests
from bs4 import BeautifulSoup

response = requests.get('https://t.me/+sOj9iDAtUkMyYWQy')
soup = BeautifulSoup(response.text, 'html.parser')
title = soup.find('div', 'tgme_page_title')
print(title.text)