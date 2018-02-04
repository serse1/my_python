import zipfile
with zipfile.ZipFile('название файла','r') as zfile:
    zfile.extractall('/home/ser/Untitled Folder')   
