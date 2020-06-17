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




while data != '':#直到音频放完
    height=[]
    # elapsedtime=0
    fig = plt.figure()
    ax = plt.subplot(111, projection='polar')

    ax.set_ylim(0,70)
    stream.write(data)#播放缓冲流的音频
    data = wf.readframes(CHUNK)#更新data
    numpydata = np.fromstring(data, dtype=np.int16)#把data由字符串以十六进制的方式转变为数组
    transforamed=np.real(np.fft.fft(numpydata))#傅里叶变换获取实数部分


stream.stop_stream()
stream.close()
#关闭流
p.terminate()