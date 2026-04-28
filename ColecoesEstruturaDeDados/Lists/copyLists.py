#Você não pode simplesmente copiar uma lista digitando list2 = list1, porque : list2 
#apenas será uma referencia da list1, e mudanças feitas na list1 vão ser altomaticamente feitas 
# na list2

#Podemos usar o metodo integrado copy()
minhaLista = ["banana","milk","bread"]
lista2 = minhaLista.copy()
print(lista2)

#Outra maneira de copiarmos é utilizando o método integrado list()
minhaLista = ["sword","shield","bow"]
lista3 = list(minhaLista)
print(minhaLista)

#Podemos também copiar a lista usando o operador ":" (slicing)
minhaLista = ["mouse","keyboard","monitor"]
lista4 = minhaLista[:]
print(lista4) 
