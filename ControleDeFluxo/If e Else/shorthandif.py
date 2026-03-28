# Short Hand If (If de uma linha só)
# Se você tem apenas uma instrução para executar, pode colocá-la 
# na mesma linha que a declaração if:

a = 5
b = 2
if a > b: print("a is greater than b")

#if else 

a = 2
b = 330
print("A") if a > b else print("B")

# Atribuir um Valor Com If ... Else (Operador Ternário)
# Você também pode usar um if/else de uma linha para escolher 
# um valor e atribuí-lo a uma variável:
a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)

#variable = value_if_true if condition else value_if_false
#variavel = valor_if_true if condição else valor_if_false


#Multiplas condições em uma linha 
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")


