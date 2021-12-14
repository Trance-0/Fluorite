from random import randint
# try to get an random private key on ethernet, and use this wallet to get ETH!
rand_hex_str = hex(randint(0, 16**64))
print(rand_hex_str)