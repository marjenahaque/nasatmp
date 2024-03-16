
from netCDF4 import Dataset
import numpy as np
import pandas as pd
import glob
all_years = []
 for file in glob.glob('*.nc'):
     print(file)
     Data = Dataset(file, 'r')
     time = Data.variables['time']
     years = time.units[14:18]
     all_years.append(years)

 starting = min(all_years)
 ending = max(all_years)
 date_range = pd.date_range(start=str(starting) + '-01-01', end=str(ending) + '-12-31', freq='D')
 #print(date_range)
 Df = pd.DataFrame(0.0, columns=['Precipitation'], index=date_range)
 #print(Df)
 # Defining the location, lat, lon based on the csv data
 station = pd.read_csv('bdstaion.csv')

 for index, row in station.iterrows():
     location = row['NAME']
     location_latitude = row['LATITUDE']
     location_longitude = row['LONGITUDE']
     all_years.sort()
     for yr in all_years:
         data = Dataset(str(yr) + '.nc', 'r')
         lat = data.variables['lat'][:]
         lon = data.variables['lon'][:]
         #print(precip)
         #Square difference of lat and lon
         sq_diff_lat = (lat - location_latitude)**2
         sq_diff_lon = (lon - location_longitude)**2
         min_index_lat = sq_diff_lat.argmin()
         min_index_lon = sq_diff_lon.argmin()
         precip = data.variables['precip']
         start = str(yr) + '-01-01'
         end = str(yr) + '-12-31'
         d_range = pd.date_range(start=start, end=end, freq='D')
         print(d_range)
         for time_index in np.arange(0, len(d_range)):
             print('recording of the value'+str(d_range[time_index]))
             Df.loc[d_range[time_index]]['Precipitation'] = precip[time_index, min_index_lat, min_index_lon]


     Df.to_csv(location+'.csv')
import csv

nasa = pd.read_csv(r'C:\Users\marji\PycharmProjects\netcdftocsv/tmp5.csv',skiprows=10, usecols=['T2M_MAX','T2M_MIN'])
nasa.rename(columns={'T2M_MAX':19980101,'T2M_MIN':''},inplace= True)
print(nasa)
nasa.to_csv('tmp5.txt',index = False)




