import moviepy.editor as mp
import speech_recognition as sr
import moviepy.editor as mp
from pydub import AudioSegment
import os
from app.extraction.getFiles import get_all_files
from app.database.database import insert_audio, get_all_audio
from app.process.getText import get_text

path = "./audios/"

      
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
