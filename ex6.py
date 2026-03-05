import pandas as pd

df = pd.read_csv("datas.csv") #le o csv

print("Antes: ")
print(df)
print("tipo de coluna data: ", df["data"].dtype) #esta printando o tipo de coluna que é aq coluna data

df["data"] = pd.to_datetime(df["data"], format = "%Y/%m/%d") #indica o formato inicial que se encontra o csv
df["data"] = df["data"].dt.strftime("%d-%m-%Y") #muda o formato da data

print("\nDepois: ")
print(df)

