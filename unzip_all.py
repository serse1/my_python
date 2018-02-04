import glob
import zipfile
zip_files = glob.glob('*.zip')

for zip_filename in zip_files:
    zip_handler = zipfile.ZipFile(zip_filename, 'r')
    zip_handler.extractall()
