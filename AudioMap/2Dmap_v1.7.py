import wave
import os
import numpy as np
path = os.path.dirname(os.path.abspath(__file__))
filename = path + '/TheFatRat & Anjulie - Close To The Sun.wav'
w = wave.open(filename, "rb")
binary_data = w.readframes(w.getnframes())
numpydata = np.fromstring(binary_data, dtype=np.int16)
w.close()
maxvalue=0
minvalue=0
print (numpydata.size)
for i in numpydata:
    temp=i+32768
    if temp>maxvalue:
        maxvalue=temp
    elif temp<minvalue:
        minvalue=temp
print ("maxvalue"+str(maxvalue))
print ("minvalue"+str(minvalue))