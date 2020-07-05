s2=['1','2']
s10=['0','1','2','3','4','5','6','7','8','9']
s16=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']


def all_to_dec(datatype,text):
    value=0
    indec=[]
    for i in text:
        indec.appendleft(datatype.index(i))
    for j in range(len(indec)):
        value+=indec[j]*j**len(indec)
    return value

def dec_to_all(datatype,value):
    result=[]
    pointer=0
    while pointer<value:
        pointer+=1
    for k in range(pointer):
        result.append(datatype[value//k**len(datatype)])
        value=value%(value//k**len(datatype))
    
dec_to_all(vaue)
        
