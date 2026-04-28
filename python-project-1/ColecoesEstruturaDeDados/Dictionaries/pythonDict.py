thisdict = {
    "marca": "ford",
    "modelo": "mustang",
    "ano": 1964
}

#Dictionaries são usados para armazenar valores de dados em pares chave: valor
#um dicionario é uma coleção que está ordenada, alteravel e não aceita duplicatas
thisdict = {
    "marca": "ford",
    "modelo": "mustang",
    "ano": 1964
}
print(thisdict)

# Os itens do dicionário são ordenados, alteráveis e não permitem duplicatas.
# Os itens do dicionário são apresentados em pares chave:valor (key:value) 
# e podem ser referenciados usando o nome da chave.

#printe a marca do dicionario
thisdict = {
    "marca": "ford",
    "modelo": "mustang",
    "ano": 1964
}
print(thisdict["marca"])

# Ordenados ou Desordenados?
# A partir da versão 3.7 do Python, os dicionários são ordenados. 
# No Python 3.6 e versões anteriores, os dicionários eram desordenados.
# Quando dizemos que os dicionários são ordenados, significa que os itens 
# têm uma ordem definida e essa ordem não mudará.
# Desordenado significa que os itens não têm uma ordem definida, você 
# não pode se referir a um item usando um índice.

# Alteráveis (Changeable)
# Dicionários são alteráveis, o que significa que podemos alterar, 
# adicionar ou remover itens após o dicionário ter sido criado.

# Duplicatas Não Permitidas
# Dicionários não podem ter dois itens com a mesma chave:

#Para sabermos quantos itens temos no dicionario usamos a função len()
print(len(thisdict))

#Os valores dentro dos dicionarios podem ter quaisquer tipos de dados 
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

#type() -> <class 'dict'>
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))

#Contrutor dict()
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)