import sqlite3

def ExcluirCliente(Cod):
  sql = "DELETE FROM cadastro WHERE codigo = :param"
  cursor.execute(sql, {'param': Cod})
  conector.commit()
  return print(f"Cliente {(Cod)} com sucesso.")

conector = sqlite3.connect("conta.db")
cursor = conector.cursor()

ExcluirCliente(1389)