def BuscaSeq(list, item):
  pos = 0
  x = False

  while pos<len(list) and not x:
    if list[pos]== item:
      x= True
    else:
      pos += 1
  return pos



lista = ["teste1", "teste2", "teste3", "teste4", "teste5", "teste6"]
print(BuscaSeq(lista, "teste4"))
print(BuscaSeq(lista,"teste7"))