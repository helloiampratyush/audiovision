import pyaudio
import wave
from tqdm.auto import tqdm

#hyper parameter

frames_per_buffer=3200
format=pyaudio.paInt16
channels=1
rate=16000

p=pyaudio.PyAudio()

stream=p.open(
    format=format,
    channels=channels,
    rate=rate,
    input=True,
    frames_per_buffer=frames_per_buffer
)

print("start recording ! ...")

time=5

frames=[]

for i in range(0,int(rate/frames_per_buffer*time)):

    data=stream.read(frames_per_buffer)

    frames.append(data)

stream.stop_stream()
stream.close()
p.terminate()


obj=wave.open("output.wav","wb")

obj.setnchannels(channels)
obj.setsampwidth(p.get_sample_size(format=format))
obj.setframerate(rate)
obj.writeframes(b"".join(frames))

obj.close()