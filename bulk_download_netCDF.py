import requests
import pandas as pd
import numpy as np
import os

username = '************.com'
password = '******'

years = np.arange(1998,2016)

for year in years:
    url = 'http://aphrodite.st.hirosaki-u.ac.jp/product/APHRO_V1808_TEMP/APHRO_MA/025deg_nc/APHRO_MA_TAVE_025deg_V1808.'+ str(year)+ '.nc.gz'
    r = requests.get(url, auth=(username,password), allow_redirects = True)
    open(str(year)+'.gz', 'wb').write(r.content)


    


