import os
import telebot
from time import sleep
from telebot import types
from threading import Thread
from subprocess import PIPE, Popen
from configparser import ConfigParser

cfg = ConfigParser()
cfg.read("config.cfg")
id = cfg.get("paladin","id")
tts = int(cfg.get("paladin","tts"))
token = cfg.get("paladin","token")
file_send = cfg.get("paladin","file")
if not os.path.isfile(file_send):
    with open(file_send,"w") as f:pass
welcome = cfg.get("paladin","welcome")

bot = telebot.TeleBot(token)

def get_status(id,service):
    data = {}
    for i in service:
        with Popen(f'sudo systemctl -l status {i}', stdout=PIPE, stderr=PIPE, shell=True) as process:
            output = process.communicate()[0].decode("utf-8")
            data[i] = [output.split("Active: ")[1].split("\n")[0].strip(),output] if "Active: " in output else ['error',output]
    with open(file_send,"r") as f: s = f.read()
    if len(s)>1: data["file"] = [s,""]
    with open(file_send,"w") as f:pass
    return data

def restart(id,service):
    for i in service: os.system(f"sudo systemctl restart {i}")
    get_str_status(id,service)

def stop(id,service):
    for i in service: os.system(f"sudo systemctl stop {i}")
    get_str_status(id,service)

def get_str_status_error(id,service):
    data = get_status(id,service)
    markup = types.InlineKeyboardMarkup()
    serv =[i for i in data if data[i][0][:6]!="active"]
    for i in operations:
        markup.row(types.InlineKeyboardButton(f"{i}",callback_data=f"{i} {' '.join([i for i in serv if i!='file'])}"))
    message = '\n'.join([f'{i}:{data[i][0]}' for i in serv])
    if message:
        if (len([i for i in serv if i!='file'])>0):
            bot.send_message(id, message, disable_notification=True, reply_markup=markup)
        else:
             bot.send_message(id, message)
def get_str_status(id,service):
    data = get_status(id,service)
    send(id, '\n\n'.join([f'{i}:{data[i][0]}\n{data[i][1]}' for i in data]))

def status_updater(id,service):
    while True:
        get_str_status_error(id,service)
        sleep(tts)

service = ["flask","techcard","sheduller","redis","nginx","paladin",]
operations = {"status":get_str_status,"restart":restart,"stop":stop}

def send(id,data):
    if len(data)<4095:
        if len(data)!=0:bot.send_message(id, data)
    else:
        data = data.split("\n") if "\n" in data else [data]
        repack = []
        patch = ""
        for i in data:
            if len(patch+i)<4095: patch+=i
            elif len(patch)>0:
                repack.append(patch)
                patch = ""
        for i in repack:
            bot.send_message(id, i)

th = Thread(target = status_updater,args=(id,service,))
th.start()

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if " " in call.data:
            op, service = call.data.split(" ")[0],call.data.split(" ")[1:]
            operations[op](id,service)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Принято в работу!",
        reply_markup=None)
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
            text="Готово...")

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(*[types.KeyboardButton(f"/{i}") for i in operations])
    if int(message.chat.id)==int(id):
        bot.send_message(message.chat.id, welcome, reply_markup=markup)

   
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if int(message.chat.id)==int(id):
        if message.text[1:] in operations:
            markup = types.InlineKeyboardMarkup()
            for i in service:
                markup.row(types.InlineKeyboardButton(f"{i}",callback_data=f"{message.text[1:]} {i}"))
            bot.send_message(id,message.text, disable_notification=True, reply_markup=markup)
        else:
            bot.send_message(message.chat.id, "Undefined command")

bot.polling(none_stop=True, interval=0)
