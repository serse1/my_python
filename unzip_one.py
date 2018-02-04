import zipfile
with zipfile.ZipFile('file name','r') as zfile:
    zfile.extractall('folder path')   
