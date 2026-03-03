import pandas as pd

df = pd.read_csv("vendas.csv")

# Quantas linhas e colunas tem
print("Tamanho da tabela:")
print(df.shape)  # (linhas, colunas)

print("\nPrimeiros 5 registros:")
print(df.head)

print("\nValores vazios por coluna:")
print(df.isnull().sum())

