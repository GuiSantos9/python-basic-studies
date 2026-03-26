# Ordenar Lista Alfanumericamente
# Objetos do tipo lista têm um método sort() que ordenará a lista 
# alfanumericamente, de forma ascendente, por padrão:
minhaLista = ["orange", "mango", "kiwi", "pineapple", "banana"]
minhaLista.sort()
print(minhaLista)

minhaListaDeNumeros = [100,43,542,324,56,2]
minhaListaDeNumeros.sort()
print(minhaListaDeNumeros)

#Ordenando de forma decresente 
#para ordenar de forma decrescente usamos a palavra chave reverse = True
minhaLista = ["orange", "mango", "kiwi", "pineapple", "banana"]
minhaLista.sort(reverse=True)
print(minhaLista)

minhaListaDeNumeros = [100,43,542,324,56,2]
minhaListaDeNumeros.sort(reverse=True)
print(minhaListaDeNumeros)


# Customizar Função de Ordenação
# Você também pode customizar sua própria função usando o argumento de 
# palavra-chave key = function.
# A função retornará um número que será usado para ordenar a lista 
# (o menor número primeiro):
def myfunc(n):
    return abs(n - 50) #Retorna os numeros mais proximos de 50

minhaListaDeNumeros = [100, 50, 65, 82, 23]
minhaListaDeNumeros.sort(key = myfunc)
print(minhaListaDeNumeros) 

# Ordenação Sensível a Maiúsculas e Minúsculas (Case Sensitive)
# Por padrão, o método sort() é sensível a maiúsculas e minúsculas, 
# resultando em todas as letras maiúsculas sendo ordenadas antes 
# das letras minúsculas:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
# Felizmente, podemos usar funções integradas (built-in) como funções de 
# chave ao ordenar uma lista.
# Portanto, se você quiser uma função de ordenação insensível a maiúsculas 
# e minúsculas, use str.lower como uma função de chave:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

# Ordem Inversa (Reverse Order)
# E se você quiser inverter a ordem de uma lista, independentemente do alfabeto?
# O método reverse() inverte a ordem de classificação atual dos elementos.
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)