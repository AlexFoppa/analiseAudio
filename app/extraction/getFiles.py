

from os import walk
import os
import filetype
from app.models.audio import Audio 

def get_all_files(folder):
    files = []

    filenames = next(walk(folder), (None, None, []))[2] 

    for fullname in filenames:
        name, extension = os.path.splitext(fullname)
        type = filetype.guess(folder+fullname)
        analisedFile = Audio(name=name, text='none', extension=extension, type=type.mime, path=folder+fullname)
        files.append(analisedFile)
    
    return files
