import pandas as pd
df = pd.read_csv("08\hello.csv")
ser = pd.Series(df['Name'])
print(ser)
ser = pd.DataFrame(df[['Name','Team','Number']])
print(ser)
