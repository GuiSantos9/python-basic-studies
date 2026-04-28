# Booleanos representam um de dois valores: True (Verdadeiro) ou False (Falso).
# Valores Booleanos:
# Na programação, você frequentemente precisa saber se uma expressão é True ou False.
# Você pode avaliar qualquer expressão em Python e obter uma de duas respostas: True ou False.
# Quando você compara dois valores, a expressão é avaliada e o Python retorna a resposta Booleana:

print(10 > 9)  #True
print(10 == 9) #False
print(10 < 9)  #False

# Quando você executa uma condição em uma instrução 'if',
# o Python retorna True (Verdadeiro) ou False (Falso):
a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

#A função bool() permite avaliar qualquer valor e retornar True (Verdadeiro) ou False (Falso).
print(bool("Hello"))
print(bool(15))

#Avalie duas variáveis 
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

# Quase qualquer valor é avaliado como True (Verdadeiro) se tiver algum tipo de conteúdo.
# Qualquer string é True, exceto strings vazias.
# Qualquer número é True, exceto o 0.
# Qualquer lista, tupla, conjunto e dicionário são True, exceto os vazios.

bool(123)
bool("abc")
bool(["apple","banana","orange"])

# Na verdade, não existem muitos valores que são avaliados como False (Falso), 
# exceto valores vazios, tais como (), [], {}, "", o número 0 e o valor None. 
# E, claro, o próprio valor False é avaliado como False.

bool(False)
bool(0)
bool("")
bool(())
bool({})
bool([])

# Mas um valor, ou objeto neste caso, é avaliado como False (Falso): 
# e é quando você tem um objeto criado a partir de uma classe com uma 
# função __len__ que retorna 0 ou False:

class myclass():
    def __len__(self): #Se o tamanho for 0, o Python assume que o objeto é "falso".
        return 0
    
myobj = myclass()
print(bool(myobj))

# Funções podem retornar um Booleano
# Você pode criar funções que retornam um Valor Booleano:
def myFunction():
    return True

print(myFunction())



#Printe Yes se a função retornar true
def minhaFunction():
    return True

if minhaFunction():
    print("Yes")
else:
    print("No")

# O Python também possui muitas funções integradas que retornam um valor booleano, 
# como a função isinstance(), que pode ser usada para determinar se um objeto 
# é de um determinado tipo de dado:
x = 200
print(isinstance(x, int))
