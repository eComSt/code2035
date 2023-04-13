import random
import requests
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType 
from bs4 import BeautifulSoup
from datetime import datetime
from wiki import get_wiki_article

url = "http://www.cbr.ru/scripts/XML_daily.asp?"
today = datetime.today()
today = today.strftime("%d/%m/%Y")
payload = {"date_req": today}
response = requests.get(url, params=payload)
xml = BeautifulSoup(response.content, features="xml")
def get_course(currency):
    for c in xml.find_all("Valute"):
        currency_name = c.Name.text.lower()
        if currency_name == currency:
            return currency.Nominal.text, currency.Value.text
    return None, None

with open("key_vk") as file:
    token = file.read()
    
while True:
    try:
        vk_session = vk_api.VkApi(token=token)
        vk = vk_session.get_api()
        longpoll = VkLongPoll(vk_session)

        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                msg = event.text.lower()
                print(msg)
                user_id = event.user_id
                random_id = random.randint(1,10**10)
                if msg.startswith('-k'):
                    course = msg[2:]
                    print(course)
                    nominal, value = get_course(course)
                    if nominal:
                        responce = f"{value} rub for {nominal} {course}"
                    else: responce ="No such valute"
                elif msg.startswith("-w"):
                    article = msg[2:]
                    responce = get_wiki_article(article)
                else:
                    responce = "unknown message"
                vk.messages.send(user_id=user_id,random_id=random_id,message = response)
    except:pass