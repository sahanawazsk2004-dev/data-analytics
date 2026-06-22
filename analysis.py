

import pandas as pd

df = pd.read_excel("coffe_sales2.xlsx")



print(df.columns)

result =df.groupby('coffee_name')['money'].sum()

print(result)

print()
print(df['coffee_name'].value_counts())
print(df['coffee_name'].value_counts().head(5))
print()

result2 = df.groupby('Month_name')['money'].sum().sort_index()
print(result2)
print()
result3 = df.groupby('Weekday')['money'].sum().sort_index()
print(result3)

print()

result4 = df.groupby('Time_of_Day')['money'].sum().sort_index()
print(result4)
