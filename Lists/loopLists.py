#Você pode fazer um loop pelos itens da lista usando um, loop for

#printando todos os itens da lista um por um
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

#Você também pode fazer um loop pelos itens da lista fazendo referencia
# com seu índice

#Usamos as funções range() e o len() para criar um iterável adequado
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])


#Usando um loop while
#use a função len() para determinar o tamanho da lista, então começe por 0
#e faça o loop pelos itens da lista, fazendo referência aos seus índices
#lembre-se de incrementar o índice por 1 para cada iteração
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i += 1 #Em vez de i++

#Fazendo loop usando Compreenção de Lista (List Comprehension)
#Compreenção de lista oferece a menor sintaxe para fazer loops em listas:
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
