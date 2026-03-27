#Um dicionario pode conter dicionarios, são chamados de dicionarios aninhados
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

#Ou podemos criar 3 dicionarios e adicionar em outro
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

#Acessando os items
# Para acessar itens de um dicionário aninhado, você usa o nome dos 
# dicionários, começando pelo dicionário externo:
print(myfamily["child1"]["name"])

#Percorrendo os diacionários aninhados
for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])