# Operadores Lógicos
# Operadores lógicos são usados para combinar declarações condicionais:

# and: Retorna True se ambas as declarações forem verdadeiras.
#      Ex: x < 5 and x < 10

# or:  Retorna True se uma das declarações for verdadeira.
#      Ex: x < 5 or x < 4

# not: Inverte o resultado, retorna False se o resultado for verdadeiro.
#      Ex: not(x < 5 and x < 10)

x = 5
print(x > 0 and x < 10)  # Saída: True (ambos são verdadeiros)


x = 5
print(x < 5 or x > 10)   # Saída: False (nenhuma das duas é verdadeira)

x = 5
print(not(x > 3 and x < 10)) # Saída: False
    
    