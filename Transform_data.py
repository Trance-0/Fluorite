
def s(number):
    s36=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    return s36[:number]


def all_to_dec(datatype,text):
    value=0
    indec=[]
    for i in text:
        indec.insert(0,datatype.index(i))
    for j in range(len(indec)):
        value+=indec[j]*(len(datatype)**j)
    # print(value)
    return value

def dec_to_all(datatype,value):
    result=""
    pointer=0
    while len(datatype)**(pointer+1)<=value:
        pointer+=1
    for k in range(pointer+1):
        result=result+(datatype[value//len(datatype)**(pointer-k)])
        if value>=len(datatype)**(pointer-k):
            value=value%((value//len(datatype)**(pointer-k))*len(datatype)**(pointer-k))
    # print(result)
    return result
    

def all_to_all (data,tran,resu):
    return dec_to_all(resu,all_to_dec(tran,data))

print(all_to_all("2b",s(16),s(10)))
