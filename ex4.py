import pandas as pd

dados = {
    "nome": ["Ana", "Carlos", "Maria", "João", "Pedro"],
    "idade": [22, 30, 40, 50, 20],
    "cidade": ["São Paulo", "Rio", "BH", "Curitiba", "Brasília"]
}

df = pd.DataFrame(dados)

print("tabela completa: ")
print(df)

print("\nmaiores que 25:")
filtrado = df[df["idade"] > 25]
print(filtrado)


