#Slicing
#Você pode retornar um intervalo de caracteres usando a sintaxe de fatiamento.
#Especifique o índice inicial e o índice final, separados por dois pontos, 
# para retornar uma parte da string.

#Obtenha os caracteres da posição 2 à posição 5 (não incluídos):
b = "Hello, World!"
print(b[2:5])

#Slice no inicio
#não especificando o primeiro indice, o intervalo começara no primerio caracter
#Obtenha os caracteres do inicio à posição 5 (não incluídos):
b = "Hello, World!"
print(b[:5]) #Hello 

#Slice no fim 
#não especificando o ultimo indice, o intervalo irá até o fim
b = "Hello, World!"
print(b[2:])

#Indexação negativa
#Use índices negativos para iniciar a fatia a partir do final da string:
b = "Hello, World!"
print(b[-5:-2])