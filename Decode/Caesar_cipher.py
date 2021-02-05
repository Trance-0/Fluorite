from collections import deque
def move(a,b):
    for i in range(b):
        temp=a.popleft()
        a.append(temp)
    return a

def dict_maker(a,b):
    c=a.copy()
    move(c,b)
    d=dict(zip(a,c))
    return d

def Caesar_cipher(a,b):
    for k in range(len(a)):
        a=a.copy()
        c=b
        d=dict_maker(a,k)
        # c=c.lower()#abc dictionary only
        c=list(c)
        e=[]
        for i in c:
            if i in d:
                e.append(d[i])
            else:
                e.append(i)
        e=''.join(e)
        print('if a = ',len(a)-k,' : ',e)
                
abc=deque(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
hexset=deque(['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E'])
asc=deque(['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
dictionary=hexset
print('Input the text that you need to decode.')
b=input()
Caesar_cipher(dictionary,b)

