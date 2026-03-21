#Variaveis que são criadas fora de uma função são chamadas de
#Variaveis globais
x = "Bom"

def myfunc():
    print("Jesus é " + x)
myfunc()

#Se você criar uma variável com o mesmo nome dentro de uma função, 
# essa variável será local e só poderá ser usada dentro da função. 
# A variável global com o mesmo nome permanecerá como estava,
#  global e com o valor original.
x = "Bom"

def myfunc():
    x = "Bom"
    print("Jesus é " + x)
myfunc()

print("Jesus é " + x)

#Palavra chave global
#Normalmente, quando você cria uma variável dentro de uma função, 
# essa variável é local e só pode ser usada dentro dessa função.
#Para criar uma variável global dentro de uma função, você pode usar a 
# palavra-chave `global`.

#Se você usar a palavra-chave global,
#a variável pertencerá ao escopo global:
def myfunc():
    global x
    x = "Bom"

myfunc()
print("Jesus é " + x)

#Além disso, use a palavra-chave global se você quer mudar a variavel global
#dentro da função
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)