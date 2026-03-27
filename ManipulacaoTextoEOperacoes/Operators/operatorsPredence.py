#Precedencia de operadores
#Descreve a ordem em que cada operador performa


#O parentese tem a maior precedencia, as operações dentro dos parenteses 
#devem ser feitas primeiro

print((6+1) - (3+4))

# A Multiplicação * tem precedência maior que a adição +, 
# e portanto as multiplicações são avaliadas antes das adições:

print(6+3 * 5)

# Ordem de Precedência (Do mais alto para o mais baixo):

# ()            Parênteses
# **            Exponenciação
# +x, -x, ~x    Mais unário, menos unário e NOT bitwise
# *, /, //, %   Multiplicação, divisão, divisão inteira e módulo
# +, -          Adição e subtração
# <<, >>        Deslocamentos bitwise à esquerda e à direita
# &             AND bitwise
# ^             XOR bitwise
# |             OR bitwise
# ==, !=, >, >=, <, <=, is, is not, in, not in  (Comparações, identidade e associação)
# not           NOT lógico
# and           AND lógico
# or            OR lógico

#Se duas operações tem a mesma precedencia, a expressão sera executada da
#esquerda para a direita
print(6 + 5 - 4 + 5) # 6 + 5 será resolvido primeiro
