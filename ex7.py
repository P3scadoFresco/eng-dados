import sqlite3

# Cria (ou abre) o banco de dados
conn = sqlite3.connect("clientes.db")
cursor = conn.cursor()

# Cria a tabela
cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        cidade TEXT,
        valor_gasto REAL
    )
""")

# Insere 5 clientes
cursor.executemany("""
    INSERT INTO clientes (nome, cidade, valor_gasto) VALUES (?, ?, ?)
""", [
    ("Ana",     "São Paulo", 350.00),
    ("Carlos",  "Rio",       120.00),
    ("Maria",   "São Paulo", 890.00),
    ("João",    "Curitiba",  200.00),
    ("Pedro",   "São Paulo", 540.00),
])

conn.commit()  # salva no banco

# Busca só os de São Paulo
cursor.execute("""
    SELECT nome, cidade, valor_gasto
    FROM clientes
    WHERE cidade = 'São Paulo'
""")

resultados = cursor.fetchall()

print("Clientes de São Paulo:")
for linha in resultados:
    print(linha)

conn.close()