from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

print("This ")
have_key=input("do you have any public key?")
keyPair = RSA.generate(3072)
 
pubKey = keyPair.publickey()
print(f"Public key:  (n={hex(pubKey.n)}, e={hex(pubKey.e)})")
pubKeyPEM = pubKey.exportKey()
print(pubKeyPEM.decode('ascii'))
 
print(f"Private key: (n={hex(pubKey.n)}, d={hex(keyPair.d)})")
privKeyPEM = keyPair.exportKey()
print(privKeyPEM.decode('ascii'))
 
#encryption
msg = 'A message for encryption'
encryptor = PKCS1_OAEP.new(pubKey)
encrypted = encryptor.encrypt(msg.encode())
encrypted_hex=binascii.hexlify(encrypted)
print("Encrypted:",encrypted_hex )
bytes_object = bytes.fromhex(encrypted_hex.decode('utf-8'))
ascii_string = bytes_object.decode("ascii")
print("Magic convert:",ascii_string)