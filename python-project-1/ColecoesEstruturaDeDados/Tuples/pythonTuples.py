minhaTupla = ("apple", "banana", "cherry")

#Tuplas são usadas para armazenar multiplos itens em uma única variável 
#A tupla é um dos quatro tipos de dados nativos do Python usados
#​​para armazenar coleções de dados; os outros três são lista, conjunto e dicionário, 
# cada um com qualidades e usos diferentes.

#A tupla é uma coleção que é ordenada e INALTERAVEL
#tuplas são escritas com colchetes ()
minhaTupla = ("apple", "banana", "cherry")
print(minhaTupla)

#Os itens de uma tupla são ordenados, inalterados, e aceitam valores duplicados 
#Os itens são indexados, o primeiro item tem o índice[0].

#ORDENADO
#Quando dizemos que as tuplas são ordenadas, significa que os itens têm uma ordem 
# definida e que essa ordem não mudará.

#IMUTÁVEIS
#As tuplas são imutáveis, o que significa que não podemos alterar, adicionar ou remover 
# itens depois que a tupla tiver sido criada.

#DUPLICAVEIS
#Como as tuplas são indexadas, elas podem conter itens com o mesmo valor:
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#Para determinarmos quantos itens temos na tupla usamos a função len()
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(len(thistuple))

#CRIANDO UMA TUPLA COM UM ITEM
#Para criar uma tupla com apenas um item, você precisa adicionar uma vírgula após o item; 
# caso contrário, o Python não a reconhecerá como uma tupla.
minhaTupla = ("cenoura",)
print(type(minhaTupla))

#Os itens da tuplas podem ser de qualquer tipo de dado:
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

#A tupla pode conter dentro dela multiplos tipos de dados de uma vez
tuple1 = ("abc", 34, True, 40, "male")

#Type()
#Na perspectiva do Python, as tuplas são definidas como objetos com o tipo de dados 'tuple':

#Contrutor tuple()
#também é possivel utilizar o construtor tuple() para contruir uma tupla
minhaTupla = tuple(("apple", "banana", "cherry"))
print(minhaTupla)


