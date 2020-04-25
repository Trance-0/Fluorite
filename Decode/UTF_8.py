import chardet

def utf_8(inputs,sign):
    l=inputs.split(sign)
    i=[]
    for k in range(len(l)-1):
        i.append(k)
        i.append('\\u')
    i=''.join(i)
    print(i)
    result = i.encode('utf-8').decode('unicode_escape')
    return result

print('Input the text that you need to decode.')
c=input()
print('Input the signal that you need to decode.')
d=input()
print(utf_8(c,d))