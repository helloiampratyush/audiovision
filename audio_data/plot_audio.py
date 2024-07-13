import wave
import numpy as np
import matplotlib.pyplot as plt

#open wav file
obj=wave.open("sound1.wav","rb")

sample_freq=obj.getframerate()
n_samples=obj.getnframes()
signal_wave=obj.readframes(-1)

obj.close()

t_audio=n_samples/sample_freq

print(t_audio)

signal_array=np.frombuffer(buffer=signal_wave,dtype=np.int16)

times=np.linspace(0,t_audio,num=n_samples*2)

print(signal_array,times)

plt.figure(figsize=(10,7))
plt.plot(times,signal_array)
plt.title("audio_signal")
plt.ylabel("Signal wave")
plt.xlabel("time")
plt.show()
