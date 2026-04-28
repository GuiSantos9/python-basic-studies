#Membership Operators 
#membership operators são usados para testar se uma sequencia está presente 
#em um objeto

#in -> Retorna True se a sequencia com o valor especificado estiver presente
#no objeto

#not in -> Retorna True se a sequencia com o valor especificado não estiver
#presente no objeto

fruits = ["banana", "morango", "manga"]

print("banana" in fruits)
print("abacaxi" not in fruits)

#os memberships operators também funcionam em strings
text = "Hello World" 

print("H" in text)
print("hello" in text)
print("z" not in text)