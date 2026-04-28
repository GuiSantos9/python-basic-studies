# Copiar um Dicionário
# Você não pode copiar um dicionário simplesmente digitando dict2 = dict1, 
# porque: dict2 será apenas uma referência ao dict1, e as alterações feitas 
# em dict1 serão automaticamente feitas também em dict2.
# Existem maneiras de fazer uma cópia; uma delas é usar o método 
# integrado de dicionário copy().

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

#Outra maneira de copiar um dicionario é usando a função dict()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

mydict = dict(thisdict)
print(mydict)