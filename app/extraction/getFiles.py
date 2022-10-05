from os import walk

path = './audios/'

f = []
for (dirpath, dirnames, filenames) in walk(path):
    print(filenames)
    f.extend(filenames)
    break