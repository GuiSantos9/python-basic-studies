#Os itens de uma tupla são indexados e você pode acessa-los
#referindo-se ao número indexado
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple[1])

#Indexação negativa significa que vamos começar pelo final da tupla
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple[-1])

#Você pode especificar um intervalo de índices definindo onde o intervalo deve começar
# e onde deve terminar.
#Ao especificar um intervalo, o valor retornado será uma nova tupla com os itens especificados
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

#Tirando o valor de inicio ele iniciara no primeiro item 
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

#Tirando o valor final, ele ira percorrer até o final da lista
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

#Especifique os índices negativos se você quer começar a pesquisa pelo final
# da lista
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

#Quero inverter uma tupla 
mytuple = ("banana","apple","cherry","mango","pineapple","grape")
invertida = mytuple[::-1]
print(invertida)

#Checar o item caso ele exista
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")