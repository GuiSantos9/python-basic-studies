mySet = {"apple", "banana", "cherry"}
print(mySet)
#Um Set é uma coleção desordenada, imutáevl* e não indexada

#Os itens no set são desordenados, imutáveis e não permitem valores duplicados

#Desordenado significa que os itens do set aparecem em uma ordem diferente a cada vez 
#que usamos ele, e não pode ser referenciado por um indice ou uma key 

#Imutável significa que não podemos mudar os itens depois que o set foi criado

#Sem duplicações
#Valores duplicados seram ignorados
mySet = {"apple", "banana", "cherry", "apple"}
print(mySet)

#Os valores True e 1 são considerados os mesmos dentro dos sets e são tratados 
#como duplicados 
mySet = {"apple","banana","cherry",True,1,2}
print(mySet)

#Os valores False e 0 são considerados os mesmos dentro dos sets e são tratados 
#como duplicados 
mySet = {"apple", "banana", "cherry", False, True, 0}
print(mySet)

#Para pegarmos o tamanho de um set usamos a função len()
mySet = {"apple", "banana", "cherry"}
print(len(mySet))

#Os itens dos sets podem ser de qualquer tipo de dado:
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

#O set pode conter dentro dela multiplos tipos de dados de uma vez
set1 = {"abc", 34, True, 40, "male"}

#Type()
#Na perspectiva do Python, os sets são definidas como objetos com o tipo de dados 'sets':

#Contrutor set()
#também é possivel utilizar o construtor tuple() para contruir uma tupla
mySet = set(("apple", "banana", "cherry"))
print(mySet)