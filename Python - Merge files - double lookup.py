import pandas as pd
import numpy as np

file_path1 = "D:\Data table 1.xlsx"
df = pd.read_excel(file_path1)

file_path2 = "D:\Data table 2.xlsx"
df2 = pd.read_excel(file_path2)

#rename headers if needed
df.rename(columns={'User':'USERID'},inplace=True)
df.rename(columns={'Quantity':'quantity1'},inplace=True)

df2.rename(columns={'Users':'USERID'},inplace=True)
df2.rename(columns={'Quantity':'Quantity2'},inplace=True)

# merge the 2 files
result = pd.merge(df, df2, on='USERID', how='outer')
result = result.replace({np.NAN: 'missing'})

# write merged file
file_path_merged = 'D:\Data table 1 - merged.xlsx'
result.to_excel(file_path_merged, index=0)
