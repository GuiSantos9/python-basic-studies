#Acessando itens da lista
#Os itens de uma lista são indexados e você pode acessa-los
#referindo-se ao número indexado
mylist = ["banana","apple","cherry"]
print(mylist[1]) #Retorna o segundo item da lista 


#Indexação negativa 
#Indexação negativa significa que vamos começar pelo final da lista
mylist = ["banana","apple","cherry"]
print(mylist[-1]) 

# Intervalo de Índices (Range of Indexes)
# Você pode especificar um intervalo de índices determinando onde começar 
# e onde terminar o intervalo.
# Ao especificar um intervalo, o valor de retorno será uma nova lista 
# com os itens especificados.
#string[inicio : fim]
mylist = ["banana","apple","cherry","mango","pineapple","grape"]
print(mylist[2:5])

#Tirando o valor de inicio ele iniciara no primeiro item 
mylist = ["banana","apple","cherry","mango","pineapple","grape"]
print(mylist[:4])

#Tirando o valor final, ele ira percorrer até o final da lista
mylist = ["banana","apple","cherry","mango","pineapple","grape"]
print(mylist[2:])


#Intervalo dos Indices Negativos 
#Especifique os índices negativos se você quer começar a pesquisa pelo final
# da lista
mylist = ["banana","apple","cherry","mango","pineapple","grape"]
print(mylist[-4:-1]) 

#Quero inverter uma lista 
mylist = ["banana","apple","cherry","mango","pineapple","grape"]
invertida = mylist[::-1]

print(mylist[2:5])
print(invertida)

#Checar o item caso ele exista
thislist = ["banana","apple","cherry"]
if "apple" in thislist:
    print("Sim, maça está na lista de frutas")





