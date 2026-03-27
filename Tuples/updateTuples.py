#Tuplas são imutaveis, significando que você não pode mudar, adicionar ou remover
#itens uma vez que a tupla já foi criada 

#Mas temos algumas soluções alternativas, você pode transformar uma tupla em uma lista,
#mudar a lista e converter a lista de volta a uma tupla 
x = ("apple", "banana","cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#Adicionar itens
#Sendo as tuplas imutaveis, eles não tem um metodo integrado append(), mas temos outros 
#jeitos de adiconar items em uma tupla

#1- Converter para uma lista: igual a solução alternativa usadas para mudar um elemento 
#dentro de uma tupla , podemos converter em uma lista, adicionarmos o elemento, e convertermos
#devolta a uma tupla
x = ("apple", "banana","cherry")
y = list(x)
y.append("orange")
x = tuple(y)

print(x)

#2 - Adicionar uma tupla em outra tupla: É permitido adicionar uma tupla em outra, então,
#se quisermos adicionar um item ou muitos, criamos uma nova tupla com os itens e adicionamos
#na tupla existente
x = ("apple", "banana","cherry")
y = ("apple", "banana","cherry")
x += y

print(x)

#REMOVER ITENS 
#tuplas são imutaveis, então, para removermos itens delas precisamos novamente fazer 
#o uso das soluçoes alternativas
x = ("apple", "banana","cherry")
y = list(x)
y.remove("banana")
x = tuple(y)

print(x)

#Ou podemos deletar o tupla completamente
x = ("apple", "banana","cherry")
del x 