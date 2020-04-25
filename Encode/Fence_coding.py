def fence(string, space):
    key = 0
    result=[]
    while key < space:
        for i in range(0, len(string), space):
            if (i + key) < len(string):
                result.append(string[i + key])
        key = key + 1
    result=''.join(result)
    return result

print('Input the text that you need to encode.')
a=input()
print('Input the space of your code.')
b=int(input())
print(fence(a,b))

