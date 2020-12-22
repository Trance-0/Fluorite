import hashlib

d=["A","a","B","b","C","c","D","d","E","e","F","f","G","g","H","h","I","i","J","j","K","k","L","l","M","m","N","n","O","o","P","p","Q","q","R","r","S","s","T","t","U","u","V","v","W","w","X","x","Y","y","Z","z","1","2","3","4","5","6","7","8","9","0","-"," "]
def dec_to_all(data,add):
    b=[]
    while True:
        s=data//add#商
        y=data%add#余数
        b=b+[y]
        if s==0:
            break
        data=s
    b.reverse()
    for i in range(0,16):
        print(d[b[i]],end='')


magickey=""
with open('magickey.txt', 'r') as file:
    magickey+=file.read().replace('\n', ' ')
print(magickey)
s=hashlib.sha512()
website=input("website name:")
finalkey=website+magickey
s.update(finalkey.encode("utf-8"))
hexd=str(s.hexdigest())
decd=int(hexd,16)
dec_to_all(decd,64)