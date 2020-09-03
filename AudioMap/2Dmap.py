import warnings
warnings.simplefilter("ignore", DeprecationWarning)#防止报警告
import pyaudio
import wave
import cv2 as cv
import os

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

def convert_to_color(number):
    result=[]
    r=number//32//32
    g=(number-r*32**2)//32
    b=number%32
    result.append(r*4)
    result.append(g*4)
    result.append(b*4)
    return result

CHUNK = 16384#我把它理解为缓冲流

path = os.path.dirname(os.path.abspath(__file__))
filename = path + '/TheFatRat & Anjulie - Close To The Sun.wav'
# filename = path + '/Lesson17.mp3'
wf = wave.open(filename, 'rb')#以只读的方式打开"1qom8-vi8uq.wav"文件

#创建播放器
p = pyaudio.PyAudio()
#打开数据流  output=True表示音频输出
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),#设置声道数
                rate=wf.getframerate(),#设置流的频率
                output=True)


data = wf.readframes(CHUNK)#音频数据初始化
status=True
count=16#设置间隔区
imageWidth=32766//count+1
maxcount=0
mincount=0
img = np.zeros([1000,imageWidth,3])
index=0
while data != '' and status:#直到音频放完
    height=[]
    # elapsedtime=0

    stream.write(data)#播放缓冲流的音频
    data = wf.readframes(CHUNK)#更新data
    numpydata = np.fromstring(data, dtype=np.int16)#把data由字符串以十六进制的方式转变为数组
    # print(len(numpydata))
    # for n in range(0,numpydata.size,count):#从频域中的2048个数据中没隔count个数据中选取一条
    #     hight=abs(int(numpydata[n]//1000))#对这么多数据取整和绝对值
    #     height.append(hight)

    pitch=0
    for n in range(0,numpydata.size,count):#从频域中的2048个数据中没隔count个数据中选取一条
        hight=abs(numpydata[n])
        if hight>maxcount:
            maxcount=hight
        if hight<mincount:
            mincount=hight
        height.append(hight)
        color=convert_to_color(hight)
        img[index,pitch,0]=color[0]
        img[index,pitch,1]=color[1]
        img[index,pitch,2]=color[2]
        pitch+=1
    # print (len(height))
    # print("maxcount="+str(maxcount))
    # print("mincount="+str(mincount))
    index+=1
    cv.imshow("image", img)
    if cv.waitKey(1) == ord('q'):
        break

stream.stop_stream()
stream.close()
#关闭流
p.terminate()