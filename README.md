# NASA_POWER_API_PythonforSWAT
This Python script allows you to download daily temperature data from NASA's Power API for specific geographic coordinates. The data is obtained in CSV format and can be used for various purposes, including input to the SWAT (Soil and Water Assessment Tool) module.

## Prerequisites
Before running the script, ensure that you have the following prerequisites:

- Python 3.x installed on your system.
- Required Python libraries installed (you can install them using pip):
  - **requests**: Used for making HTTP requests.
  - **pandas**: Used for data manipulation.
  - **re**: Regular expressions library for text processing.
```python
import requests
import pandas as pd
import re
```
## Usage
1.Modify the locations list with the latitude and longitude coordinates for the locations you are interested in. You can add or remove coordinates as needed.
```python
locations = [(22.800,91.710),(22.700,91.830),(22.680,91.880),(22.470,91.790)]
```

1.Customize the base_url variable if necessary. The default URL fetches daily maximum and minimum temperature data for Renewable Energy (RE) communities from 1982-01-01 to 2017-12-31. You can adjust the parameters, community, start date, and end date as needed.
```python
base_url = r"https://power.larc.nasa.gov/api/temporal/daily/point?parameters=T2M_MAX,T2M_MIN&community=RE&longitude={longitude}&latitude={latitude}&start=19820101&end=20171231&format=CSV"
```

1.Run the script by executing it with Python:   ***Nasatmpdata_for_swat.py***
```python
for latitude, longitude in locations:
    api_request_url = base_url.format(longitude=longitude, latitude=latitude)
    lat=str(latitude)
    LAT=re.sub('[\W_]+', '', lat)
    # print(LAT)
    response = requests.get(url=api_request_url, verify=True, timeout=30.00)
    open('tmp'+ str(LAT) + '.csv', 'wb').write(response.content)
    nasa = pd.read_csv(r'C:\Users\to\your\path\tmp'+str(LAT)+'.csv',skiprows=10, usecols=['T2M_MAX','T2M_MIN'])
    nasa.rename(columns={'T2M_MAX':19820101,'T2M_MIN':''},inplace= True)
    print(nasa)
    nasa.to_csv('tmp'+str(LAT)+'.txt',index = False)
```
1.The script will download temperature data for each location in the locations list and save it as CSV files with filenames like tmp{LAT}.csv and corresponding text files tmp{LAT}.txt.

## Output
For each location specified in the **locations** list, you will get two files:

- **'tmp{LAT}.csv'**: A CSV file containing daily temperature data with columns 'T2M_MAX' and 'T2M_MIN'.
- **'tmp{LAT}.txt'**: A CSV file with the same data, but with columns renamed to the date in YYYYMMDD format (e.g., '19820101' for January 1, 1982).

## Notes
The script uses the latitude to generate a unique filename for each location by removing non-alphanumeric characters from the latitude value.
Make sure to adjust the file paths in the script (**pd.read_csv** and **nasa.to_csv**) according to your system's configuration.
The script currently saves the data in the same directory as the script itself. You can modify the save path as needed.
Remember to comply with NASA's data usage policies and terms when using the data obtained through this script.




