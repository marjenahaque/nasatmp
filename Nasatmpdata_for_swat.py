import requests
import pandas as pd
import re
locations = [(22.800,91.710),(22.700,91.830),(22.680,91.880),(22.470,91.790)]
base_url = r"https://power.larc.nasa.gov/api/temporal/daily/point?parameters=T2M_MAX,T2M_MIN&community=RE&longitude={longitude}&latitude={latitude}&start=19820101&end=20171231&format=CSV"
for latitude, longitude in locations:
    api_request_url = base_url.format(longitude=longitude, latitude=latitude)
    lat=str(latitude)
    LAT=re.sub('[\W_]+', '', lat)
    # print(LAT)
    response = requests.get(url=api_request_url, verify=True, timeout=30.00)
    open('tmp'+ str(LAT) + '.csv', 'wb').write(response.content)
    nasa = pd.read_csv(r'C:\Users\marji\PycharmProjects\netcdftocsv\tmp'+str(LAT)+'.csv',skiprows=10, usecols=['T2M_MAX','T2M_MIN'])
    nasa.rename(columns={'T2M_MAX':19820101,'T2M_MIN':''},inplace= True)
    print(nasa)
    nasa.to_csv('tmp'+str(LAT)+'.txt',index = False)