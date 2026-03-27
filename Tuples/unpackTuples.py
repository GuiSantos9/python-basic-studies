#Quando criamos um tupla, normalmente nos atribuimos valores a ela. Isso se chama
#"packing"
fruits = ("apple", "banana","cherry")

#Mas em Python, nos podemos extrair os valores de volta para as variaveis. E isso
# é chamado de "unpacking"

fruits = ("apple", "banana","cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

#Usando asterisco
#Se os números das variaveis é menor do que o numero de valores, podemos adicionar 
#um * no nome e no valor da variavel que seram atribuidos na variavel da lista 
fruits = ("apple", "banana","cherry","strawberry","raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red) #Atribimos o resto dos valores em uma lista chamada "red"

#Se o asterisco for adicionado no nome de outra variavel sem ser a ultima, o Python
#irá atribuir valor na variavel até que o numero de valores que faltam se iguale ao 
#numero de variaveis que faltam
fruits = ("apple", "mango","papaya","pineapple","raspberry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)