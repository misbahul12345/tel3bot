import requests
import time
import schedule
import json
import hashlib
def send_messege(text_m):                                             api = "5051071517:AAG4Q5F9Yb5HGqhzEzRVcsALyEwxdBSZyPg"
    id_client ="1615808371"
    send_chat = "https://api.telegram.org/bot"+api+"/sendMessage?chat_id="+id_client+"/parse_mode=Markdown&text="+text_m
    response = requests.get(send_chat)
    return response.json()

for a in range(1,10000):
    if (a > 0):
        send_messege("hai fuad,kamu sange ga?")



~
