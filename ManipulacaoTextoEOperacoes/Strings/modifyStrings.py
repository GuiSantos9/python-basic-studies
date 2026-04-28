#Python possui um conjunto de métodos integrados que você pode usar em strings.

#O método upper() retorna uma String maiuscula
a = "Hello World"
print(a.upper())

#O método lower() retorna uma String minúscula
a = "Hello World"
print(a.lower())

#Remover espaços em branco
#Espaços em branco são os espaços antes e/ou depois do texto propriamente dito, 
# e muitas vezes você deseja remover esses espaços.

#O método strip() remove qualquer espaço em branco do início ou do fim:
a = " Hello, World! "
print(a.strip()) #retorna "Hello, World!"

#Substituir String
#O método replace() substitui uma string por outra string:
a = "Hello World"
print(a.replace("H", "J"))

#Split String
#O método split() retorna uma lista onde o texto entre o separador especificado 
# se torna os itens da lista.
#O método split() divide a string em substrings se encontrar ocorrências do separador:
a = "Hello, World"
print(a.split(","))


