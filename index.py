from app.extraction.getFiles import get_all_files
from app.database.database import insert_audio, get_all_audio
from app.process.getText import get_text

path = "./audios/"

files = get_all_files(path)

for file in files:
   get_text(file, path)
   insert_audio(file)

print(get_all_audio())
