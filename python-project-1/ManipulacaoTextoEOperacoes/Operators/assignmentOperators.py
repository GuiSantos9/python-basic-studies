# Operadores de Atribuição
# Operadores de atribuição são usados para atribuir valores a variáveis:

# =   Ex: x = 5      (Mesmo que: x = 5)
# +=  Ex: x += 3     (Mesmo que: x = x + 3)
# -=  Ex: x -= 3     (Mesmo que: x = x - 3)
# *=  Ex: x *= 3     (Mesmo que: x = x * 3)
# /=  Ex: x /= 3     (Mesmo que: x = x / 3)
# %=  Ex: x %= 3     (Mesmo que: x = x % 3)
# //= Ex: x //= 3    (Mesmo que: x = x // 3)
# **= Ex: x **= 3    (Mesmo que: x = x ** 3)

# Operadores Bitwise (Binários):
# &=  Ex: x &= 3     (Mesmo que: x = x & 3)
# |=  Ex: x |= 3     (Mesmo que: x = x | 3)
# ^=  Ex: x ^= 3     (Mesmo que: x = x ^ 3)
# >>= Ex: x >>= 3    (Mesmo que: x = x >> 3)
# <<= Ex: x <<= 3    (Mesmo que: x = x << 3)

# O Operador Walrus (Morsa) :=
# O Python 3.8 introduziu o operador :=, conhecido como "walrus operator".
# Ele atribui valores a variáveis como parte de uma expressão maior:
# Ex: print(x := 3)  (Atribui 3 a x e imprime o valor ao mesmo tempo)

numbers = [1,2,3,4,5]
if(count := len(numbers)) > 3:
    print(f"A lista tem {count} elementos")

