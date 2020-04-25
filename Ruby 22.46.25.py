import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import math
from matplotlib.widgets import Slider

import warnings
warnings.simplefilter("ignore", DeprecationWarning)#防止报警告
import pyaudio
import wave

import numpy as np


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
fig = plt.figure()
ax = plt.axes()
ax.set_xlim([0, 1024])
ax.set_ylim([5, -5])
while data != '':#直到音频放完

    stream.write(data)#播放缓冲流的音频
    data = wf.readframes(CHUNK)#更新data
    numpydata = np.fromstring(data, dtype=np.int)
    count=1#设置间隔区
    for n in range(numpydata.size):#从频域中的2048个数据中没隔count个数据中选取一条
        magic(n*count)#画矩形

    pygame.display.update()#更新屏幕

stream.stop_stream()
stream.close()
#关闭流
p.terminate()

def magic(smu,ssigma);
# Initialize the figure
fig, ax = plt.subplots()
plt.subplots_adjust(bottom = 0.25)

# Initialize a Gaussian model
mu = 0
sigma = 1
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
l, = plt.plot(x, stats.norm.pdf(x, mu, sigma))

axmu = plt.axes([0.25, 0.1, 0.5, 0.03])
axsigma = plt.axes([0.25, 0.15, 0.5, 0.03])
smu = Slider(axmu, 'Mu', -5, 5, valinit = 0)
ssigma = Slider(axsigma, "Sigma", 0, 10, valinit = 1)

def update(val):
    global mu, sigma

    mu = smu.val
    sigma = ssigma.val
    l.set_ydata(stats.norm.pdf(x, mu, sigma))
    fig.cancas.draw_idle()

smu.on_changed(update)
ssigma.on_changed(update)

plt.show()