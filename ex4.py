import pandas as pd

dados = {
    "nome": ["Ana", "Carlos", "Maria", "João", "Pedro"],
    "idade": [22, 30, 40, 50, 20],
    "cidade": ["São Paulo", "Rio", "BH", "Curitiba", "Brasília"]
}

df = pd.DataFrame(dados) #cria um DataFame, que nao é nada mais que uma tabela, no caso esta criando com "dados"

print("tabela completa: ")
print(df) #vai printar o df que nesse momento carrega a tabela 

print("\nmaiores que 25:")
filtrado = df[df["idade"] > 25] #vai pegar os valores maiores que 25 em cada coluna
print(filtrado)


