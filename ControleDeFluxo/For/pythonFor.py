#Um laço `for` é usado para iterar sobre uma sequência (que pode ser uma lista, uma tupla, um dicionário,
#um conjunto ou uma string).

#Ele se assemelha menos à palavra-chave `for` de outras linguagens de programação 
#e funciona mais como um método iterador, como os encontrados em linguagens de programação 
#orientadas a objetos.

#Com o laço `for`, podemos executar um conjunto de instruções, 
#uma vez para cada item em uma lista, tupla, conjunto etc.

#printe uma lista de frutas 
frutas = ["banana","orange","cherry"]
for x in frutas:
    print(x)

#O loop for não é necessário definir previamente uma variável de indexação.

#Até mesmo strings são objetos iteraveis, pois são um conjunto de caracteres
#percorrendo uma string
for x in "Jesus":
    print(x)

#Com a instrução `break`, podemos interromper o loop antes que ele tenha percorrido todos os itens:
frutas = ["apple", "banana", "cherry"]
for x in frutas:
    print(x)
    if x == "banana":
        break

#ou
frutas = ["apple", "banana", "cherry"]
for x in frutas:
    if x == "banana":
        break
    print(x) #printe todos menos "banana"

#Com a instrução continue, podemos interromper a iteração atual do loop e continuar com a próxima: 
frutas = ["apple", "banana", "cherry"]
for x in frutas:
    if x == "banana":
        continue
    print(x)

#Para percorrer um conjunto de código um número específico de vezes, podemos usar a função `range()`.
#A função `range()` retorna uma sequência de números, começando em 0 por padrão, incrementando de 1 em 1
#  (por padrão) e terminando em um número especificado.

for x in range(6):
    print(x)

#A função range() tem como valor inicial padrão 0, porém é possível especificar o valor inicial adicionando 
#um parâmetro: range(2, 6), que significa valores de 2 a 6 (mas não incluindo 6):

for x in range(2,6):
    print(x)

#A função range() incrementa a sequência em 1 por padrão, porém é possível especificar o valor do
#incremento adicionando um terceiro parâmetro: range(2, 30, 3):

for x in range(2, 30, 3):
    print(x)

#A palavra-chave `else` em um laço `for` especifica um bloco de código a ser executado quando o laço terminar:
for x in range(6):
    print(x)
else:
    print("Finally finished!")

#Observação: o bloco else NÃO será executado se o loop for interrompido por uma instrução break.
for x in range(6):
    if x == 3: break
    print(x)
else:
    print("Finally finished!")


#Um laço aninhado é um laço dentro de outro laço.
#O "laço interno" será executado uma vez para cada iteração do "laço externo".
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

#Os laços `for` não podem estar vazios, mas se por algum motivo você tiver um laço `for` 
# sem conteúdo, insira a instrução `pass` para evitar um erro.
for x in [0 ,1 ,2]:
    pass

