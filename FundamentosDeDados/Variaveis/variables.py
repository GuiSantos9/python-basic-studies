#variables 
#No python não temos comando de declaração de variaveis
#Uma variavel é criada no momento em que você atribui valor a ela

x = 5 #x é do tipo int 
y = "John" #y é do tipo str

#Casting
#Se precisamos especificar o tipo de dado da variavel 
#podemos faze-lo com o casting

x = str(3) #será '3'
y = int(3) #será 3
z = float(3) #será 3.0

#Pegar o tipo
#Você pode pegar o tipo de dado da variavel com a funcao type()
#.__name__ é um atributo interno do objeto que contém o identificador
x = 5
y = "John"
print("O valor de x é do tipo",type(x).__name__)
print("O valor de y é do tipo",type(y).__name__)

#Strings podem ser declaradas tanto em aspas duplas, como em aspas normais
x = "John"
x = 'John'

#Case sensitive
#Nesse caso serão criadas duas variavies 
a = 4
A = "Sally" 

#Nomes de variaveis
#Exemplos de nomes aceitaveis 
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Exemplos de nomes não aceitaveis
#2myvar = "John"
#my-var = "John"
#my var = "John"

