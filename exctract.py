import pandas as pd

df1 = pd.read_csv('../data1.csv')
df2 = pd.read_csv('../data2.csv')
df3 = pd.read_csv('../data3.csv')

combinedDataFrame = pd.concat([df1,df2,df3], ignore_index = False)


