import wave
import os
path = os.path.dirname(os.path.abspath(__file__))
filename = path + '/TheFatRat & Anjulie - Close To The Sun.wav'
w = wave.open(filename, "rb")
binary_data = w.readframes(w.getnframes())
w.close()
print(binary_data)