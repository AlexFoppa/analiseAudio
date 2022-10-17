

from importlib.metadata import metadata
from os import walk
import os
import filetype
from app.models.audio import Audio
import hashlib

def get_all_files(folder):
    files = []

    filenames = next(walk(folder), (None, None, []))[2] 

    for fullname in filenames:
        hashMD5 = hashlib.md5(open(folder+fullname,'rb').read()).hexdigest()
        hashSHA256 = hashlib.sha256(open(folder+fullname,'rb').read()).hexdigest()
        name, extension = os.path.splitext(fullname)
        type = filetype.guess(folder+fullname)
        analisedFile = Audio(name=name, text='none', duration='none', extension=extension, type=type.mime, path=folder+fullname, hashMD5=hashMD5, hashSHA256=hashSHA256)
        files.append(analisedFile)
    
    return files
