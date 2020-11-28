print("*"*25)
print("Calculadora de Média")
print("*"*25)

aluno = dict()
aluno['nome'] = str(input('Qual o seu nome? '))

p = int(input('Quantas provas você realizou '+ aluno['nome']+'? '))

def ValorLista():
  for i in range(1,p+1):
    lista.append(float(input(f'Digite o valor da dua prova {i}: ')))

def Media():
  s=0
  for i in range(len(lista)):
    s += lista[i]
  m= s / len(lista)
  return m

lista = []
ValorLista()
m= Media()
aluno['media'] = m

if aluno['media'] >= 7:
  aluno['situacao'] = "aprovado!!!"

else:
  aluno['situacao'] = "reprovado..."

print(aluno['nome'] + ' sua média é ' + str(aluno['media']) + ' e Você está ' + aluno['situacao'])

print(aluno.items())
print(aluno.keys())
print(aluno.values())
