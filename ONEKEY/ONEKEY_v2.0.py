import hashlib

default_algorthm=[4,6,5,3,2,8,7,9,1,0]

def blend(element_1,element_2,blend_algorithm=default_algorithm):
    result=""
    if len(element_1)>len(element_2):
        temp=element_1
        element_1=element_2
        element_2=temp
    for i in range(0,len(element_1)):
        
    return result

def string_to_list():
    


parent_key=""
key_pattern=""
with open('magickey.txt', 'r') as file:
    parent_key+=file.read().replace('\n', ' ')
print(parent_key)
s=hashlib.sha512()
website=input("website name:")
finalkey=blend(parent_key,website)
s.update(finalkey.encode("utf-8"))
hex_result=str(s.hexdigest())
dec_result=int(hex_result,16)
print(dec_result);

