import sqlite3

def UpdateCliente(Cod, new):
  cursor.execute("""
  UPDATE cadastro
  SET idade = ?
  WHERE codigo = ?
  """, (new,Cod))
  
  conector.commit()
  return print(f"Cliente {(Cod)} foi atualizado com sucesso.")

conector = sqlite3.connect("conta.db")
cursor = conector.cursor()

UpdateCliente(1284, 99)
