#Listas em Python 
mylist = ["apple", "banana", "cherry"]

#Lista 
#listas são usadas para guardar multiplos itens e uma única variavel

#lista são uma dos 4 tipos de dados embutidos no python usados para 
#coleções de dados, os outros 3 são a tupla, set e dicionarios, todos 
#com funções e usos diferentes 

#Listas são criadas usando colchetes []
thislist = ["hello", "world"]
print(thislist)

#Itens da lista
#Os itens de uma lista são ordenadas, podem ser mudadas e permitem valores
#duplicados 

#Os itens são indexados, o primeiro item tem o index[0], o segundo tem o 
#index[1] e assim por diante.

#ORDENADO
# Quando dizemos que as listas são ordenadas, isso significa que os itens 
# têm uma ordem definida, e essa ordem não mudará.
# Se você adicionar novos itens a uma lista, os novos itens serão 
# colocados no final da lista.

#MUTÁVEIS 
# A lista é alterável (mutável), o que significa que podemos alterar, 
# adicionar e remover itens em uma lista após ela ter sido criada.

#PERMITIR DUPLICATAS
# Como as listas são indexadas, as listas podem ter itens com o mesmo valor:

mylist = ["apple", "banana", "cherry","apple", "banana", "cherry"]
print(mylist)

#Tamanho da lista
#para vermos o tamanho da lista usamos a função len()
minhaLista = ["apple", "banana", "cherry"]
print(len(minhaLista))

#Tipos de dados
#Os itens da lista podem ter qualquer tipo de dados 
list1 = ["apple", "banana", "cherry"]
list2 = [1,2,3,4,5,6,7]
list3 = [True, False, True, False]

#Uma lista pode conter varios tipos de dados
list1 = ["abc",34,True]


#type()
#Na perspectiva do Python listas são definidas como objetos com o tipo de 
#dado sendo 'list'
#<class 'list'>

minhaLista = ["apple", "banana", "cherry"]
print(type(minhaLista))

#list() constructor
#Também é possível usar o construtor list() para criar uma nova lista
thislist = list(("apple", "banana", "cherry"))
print(thislist)


# Coleções de Python (Arrays)
# Existem quatro tipos de dados de coleção na linguagem de programação Python:

# List (Lista): é uma coleção ordenada e alterável. Permite membros duplicados.
# Tuple (Tupla): é uma coleção ordenada e inalterável. Permite membros duplicados.
# Set (Conjunto): é uma coleção não ordenada, inalterável* e não indexada. Não permite membros duplicados.
# Dictionary (Dicionário): é uma coleção ordenada** e alterável. Não permite membros duplicados.

# *Itens de Set (Conjunto) são inalteráveis, mas você pode remover e/ou adicionar itens quando quiser.
# **A partir da versão 3.7 do Python, os dicionários são ordenados. No Python 3.6 e anteriores, eram não ordenados.

# Ao escolher um tipo de coleção, é útil entender as propriedades desse tipo. 
# Escolher o tipo certo para um conjunto de dados específico pode significar a retenção do 
# significado e pode significar um aumento na eficiência ou segurança.