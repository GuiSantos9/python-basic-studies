# Operadores Lógicos Python
# Usados para combinar declarações condicionais:

# and: Retorna True se AMBAS as declarações forem verdadeiras.
# or:  Retorna True se pelo menos UMA das declarações for verdadeira.
# not: Inverte o resultado (True vira False e vice-versa).

#AND
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#OR
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

#NOT
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

#MULTIPLES 
idade = 25
e_estudante = False
tem_codigo_desconto = True

if (idade < 18 or idade > 65) and not e_estudante or tem_codigo_desconto:
  print("Discount applies!")


#Usando parentesis para melhor compreenção
temperature = 25
is_raining = False
is_weekend = True

if (temperature > 20 and not is_raining) or is_weekend:
  print("Great day for outdoor activities!")