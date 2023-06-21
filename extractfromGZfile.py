import patoolib
import os
for zipfiles in os.listdir(r'C:\Users\marji\PycharmProjects\netcdftocsv'):
    if zipfiles[-3: ] =='.gz':
        patoolib.extract_archive(zipfiles, outdir=r'C:\Users\marji\PycharmProjects\netcdftocsv\prcp')
for extracted_files in os.listdir(r'C:\Users\marji\PycharmProjects\netcdftocsv\prcp'):
    os.chdir(r'C:\Users\marji\PycharmProjects\netcdftocsv\prcp')
    os.rename(extracted_files, extracted_files+'.nc')