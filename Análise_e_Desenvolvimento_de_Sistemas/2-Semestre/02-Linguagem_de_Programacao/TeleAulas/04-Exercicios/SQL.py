import pandas as pd
import sqlite3

conn = sqlite3.connect("../03-Exercicios/conta.db")

df = pd.read_sql_query("SELECT * FROM cadastro", conn)

print(df.head())

data = pd.DataFrame([[200, "Blusa", 59.9],
                    [101, "Calca", 35.9],
                    [203, "Camisa", 99.9]],
                    columns = ["id", "descricao", "valor"])

data.to_sql("Produto", conn)