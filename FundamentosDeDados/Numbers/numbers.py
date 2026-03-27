#Temos 3 tipos numericos em python: int, float e complex 
#Variaevis do tipo numerico são criadas qunado você atribui valor a elas
x = 1    # int 
y = 3.2  # float
z = 3j   # complex

print(type(x).__name__)
print(type(y).__name__)
print(type(z).__name__)

#O float também podem ser números científicos com um 
# "e" para indicar a potência de 10.
x1 = 35e3
y1 = 12E4
z1 = -87.7e100

print(type(x1).__name__)
print(type(y1).__name__)
print(type(z1).__name__)

#Complex 
#Numeros complexos são escritos com a letra "j" como uma parte imaginaria
x2 = 3+5j
y2 = 5j
z2 = -5j
print(type(x).__name__)
print(type(y).__name__)
print(type(z).__name__)

#Conversão de tipos
#Você pode converter um tipo de dado em outro com os metodos:
#int(), float() e complex()
x3 = 1
y3 = 3.4
z3 = 9j 

a = float(x3)
b = int(y3)
c = complex(x3)

print(a)
print(b)
print(c)

print(type(a).__name__)
print(type(b).__name__)
print(type(c).__name__)

#Python não possui uma função `random()` para gerar números aleatórios, 
# mas possui um módulo integrado chamado `random` que pode ser usado para isso:

import random

#Printe um numero aleatório entre 1 e 10
print(random.randrange(1,10)) 