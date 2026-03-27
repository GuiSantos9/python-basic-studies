#Há muitas maneiras de unirmos dois ou mais sets em Python
#Os metodos union() e update() uniram todos os itens dos dois sets
#O metodo intersection() mantem somente os duplicados
#O metodo difference() mantem os itens do primeiro set que não estão no outro set
#O metodo symmetric_difference() mantem todos os itens exeto os duplicados 

#UNION
set1 = {"apple","banana","cherry"}
set2 = {1,2,3}

set3 = set1.union(set2)
print(set3)

#podemos usar o operador | ao inves do metodo union() e teremos o mesmo resultado
set1 = {"apple","banana","cherry"}
set2 = {1,2,3}

set3 = set1|set2
print(set3)


#Podemos unir multiplos sets com o union()
set1 = {"apple","banana","cherry"}
set2 = {1,2,3}
set3 = {"João", "Maria"}
set4 = {"a","b","c"}

mySet = set1.union(set2, set3, set4)
print(mySet)

#ou
set1 = {"apple","banana","cherry"}
set2 = {1,2,3}
set3 = {"João", "Maria"}
set4 = {"a","b","c"}

mySet = set1 | set2 | set3 | set4
print(mySet)

#podemos unir um set e uma tupla
mySet = {"apple","banana","cherry"}
myTuple = (1,2,3)

mySet1 = mySet.union(myTuple)
print(mySet1)

#UPDATE
#O metodo uptade() insere todos os itens de um set para outro 
#O metodo muda o set original, e não retorna uma nova lista
set1 = {"apple","banana","cherry"}
set2 = {1,2,3}

set1.update(set2)
print(set1)

#ambos union() e update() vão excluir qualquer valor duplicado


#INTERSECTION
#Irá retornar um novo set, que contém somente os itens que estão presentes em ambos os sets 
set1 = {"apple","banana","cherry"}
set2 = {"microsoft","samsung","apple"}

set3 = set1.intersection(set2)
print(set3)

#podemos usar o operador &set1 = {"apple","banana","cherry"}
set2 = {"microsoft","samsung","apple"}

set3 = set1 & set2
print(set3)

#O metodo intersection_uptade() irá manter somente os duplicados, mas vai mudar o set 
#original ao inves de retornar um novo set
set1 = {"apple","banana","cherry"}
set2 = {"microsoft","samsung","apple"}

set1.intersection_update(set2)
print(set1)

# Os valores True e 1 são considerados o mesmo valor. 
# O mesmo vale para False e 0.

# Exemplo: 
# Junte conjuntos que contenham os valores True, False, 1 e 0, 
# e veja o que é considerado duplicata:
set1 = {"apple", 1, "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)

print(set3)

# Diferença (Difference)
# O método difference() retornará um novo conjunto que conterá apenas 
# os itens do primeiro conjunto que não estão presentes no outro conjunto:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)

#podemos usar o operador - 
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2

print(set3)

# O operador - permite apenas juntar conjuntos com conjuntos (set com set), 
# e não com outros tipos de dados como você pode fazer com o método difference().

# O método difference_update() manterá os itens do primeiro conjunto que 
# não estão no outro conjunto, mas alterará o conjunto original 
# em vez de retornar um novo conjunto.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1)

# Diferenças Simétricas (Symmetric Differences)
# O método symmetric_difference() manterá apenas os elementos que NÃO 
# estão presentes em ambos os conjuntos:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)

#ou 

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2 

print(set3)

# O método symmetric_difference_update() também manterá tudo, exceto as 
# duplicatas, mas alterará o conjunto original em vez de retornar um novo conjunto.
