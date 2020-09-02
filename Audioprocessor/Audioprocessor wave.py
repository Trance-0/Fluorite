import warnings
warnings.simplefilter("ignore", DeprecationWarning)#防止报警告
import pyaudio
import wave
import os

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

CHUNK = 8192#我把它理解为缓冲流

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


while data != '':#直到音频放完
    height=[]
    # elapsedtime=0
    fig = plt.figure()
    ax = plt.subplot(111, projection='polar')

    ax.set_ylim(0,50)
    stream.write(data)#播放缓冲流的音频
    data = wf.readframes(CHUNK)#更新data
    numpydata = np.fromstring(data, dtype=np.int16)#把data由字符串以十六进制的方式转变为数组
    # print(len(numpydata))
    count=1024#设置间隔区
    # for n in range(0,numpydata.size,count):#从频域中的2048个数据中没隔count个数据中选取一条
    #     hight=abs(int(numpydata[n]//1000))#对这么多数据取整和绝对值
    #     height.append(hight)

    for n in range(0,numpydata.size,count):#从频域中的2048个数据中没隔count个数据中选取一条
        hight=abs(int(numpydata[n]//1000))#对这么多数据取整和绝对值
        height.append(hight)
        # colors = plt.cm.viridis(hight / 10.)


    # print(height)
    # ax3d.plot_trisurf(X, Y, Z,cmap="hsv")

    theta = np.linspace(0.0, 2 * np.pi, len(height), endpoint=False)

    width=2*np.pi/len(height)
    # colors = plt.cm.viridis(height / 10.)
    # print(width)
    h=np.array(height)
    ax.bar(theta,h, width=width, bottom=0,alpha=0.5)
    # plt.draw()
    # elapsedtime+=1;
    # plt.show()
    ax.axes.xaxis.set_visible(False)
    ax.axes.yaxis.set_visible(False)
    ax.axes.xaxis.set_ticks([])
    ax.axes.yaxis.set_ticks([])
    plt.pause(0.01)
    
    plt.close()
    # fig.canvas.draw()

stream.stop_stream()
stream.close()
#关闭流
p.terminate()