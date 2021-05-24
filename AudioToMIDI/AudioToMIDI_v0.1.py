import wave
import numpy
from pyaudio import PyAudio
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import math
from os import path
import os
from pydub import AudioSegment
 
path = os.path.dirname(os.path.abspath(__file__))
src = path + '/RolanTin - SeaSand.mp3'
dst = path + "/test.wav"

# convert wav to mp3                                                            
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")

path = os.path.dirname(os.path.abspath(__file__))
filename = path + '/test.wav'

wf = wave.open(filename, 'rb')#以只读的方式打开"1qom8-vi8uq.wav"文件

# 创建PyAudio对象
p = PyAudio()
stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),
                channels = wf.getnchannels(),
                rate = wf.getframerate(),
                output = True)
nframes = wf.getnframes()
print("nframes",nframes)
framerate = wf.getframerate()
 
# 读取完整的帧数据到str_data中，这是一个string类型的数据
str_data = wf.readframes(nframes)
wf.close()
 
# 将波形数据转换成数组
wave_data = numpy.fromstring(str_data, dtype=numpy.short)
# 将wave_data数组改为2列，行数自动匹配
wave_data.shape = -1,2
# 将数组转置
wave_data = wave_data.T
print("wave_data shape",wave_data.shape)
 
#读取片段数
nsegments=int(wave_data.shape[1]/framerate)
print("nsegments",nsegments)
 
 
 
def freqs():
    # 采样点数，修改采样点数和起始位置进行不同位置和长度的音频波形分析
    N = 44100
    
    df = framerate/(N-1)  # 分辨率
    freq = [df*n for n in range(0, N)]  # N个元素
    print("freq",freq)
    
    #片段频率数组
    seg_freqs=[]
    
    #钢琴键序号组
    key_nums=[]
    
    for i in range(nsegments):
    
        start = i*N  # 开始采样位置
        end=start+N        
        
        wave_data2 = wave_data[0][start:end]
        c = numpy.fft.fft(wave_data2)*2/N
        # 常规显示采样频率一半的频谱
        d = int(len(c)/2)
        # 仅显示频率在4000以下的频谱
        while freq[d] > 4000:
            d -= 10
        
        vf_dict=dict(zip(abs(c[:d-1]),freq[:d-1]))
        
        max_v=max(abs(c[:d-1]))
        max_f=vf_dict[max_v]  
              
        seg_freqs.append(max_f)
        print("max f:v",max_f,max_v)
        
        #计算最接近的钢琴键号
        key_num_nearest=round(math.log(max_f/27.5,1.059))+1
        key_nums.append(key_num_nearest)
        
    
    print("key_nums",key_nums)
    
    #可视化
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.figure(figsize=(20,20), dpi=90)
 
    xs=range(len(seg_freqs))
    ys=seg_freqs     
    
    #频谱
    ax1 = plt.subplot(211)
    ax1.plot(xs, ys,color="blue") 
    ax1.set_title("频率时序谱")
    ax1.set_xlabel("时间 S")
    ax1.set_ylabel("时点主频率")
 
    xs1=range(len(key_nums))
    ys1=key_nums
    
    #钢琴键谱
    ax2 = plt.subplot(212)
    ax2.scatter(xs1, ys1,color="red")    
    ax2.set_xticks(xs1)
    ax2.set_yticks(range(min(ys1)-1,max(ys1)+1))
    ax2.set_title("钢琴键时序谱")
    ax2.set_xlabel("时间 S")
    ax2.set_ylabel("时点对应钢琴键序号")
    ax2.grid()
    
    plt.show()
    
def main():
    freqs()
 
 
if __name__ == '__main__':
    main()

# ————————————————
# 版权声明：本文为CSDN博主「一粒马豆」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/MAILLIBIN/article/details/113926161