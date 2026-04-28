#Bitwise Operators (bit a bit)
#São utilizados para comparar numeros(binarios)

# &   AND: Define cada bit como 1 se ambos os bits forem 1.
#     Ex: x & y

# |   OR: Define cada bit como 1 se um dos dois bits for 1.
#     Ex: x | y

# ^   XOR: Define cada bit como 1 se apenas um dos dois bits for 1.
#     Ex: x ^ y

# ~   NOT: Inverte todos os bits (O que é 0 vira 1 e vice-versa).
#     Ex: ~x

# <<  Zero fill left shift (Deslocamento à esquerda):
#     Desloca para a esquerda empurrando zeros pela direita e descarta os bits à esquerda.
#     Ex: x << 2

# >>  Signed right shift (Deslocamento à direita sinalizado):
#     Desloca para a direita empurrando cópias do bit mais à esquerda e descarta os bits à direita.
#     Ex: x >> 2


print(6 & 3)
print(6 | 3)
print(6 ^ 3)
print(~6)
print(6 << 3)
print(6 >> 3)