import moviepy.editor as mp
import speech_recognition as sr
import moviepy.editor as mp
from pydub import AudioSegment
import os
import sys

# colocar o diretório que está o seu vídeo na variável path 
if 1 > 2:
   path = "./audios/exemplo.mp4" 
   nome = os.path.basename(path)

   # convert mp4 paramp3

   clip = mp.VideoFileClip(path).subclip()
   clip.audio.write_audiofile("./intermediario.mp3")
   r = sr.Recognizer()
   src=(r"./intermediario.mp3")

   # convert mp3 file to wav
   sound = AudioSegment.from_mp3(src)
   sound.export("./intermediario.wav", format="wav")

   file_audio = sr.AudioFile("./intermediario.wav")

file_audio = sr.AudioFile("./audios/WhatsApp-Ptt-2022-09-25-at-15.49.44.wav")
# use the audio file as the audio source

r = sr.Recognizer()
with file_audio as source:
   audio_text = r.record(source)
   text = r.recognize_google(audio_text,language='pt-BR')
arq = open('transcricao.txt','w')
arq.write(text)
arq.close()
print(text)