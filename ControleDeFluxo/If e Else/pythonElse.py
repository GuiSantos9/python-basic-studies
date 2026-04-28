# A palavra-chave else captura qualquer coisa que não tenha sido 
# capturada pelas condições anteriores.
# A declaração else é executada quando a condição if (e quaisquer 
# condições elif) resultam em False.

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

# Else Sem Elif
# Você também pode ter um else sem o elif:

a = 200
b = 33

if b > a:
    print("b é maior que a")
else:
    print("b não é maior que a")

# Como o Else Funciona
# A declaração else fornece uma ação padrão quando nenhuma das condições 
# anteriores é verdadeira. Pense nela como um "pega-tudo" (catch-all) 
# para qualquer cenário não coberto pelas suas declarações if e elif.

# Nota: A declaração else deve vir por último. Você não pode ter 
# um elif depois de um else.

number = 7

if number % 2 == 0:
  print("The number is even")
else:
  print("The number is odd")

#Podemos combinar if elif e else 

temperature = 22

if temperature > 30:
  print("It's hot outside!")
elif temperature > 20:
  print("It's warm outside")
elif temperature > 10:
  print("It's cool outside")
else:
  print("It's cold outside!")

# Else como Fallback (Reserva)
# A declaração else atua como uma reserva que é executada quando nenhuma 
# das condições anteriores é verdadeira. Isso a torna útil para 
# tratamento de erros, validação e fornecimento de valores padrão.

username = "Emil"

if len(username) > 0:
  print(f"Welcome, {username}!")
else:
  print("Error: Username cannot be empty")