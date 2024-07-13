from pydub import AudioSegment

audio=AudioSegment.from_wav("sound1.wav")

#increase the value by 6 db

audio=audio+6  #it increases db if increase to much noise will come

audio=audio*2 # it increase duration

audio=audio.fade_in(2000)

audio.export("mashup.mp3",format="mp3")

audio2=AudioSegment.from_mp3("mashup.mp3")

print("progressed")