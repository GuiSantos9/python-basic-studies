#O método remove() remove um item em específico
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#Exemplo pratico
minhaLista = ["Guilherme","Julia","Thiago","Ana"]
if "Ana" in minhaLista:
    print("Ana removida da lista")
    minhaLista.remove("Ana")
else:
    print("Ana não está lista!")

#Se tem mais de um item especificado dentro da lista, o metodo remove()
#remove a primeira ocorrencia desse item
thislist = ["apple", "banana", "cherry", "grape", "banana"]
thislist.remove("banana")
print(thislist)


#Removendo um Índice específico
#Para removermos um item em um índice especifico utilizamos o método pop()
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#Se não especificamos o item do método pop() ele remove o ultimo item da lista
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#A palavra chave del também remove um índice específico
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#A palavra chave del também pode deletar um lista inteira 
thislist = ["apple", "banana", "cherry"]
del thislist

#O método clear() limpa a lista, a lista ainda continua a existir, 
#porém não possui mais conteúdo dentro dela 
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

