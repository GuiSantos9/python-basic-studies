#Temos inumetos metodos para a remoção de itens em dicionarios
#pop() -> remove um item com a chave nome especificada
thisdict = {
    "marca": "ford",
    "modelo": "mustang",
    "ano": 1964
}
thisdict.pop("ano")
print(thisdict)

#O metodo popitem() remove o ultimo item inserido(Em versões antes do 3.7, um item
#aleatório era removido)
thisdict = {
    "marca": "ford",
    "modelo": "mustang",
    "ano": 1964
}
thisdict.popitem()
print(thisdict)

#A palavra chave del remove os itens com a chave nome especificada
thisdict = {
    "marca": "ford",
    "modelo": "mustang",
    "ano": 1964
}
del thisdict["modelo"]

#Ele pode remover o dicionario completamente
thisdict = {
    "marca": "ford",
    "modelo": "mustang",
    "ano": 1964
}
del thisdict

#O metodo clear() limpa o dicionario
thisdict = {
    "marca": "ford",
    "modelo": "mustang",
    "ano": 1964
}
thisdict.clear()
print(thisdict)