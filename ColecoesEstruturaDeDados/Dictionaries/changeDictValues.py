#Nós podemos mudar um valor específico apenas referenciando sua chave nome
thisdict = {
    "marca": "ford",
    "modelo": "mustang",
    "ano": 1964
}

thisdict["marca"] = "mercedes"
print(thisdict.get("marca"))

#UPTADE
#O metodo uptade() irá atualizar o dicionario com os itens dados no argumento
#O argumento tem que ser um dicionario, ou qualquer objeto iteravel com pares chave:valor
thisdict = {
    "marca": "ford",
    "modelo": "mustang",
    "ano": 1964
}
thisdict.update({"ano": 2000})
