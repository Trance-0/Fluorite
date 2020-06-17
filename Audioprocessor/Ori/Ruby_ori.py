import warnings
warnings.simplefilter("ignore", DeprecationWarning)#防止报警告
import pyaudio
import wave

import numpy as np
import pygame
from pygame.locals import *


CHUNK = 1024#我把它理解为缓冲流


wf = wave.open("TheFatRat & Anjulie - Close To The Sun.wav", 'rb')#以只读的方式打开"1qom8-vi8uq.wav"文件

#创建播放器
p = pyaudio.PyAudio()
#打开数据流  output=True表示音频输出
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),#设置声道数
                rate=wf.getframerate(),#设置流的频率
                output=True)


data = wf.readframes(CHUNK)#音频数据初始化
pygame.init()#pygame初始化

pygame.display.set_caption('实时频域')#设置窗口标题
screen = pygame.display.set_mode((850, 400), 0, 32)#窗口大小为(850,400)
while data != '':#直到音频放完

    stream.write(data)#播放缓冲流的音频
    data = wf.readframes(CHUNK)#更新data
    numpydata = np.fromstring(data, dtype=np.int16)#把data由字符串以十六进制的方式转变为数组
    transforamed=np.real(np.fft.fft(numpydata))#傅里叶变换获取实数部分

    screen.fill((0, 0, 0))#清空屏幕
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()       #这段代码防止无响应
    count=50#设置间隔区
    for n in range(0,transforamed.size,count):#从频域中的2048个数据中没隔count个数据中选取一条
        hight=abs(int(transforamed[n]/10000))#对这么多数据取整和绝对值

        pygame.draw.rect(screen,(255,255,255),Rect((20*n/count,400),(20,-hight)))#画矩形
    print (hight)
    pygame.display.update()#更新屏幕

stream.stop_stream()
stream.close()
#关闭流
p.terminate()