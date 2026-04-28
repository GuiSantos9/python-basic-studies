#Podemos fazer um loop usando o laço for

#Ao percorrer o dicionario, o valor retornado são as chaves do dicionario, mas também
#existem metodos para retornar os valores
thisdict = {
    "marca": "ford",
    "modelo": "mustang",
    "ano": 1964
}

for x in thisdict:
    print(x)

#Para printarmos todos os VALORES um por um
for x in thisdict:
    print(thisdict[x])

#podemos usar o metodo values() para retornar os valores
for x in thisdict.values():
    print(thisdict)

#Podemos usar o metodo keys() para retornar as chaves
for x in thisdict.keys():
    print(thisdict)

#Percorrendo ambos chaves e valores com o método items()
for x, y in thisdict.items():
    print(thisdict(x, y))