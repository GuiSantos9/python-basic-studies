#Temos diversas maneiras de unirmos, ou concatenarmos, duas ou mais listas em python 
#A maneira mais facil que temos é utilizando o operador +
lista1 = ["omelete", "frango", "suco"]
lista2 = ["banana", "mel", "café"]

lista3 = lista1 + lista2
print(lista3)

#Outra maneira de unirmos as listas seria anexando os itens da lista2 para lista1 um por um
lista1 = ["omelete", "frango", "suco"]
lista2 = ["banana", "mel", "café"]

for x in lista2:
    lista1.append(x)
    
print(lista1)

#Ou você pode usar o méetodo extend(), que o proposito é de adicionar elementos de uma lista 
#para outra lista

lista1 = ["omelete", "frango", "suco"]
lista2 = ["banana", "mel", "café"]

lista1.extend(lista2)

print(lista1)

