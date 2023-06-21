import pandas as pd
dup_slope = pd.read_csv(r'C:\Users\marji\PycharmProjects\netcdftocsv\slope.csv')

print(dup_slope)

dup_slope.drop_duplicates(subset="slope",keep='first',inplace=True)
df=dup_slope
df.to_csv('output_halda.csv')
import jenkspy
slope= pd.read_csv(r'C:\Users\marji\PycharmProjects\netcdftocsv\output_halda.csv')
df=slope
breaks = jenkspy.jenks_breaks(df['slope'], n_classes=5)
print(breaks)
