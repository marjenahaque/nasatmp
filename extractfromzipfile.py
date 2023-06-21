import zipfile
from zipfile import ZipFile
with ZipFile('asia.zip', 'r') as zipObject:
   listOfFileNames = zipObject.namelist()
   for fileName in listOfFileNames:
       if fileName.endswith('239928.txt'):
           # Extract a single file from zip
           zipObject.extract(fileName, 'temp_py')
           print('All the python files are extracted')