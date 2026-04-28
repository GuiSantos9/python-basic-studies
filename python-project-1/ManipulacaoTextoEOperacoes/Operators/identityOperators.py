#Operadores de identidades 
#Operadores de identidade são usados para compararem os objetos, não se 
#eles são iguais, mas se eles são, naverdade, o mesmo objeto, com a mesma
#localização de memória 

#is  -> Retorna True se as duas variaveis são o mesmo objeto:  x is y
#is not -> Retorna True se as duas variáveis não forem o mesmo obj: x is not y

x = ["Banana", "Apple"]
y = ["Banana", "Apple"]
z = x

print(x is y) #False
print(x is z) #True 
print(x == y) #True

print(x is not y) #True

#Diferenças entre is e ==
#Is checa se as variaveis apontam para o mesmo objeto na memória
# == checa se as duas variaveis são iguais

x = [1,2,3]
y = [1,2,3]

print(x is y) #False
print(x == y) #True
