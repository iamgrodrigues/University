import sqlite3
from sqlite3.dbapi2 import Cursor

conector = sqlite3.connect("conta.db")
cursor = conector.cursor()

sql = """
  CREATE TABLE IF NOT EXISTS cadastro (codigo INT, nome VARCHAR, idade INT)
  """
cursor.execute(sql)

sql = """
  INSERT INTO cadastro (codigo, nome, idade) VALUES (1281, 'Antonio Mattos', 37)
  """
cursor.execute(sql)

sql = """
  INSERT INTO cadastro (codigo, nome, idade) VALUES (1389, 'Maria Lúcia Machado', 42)
  """
cursor.execute(sql)

sql = """
  INSERT INTO cadastro (codigo, nome, idade) VALUES (1500, 'Ana Leticia', 22)
  """
cursor.execute(sql)

conector.commit()
cursor.close()
conector.close()

print("Abra a pasta do progrma e veja se o arquivo está lá")
print("Fim do programa")
