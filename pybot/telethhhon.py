from telethon import TelegramClient, events
import requests
from bs4 import BeautifulSoup
import time

api_id = 21028045
api_hash = 'b44b3120630e30c10cce626175c951ad'

class NameChannel:
    def __init__(self, link):
        self.link = link

    def response(self):
        response_chanell = requests.get(self.link)
        soup = BeautifulSoup(response_chanell.text, 'html.parser')
        title = soup.find('div', 'tgme_page_title')
        return title.text

client = TelegramClient(session='session_name', api_id=api_id, api_hash=api_hash)
client.start()

@client.on(events.NewMessage(chats=('tgroup')))
async def function(event):
    message_date = event.date # 1 COLUMN DATE
    print(message_date)
    message_text = event.message.text
    print(message_text)
    print('-------')
    name_channel = message_text.split('**')[1] # ссылка для паблика
    print(name_channel)
    link_chanell = 'https://t.me/+'+name_channel # 3 column ССЫЛКА НА ПАБЛИК
    print(link_chanell) # работает

    link_chanell_class = NameChannel(str(link_chanell))
    time.sleep(4)
    try:
        t = link_chanell_class.response()
        print(t)
    except Exception as ex:
        print('Не удалось обработать название канала')
    link_pablic = (message_text.split('**')[2]).split('\n')[0]
    print(link_pablic) # ссыклка на пост


if __name__ == '__main__':

    client.run_until_disconnected()