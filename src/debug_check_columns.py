import pandas as pd

df = pd.read_csv("data/weather.csv")
print(df.columns.tolist())
