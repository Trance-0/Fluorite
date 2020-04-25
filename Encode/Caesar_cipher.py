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

def Caesar_cipher(a,b,c):
        d=dict_maker(a,b)
        c=c.lower()#abc dictionary only
        c=list(c)
        e=[]
        for i in c:
            if i in d:
                e.append(d[i])
            else:
                e.append(i)
        e=''.join(e)
        return e
                
abc=deque(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
asc=deque()
dictionary=abc
print('Input the text that you need to encode.')
c=input()
print('Input the move that you need to encode.')
b=int(input())
print(Caesar_cipher(dictionary,b,c))

