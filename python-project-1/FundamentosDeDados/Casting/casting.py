#Pode haver momentos em que você queira especificar um tipo para uma variável. 
#Isso pode ser feito com conversão de tipo (casting). 
# Python é uma linguagem orientada a objetos e,como tal, usa classes para 
# definir tipos de dados, incluindo seus tipos primitivos.
#A conversão de tipo em Python é feita usando funções construtoras:


#int() - constrói um número inteiro a partir de um literal inteiro, 
# um literal de ponto flutuante (removendo todas as casas decimais) 
# ou um literal de string (desde que a string represente um número inteiro).
x = int(1)   #O valor será 1
y = int(2.3) #O valor será 2
z = int("1") #O valor será 1


#float() - constrói um número de ponto flutuante a partir de um literal inteiro,
#  um literal de ponto flutuante ou um literal de string (desde que a string 
# represente um número de ponto flutuante ou um inteiro).
x = float(2)      #O valor será 2.0
y = float(2.8)    #O valor será 2.8
z = float("1")    #O valor será 1.0
w = float("4.3")  #O valor será 4.3

#str() - constrói uma string a partir de uma ampla variedade de tipos de dados, 
# incluindo strings, literais inteiros e literais de ponto flutuante.
x = str("s1") #O valor será 's1'
y = str(2)    #O valor será '2'
z = str(3.0)  #O valor será '3.0'