import wave

#Audio file formates
#.mp3
#.flac
#.wav

# audio signal parameters
# -number of channels
# -sample width
# -framerate/samplerate
# - number of frames
# -values of a frame

obj=wave.open("sound1.wav","rb")
print("Number of channels",obj.getnchannels())
print(f"sample width {obj.getsampwidth()}")
print(f"frame rate -: {obj.getframerate()}")
print(f"number of frames : {obj.getnframes()}")
print (f"parameters : {obj.getnframes()}")

#CHANNELS-> 1-mono,2-sterio-> audio is coming from two different direction
#sample width :- no of bytes in sample
#frame rate : number of sample for each second
#number of frames : no of frames
#value of frame : 

t_audio=obj.getnframes()/obj.getframerate()
print(int(t_audio))

#total frames

frames=obj.readframes(-1)
print(type(frames),type(frames[0]))
print(len(frames))

obj.close()

obj_new=wave.open("new_audio.wav","wb")
obj_new.setnchannels(2)
obj_new.setsampwidth(2)
obj_new.setframerate(8100)
obj_new.writeframes(frames)
obj_new.close()
