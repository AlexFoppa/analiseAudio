import speech_recognition as sr
from app.models.audio import Audio
from app.process.conversions import try_conversion 

def get_text(file: Audio):
   if file.type == 'audio/x-wav':
      file.text = transcription(file.path)
   else:
      temp_file = try_conversion(file)
      if temp_file == False:
        file.text = 'Áudio não pode ser transcrito'
      else:
        file.text = transcription(temp_file)
   return file

def transcription(path):
    r = sr.Recognizer()
    file_audio = sr.AudioFile(path)
    with file_audio as source:
        audio_text = r.record(source)
        text = r.recognize_google(audio_text,language='pt-BR')
    return text