#Entrada do usuário
#O Python permite a entrada de dados pelo usuário.
#Isso significa que podemos solicitar informações ao usuário.
#O exemplo a seguir solicita seu nome e, quando você o digita, ele é exibido na tela:
print("Informe seu nome:")
nome = input()
print(f"Olé {nome}!")

#Usando o prompt
#No exemplo acima, o usuário teve que digitar seu nome em uma nova linha. 
# A função input() do Python possui um parâmetro prompt,
# que funciona como uma mensagem que você pode inserir antes da entrada do usuário, na mesma linha:
name = input("Informe seu nome!")
print(f"Olá {name}!")

#Entrada de Número
#A entrada do usuário é tratada como uma string. Mesmo que, no exemplo acima, você insira um número, o interpretador Python ainda o tratará como uma string.
#Você pode converter a entrada em um número com a função float():
import math

x = input("Informe um número:")

#Encontre a raiz quadrada do numero informado 
y = math.sqrt(float(x))

print(f"A raiz quadrada de {x} é {y}")

#Validando os inputs
y = True
while y == True:
    x = input("Informe um número:")
    try:
        x = float(x);
        y = False
    except:
        print("Tipagem errada amigo, informe um numero")

print("Obrigado!")  
print("Programa finalizado!")