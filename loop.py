#!/usr/bin/python3.5
import requests
from fake_useragent import UserAgent
from loremipsum import get_paragraph
import time
from random import randrange
ua = UserAgent()
headers = {'User-Agent': ua.chrome }
while True:
    sentence = get_paragraph(start_with_lorem=True)
    payload = {'cmd': 'set', 'key': 'messages', 'value' : sentence[0:100]}
    r = requests.get('http://10.0.10.42:80/guestbook.php', params=payload, headers=headers)
    s = requests.get('http://10.0.10.42:80/', headers=headers)
    print((r.url)[0:120])
    time.sleep(randrange(10))

