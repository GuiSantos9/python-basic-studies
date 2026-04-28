#Para adicionarmos um item ao set utilizamos o metodo add()
thisSet = {"apple","banana","cherry"}
thisSet.add("orange")

print(thisSet)

#Para adicionarmos itens de outro set ao set atual usamos o metodo uptade():
thisSet = {"apple","banana","cherry"}
anotherSet = {"grape","mango","lime"}

thisSet.update(anotherSet)

print(thisSet)

#O uptade() não funciona somente para sets podemos usa-lo também para qualquer objeto 
#iterável
thisSet = {"apple","banana","cherry"}
thisList = ["kiwi", "orange"]

thisSet.update(thisList)
print(thisSet)
