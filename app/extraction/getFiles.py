from os import walk

path = './audios/'

filenames = next(walk(path), (None, None, []))[2] 

print(filenames)