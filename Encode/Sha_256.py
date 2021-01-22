import hashlib
import os 

dir_path = os.path.dirname(os.path.realpath(__file__))
f = open(dir_path+"/shainput.txt", "r")
h = hashlib.sha512(f.read().encode('utf-8')).hexdigest()

print(h);