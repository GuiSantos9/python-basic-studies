#A compreensão de listas oferece uma sintaxe mais concisa quando você
#  deseja criar uma nova lista com base nos valores de uma lista existente.

#Exemplo:

#Com base em uma lista de frutas, você deseja uma nova lista contendo apenas
#as frutas com a letra "a" no nome.
#Sem usar list comprehension, você precisará escrever um laço `for` com um teste
#condicional dentro:
frutas = ["apple", "banana", "cherry", "kiwi", "mango"]
novaLista = []

for x in frutas:
    if "a" in x:
        novaLista.append(x)
    
print(novaLista)

#Com a list comprehension você pode fazer isso com somente uma linha de codigo
frutas = ["apple", "banana", "cherry", "kiwi", "mango"]
novaLista = [x for x in frutas if "a" in x]
print(novaLista)

#A Sintaxe:
#novaLista = [expressao for item in iteração if condição == True]
#O valor de retorno será uma nova lista, deixando a antiga sem mudanças

#Condição
#A condição é como um filtro que somente aceita itens com a valor True
novaLista = [x for x in frutas if x != "apple" ] #so aceita valores que não forem "apple"
#A condição if x != "apple" irá retornar True para todos os valores que não forem "apple"
#fazendo com que a lista tenha todas as frutas menos "apple"

#a condição é opcional e pode ser omitida
novaLista = [x for x in frutas]

#Iteração
#A iteração pode ser qualquer objeto de iteração (listas, tuplas, dicionarios, etc)
#Podemos usar a função range() para criar uma iteração
novaLista = [x for x in range(10)]
novaLista = [x for x in range(10) if x < 5 ]

#Expressão
# A expressão é o item atual na iteração, mas também é o resultado, que você pode manipular
# antes que ele se torne um item da nova lista: 

#torne todos os valores da lista em maiúcula
novaLista = [x.upper() for x in frutas]

#Você pode manipular o resultado como quiser 
#Mude todos os itens da lista para "Hello"
novaLista = ["Hello" for x in frutas]

#A expressão também pode ter condições, mas não como um filtro, mas como um jeito de manipular
#o resultado
novaLista = [x if x != "banana" else "orange" for x in frutas]
