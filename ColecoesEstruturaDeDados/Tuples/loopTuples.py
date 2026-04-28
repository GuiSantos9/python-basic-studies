#Podemos fazer um loop em uma tupla usando o laço de repetição for
fruits = ("apple", "banana","cherry","strawberry","raspberry")
for x in fruits:
    print(x)

#Nos podemos também fazer um loop nos itens da tupla referindo-se aos numeros índices
#Use as funções range() e len() para criar uma iteração adequada 
fruits = ("apple", "banana","cherry","strawberry","raspberry")

for x in range(len(fruits)):
    print(fruits[x])

#Usando um loop while
#use a função len() para determinar o tamanho da tupla, então começe por 0
#e faça o loop pelos itens da tupla, fazendo referência aos seus índices
#lembre-se de incrementar o índice por 1 para cada iteração
fruits = ("apple", "banana","cherry","strawberry","raspberry")
x = 0 
while x < len(fruits):
    print(fruits[x])
    x += 1

