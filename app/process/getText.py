import speech_recognition as sr
from app.models.audio import Audio 

def get_text(file: Audio, path):
   r = sr.Recognizer()
   if file.type == 'audio/x-wav':
      file_audio = sr.AudioFile(path+file.name+file.extension)
      with file_audio as source:
         audio_text = r.record(source)
         file.text = r.recognize_google(audio_text,language='pt-BR')
   else: 
      file.text = 'Áudio não pode ser transcrito'
   
   return file