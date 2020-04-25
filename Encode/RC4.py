# RC4的Python实现
def ini_S(R):
    '初始化状态向量S'
    S = [x for x in range(256)]
    j = 0
    # 打乱种子1
    for i in range(256):
        j = (j + S[i] + R[j]) % 256
        S[i], S[j] = S[j], S[i]
    # print(S)

    return S


def gen_R(key):
    '256个字节轮转填满'
    #按照指定的 encoding 将字符串转换为字节序列
    #UTF8 数字和字母占一个字节
    temp = list(bytes(key,"utf-8"))
    len_key = len(temp)
    #轮转填满
    R = [temp[i % len_key] for i in range(256)]
    # print(R)

    return R


def stream_k(S, length):
    '根据密文长度生成密钥流'
    j = 0
    Sh = []
    for i in range(length):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        h = (S[j] + S[i]) % 256
        # 这里的k就是当前生成密钥流中的一位
        k = S[h]
        Sh.append(k)
    return Sh


choose = input('1加密 2解密  : ')
key = input('输入密钥key:')
R = gen_R(key) # R是被轮转填满的密钥
S = ini_S(R)    # S是被打乱的1-256
if choose == '1':
    plaintext = input('输入要加密的内容:')
    ciphertext = ''
    Sh = stream_k(S, len(plaintext)) # 根据明文长度打乱S，生成准备异或的密钥
    for i in range(len(plaintext)):
        ciphertext = ciphertext + chr(Sh[i] ^ ord(plaintext[i]))
    text=ciphertext
    print('得到的密文是:', text)
if choose=='2':
    ciphertext = input('输入要解密的内容:')
    plaintext = ''
    Sh = stream_k(S, len(ciphertext))
    for i in range(len(ciphertext)):
        plaintext = plaintext + chr(ord(ciphertext[i]) ^ Sh[i])
    print('得到的内容是:', plaintext)
