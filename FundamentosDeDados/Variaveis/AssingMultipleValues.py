#O python te permite atribuir valores para multiplas variaveis em uma unica linha
x,y,z = "Orange","Banana","Apple"
print(x)
print(y)
print(z)

#Certifique-se de que o número de variáveis ​​corresponda ao número de valores, 
# caso contrário, você receberá um erro.

#Um valor para multiplas variaveis 
x = y = z = "Orange"
print(x)
print(y)
print(z)

#Unpacking 
#Quando você tem uma coleção de valores quer por uma list, tuple, etc
#o python te permite pegar esses valores da coleção e atribuí-los a variaveis
fruits = ["Orange","Banana","Apple"]
x,y,z = fruits
print(x)
print(y)
print(z)
