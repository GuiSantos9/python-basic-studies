#Change Item Value
#Para mudar um valor específico de um item, referencie o numero do índice
thislist = ["banana","apple","cherry"]
thislist[1] = "orange"
print(thislist)

#Mude o intervalo dos valores dos itens
# Para alterar o valor de itens dentro de um intervalo específico, defina uma 
# lista com os novos valores e faça referência ao intervalo de números de 
# índice onde você deseja inserir os novos valores:

thislist = ["banana","apple","cherry"]
thislist[4:] = ["strawberry", "watermelon"]
print(thislist)

# Se você inserir mais itens do que substituir, os novos itens serão 
# inseridos onde você especificou, e os itens restantes se moverão 
# adequadamente:
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

# Se você inserir menos itens do que substituir, os novos itens serão 
# inseridos onde você especificou, e os itens restantes se moverão 
# adequadamente:
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)


#Inserir itens 
#Para inserir um novo item na lista, sem  substituir nenhum valor existente,
#podemos utilzar o metodo insert()
#o metodo insert() adiciona um item em um index especificado
thislist = ["apple", "banana", "cherry"]
thislist.insert(2,"grape")
print(thislist)