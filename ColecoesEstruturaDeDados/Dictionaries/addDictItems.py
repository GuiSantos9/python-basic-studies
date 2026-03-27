#Adicionar itens no dicionario é feito usando uma nova chave indice e atribuindo valor
#a ela

thisdict = {
    "marca": "ford",
    "modelo": "mustang",
    "ano": 1964
}
thisdict["cor"] = "branco"
print(thisdict)

#UPTADE
#O metodo uptade() irá atualizar o dicionario com os itens dados no argumento
#Se o item não existe, ele será adicionado 
thisdict = {
    "marca": "ford",
    "modelo": "mustang",
    "ano": 1964
}
thisdict.update({"ano":2000})
print(thisdict)
