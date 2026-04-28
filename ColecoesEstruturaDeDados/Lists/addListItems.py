#Para adicionarmos itens no final de uma lista usamos o metodo append()
mylist = ["apple", "orange", "banana"]
mylist.append("grape")

print(mylist)

#Para inserirmos itens na lista em uma posição específica utilizamos o 
#metodo insert()
mylist = ["apple", "orange", "banana"]
mylist.insert(0,"grape")

print(mylist)

#Para acrescentar elementos de outra lista em sua lista atual, utilize
# o metodo extend()
fruits = ["banana","apple", "cherry"]
tropicalFruits = ["orange", "lime", "mango"]

fruits.extend(tropicalFruits)
print(fruits)

#O metodo extend() não precisa acrescentar somente listas, ele pode adicionar
#qualquer objeto de iteração(listas, tuplas, sets, dicionarios, etc.)
lista = ["orange", "banana"]
tupla = ("apple", "cherry")

lista.extend(tupla)
print(lista)