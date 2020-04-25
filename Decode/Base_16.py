import base64

def base(inputs):
    result = base64.b16decode(bytes(inputs.encode('utf-8'))).decode('utf-8')
    return result

print('Input the text that you need to decode.')
c=input()
print(base(c))