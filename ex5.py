import pandas as pd

df = pd.read_csv("vendas.csv") #le o csv

# Quantas linhas e colunas tem
print("Tamanho da tabela:")
print(df.shape)  # (linhas, colunas)

print("\nPrimeiros 5 registros:")
print(df.head) #le exatamente as primeiras 5 linhas

print("\nValores vazios por coluna:")
print(df.isnull().sum())

