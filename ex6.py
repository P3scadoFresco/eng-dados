import pandas as pd

df = pd.read_csv("datas.csv")

print("Antes:")
print(df)
print("Tipo da coluna data: ", df["data"].dtype)

df["data"] = pd.to_datetime(df["data"], format = "%Y/%m/%d")
df["data"] = df["data"].dt.strftime("%d-%m-%Y")

print("depois")
print(df)