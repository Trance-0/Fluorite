import base64

def base(inputs):
    result = base64.b16encode(bytes(inputs.encode('utf-8'))).decode('utf-8')
    return result

print('Input the text that you need to encode.')
c=input()
print(base(c))