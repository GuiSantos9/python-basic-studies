#Para remover um item do set usamos o metodo remove() ou o metedo discard()
thisSet = {"apple","banana","cherry"}
thisSet.remove("banana") #Se não houver banana na lista retorna um erro
thisSet.discard("apple") #Se não hoouver apple na lista não retorna um erro

print(thisSet)


#Podemos usar também o metodo pop() para remover um item, mas o metodo ira remover
#um item aleatorio, então não podemos ter certeza qual item é removido, pois, os sets
#são desordenados
thisSet = {"apple","banana","cherry"}

x = thisSet.pop()
print(x)

print(thisSet)

#Para esvaziarmos o set usamos o clear()
thisSet = {"apple","banana","cherry"}
thisSet.clear()
print(thisSet)

#Para deletarmos completamente um set usamos o del
thisSet = {"apple","banana","cherry"}
del thisSet
