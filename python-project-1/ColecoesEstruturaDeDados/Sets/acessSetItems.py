#Não podemos acessar os itens no set referindo-se ao se índice ou sua key
#Mas podemos usar um loop no set ou pedir se um valor específico está presente usando
# a palavra chave in

thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

thisset = {"apple", "orange", "cherry"}
print("banana" not in thisset)
