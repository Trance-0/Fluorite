import warnings
warnings.simplefilter("ignore", DeprecationWarning)#防止报警告
import pyaudio
import wave

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

CHUNK = 512#我把它理解为缓冲流


wf = wave.open("TheFatRat & Anjulie - Close To The Sun.wav", 'rb')#以只读的方式打开"1qom8-vi8uq.wav"文件

#创建播放器
p = pyaudio.PyAudio()
#打开数据流  output=True表示音频输出
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),#设置声道数
                rate=wf.getframerate(),#设置流的频率
                output=True)


data = wf.readframes(CHUNK)#音频数据初始化
elapsedtime=0

X=[]
Y=[]
Z=[]
ax= plt.axes

while data != '':#直到音频放完


    
    stream.write(data)#播放缓冲流的音频
    data = wf.readframes(CHUNK)#更新data
    numpydata = np.fromstring(data, dtype=np.int16)#把data由字符串以十六进制的方式转变为数组

    # print(numpydata)
    transforamed=np.real(np.fft.fft(numpydata))#傅里叶变换获取实数部分
    
    count=50#设置间隔区
    for n in range(0,transforamed.size,count):#从频域中的2048个数据中没隔count个数据中选取一条
        Y.append(abs(int(transforamed[n]/10000)))#对这么多数据取整和绝对值


    for i in range(len(Y)):
        X.append(i)
        Z.append(elapsedtime)

    print(transforamed)
    # ax3d.plot_trisurf(X, Y, Z,cmap="hsv")
    ax3d.scatter( X, Y, Z,color="blue")

    elapsedtime+=1;
    plt.show()
    plt.pause(0.1)
    plt.clf()

stream.stop_stream()
stream.close()
#关闭流
p.terminate()