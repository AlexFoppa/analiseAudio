

from os import walk
import os
import filetype
from app.models.audio import Audio 

def get_all_files(folder):
    path = folder
    files = []

    filenames = next(walk(path), (None, None, []))[2] 

    for fullname in filenames:
        name, extension = os.path.splitext(fullname)
        type = filetype.guess(path+fullname)
        analisedAudio = Audio(name=name, text='none', extension=extension, type=type.mime)
        files.append(analisedAudio)
    
    return files
