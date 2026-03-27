#Podemos acessar os items de um dicionario referenciando a chave nome, dentro dos
#colchetes
thisdict = {
    "marca": "ford",
    "modelo": "mustang",
    "ano": 1964
}

x = thisdict["modelo"]
print(x)

#Temos também o método get() que dará o mesmo resultado
x = thisdict.get("modelo")

#O método keys() irá retornar uma lista com todas as chaves do dicionario
x = thisdict.keys()

#Podemos adicionar novas keys dentro do dicionario mesmo ele ja sendo criado
thisdict = {
    "marca": "ford",
    "modelo": "mustang",
    "ano": 1964
}

x = thisdict.keys()

print(x)

thisdict["cor"] = "branco"

print(x)

#O método values() irá retornar uma lista de todos os valores do dicionario
thisdict = {
    "marca": "ford",
    "modelo": "mustang",
    "ano": 1964
}

x = thisdict.values()
print(x)

#podemos modificar os valores originais
thisdict = {
    "marca": "ford",
    "modelo": "mustang",
    "ano": 1964
}

thisdict["ano"] = 2000
print(thisdict.values())

#Podemos adicionar um novo item
thisdict = {
    "marca": "ford",
    "modelo": "mustang",
    "ano": 1964
}

thisdict["cor"] = "preto"
print(thisdict.values())

#O método items() irá retornar todos os itens do dicionario como uma tupla
x = thisdict.items()
print(x)

#Da mesma forma das anteriores podemos adicionar novos valores e novos itens com esse
#metodo


#Para determinar se uma key específica existe no dicionario usamos a palavra-chave in
thisdict = {
    "marca": "ford",
    "modelo": "mustang",
    "ano": 1964
}

if "modelo" in thisdict:
    print("Sim, o modelo é uma das chaves do dicionario")
