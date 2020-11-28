import pandas as pd

df = pd.DataFrame({
  "Nome": [ "João da Silva",
            "Carlos Souza",
            "Maria Ferreira"],
  "Idade": [22, 35, 58],
  "Sexo": ["masculino", "masculino", "feminino"]}
  )

print("A média de idade é", "%.2f" % df.Idade.mean(), "e a idade minima é", df.Idade.min())

