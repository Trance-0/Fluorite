def fence(string):
    e = string
    elen = len(e)  # 计算字符串长度
    field = []

    for i in range(2, elen):  # 做一个循环，从2开始到数字elen（字符串长度）
        if elen % i == 0:  # 计算那些数字能整除字符串长度
            field.append(i)  # 将能整出的数字加入到field里面

    for f in field:
        b = elen // f  # 用字符串实际长度除以上面计算出能整出的数字f
        result = {x: '' for x in range(b)}
        for i in range(elen):  # 字符串有多少位，就循环多少次
            a = i % b
            result.update({a: result[a] + e[i]})  # 字符串截断，并更新数据
        d = ''
        for i in range(b):
            d += result[i]
        return('If fence = '+str(f)+' : '+d+'\n')  # 输出结果，并开始下一个循环

print('Input the text that you need to decode.')
a=input()
print(fence(a))