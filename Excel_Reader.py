import pandas as pd

df = pd.read_excel('demo.xlsx', sheet_name='Sheet1')

print("Column headings:")

print(df.columns)

for i in df.index:
    print(df['A1'][i])