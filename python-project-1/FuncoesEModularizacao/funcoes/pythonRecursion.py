#Recursão é quando uma função chama a si mesma 

#Recursão é um conceito comum em matemática e programação. Significa que uma função chama a si mesma. 
# Isso tem a vantagem de permitir que você percorra os dados em um loop até chegar a um resultado.

#O desenvolvedor deve ter muito cuidado com a recursão, pois é muito fácil acabar escrevendo uma função 
# que nunca termina ou que usa quantidades excessivas de memória ou poder de processamento.
#  No entanto, quando escrita corretamente, a recursão pode ser uma abordagem muito eficiente
# e matematicamente elegante para a programação.

def contador(n):
    if n <= 0:
        print("Feito!")
    else:
        print(n)
        contador(n - 1)

contador(5)

# --- RECURSIVIDADE: CASO BASE E CASO RECURSIVO ---

# Toda função recursiva PRECISA de duas partes fundamentais:

# 1. CASO BASE: É a condição de parada. Sem ele, a função entra em 
#    loop infinito e causa um 'Stack Overflow' (estouro de pilha).
# 2. CASO RECURSIVO: É onde a função chama a si mesma, mas sempre 
#    com um argumento modificado (geralmente menor) para se aproximar 
#    do caso base.

# A recursão divide um problema grande em subproblemas menores 
# do mesmo tipo.

def fatorial(n):
    #Caso Base
    if n == 0 or n == 1:
        return 1
    #Caso Recursivo
    else:
        return n * fatorial(n - 1)

print(fatorial(5))

# --- SEQUÊNCIA DE FIBONACCI COM RECURSIVIDADE ---

# Na sequência de Fibonacci, cada número é a soma dos dois anteriores.
# Sequência: 0, 1, 1, 2, 3, 5, 8, 13, 21...

# Para resolver isso recursivamente, precisamos de:
# 1. DOIS Casos Base: Para n=0 (retorna 0) e n=1 (retorna 1).
# 2. Caso Recursivo: A soma da função chamada para (n-1) e (n-2).
def fibonacci(n):
    if n <= 1:
        return n
    else: 
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))

#Recursão com listas 
def somarListas(numeros):
    if len(numeros) == 0:
        return 0
    else:
        return numeros[0] + somarListas(numeros[1:])

minhaLista = [1,2,3,4,5,6,7,8,9,10]
print(somarListas(minhaLista))

#Encontre o valor da lista
def encontrarMaximo(numeros):
    if len(numeros) == 1: 
        return numeros[0]
    else:
        maximo = encontrarMaximo(numeros[1:])
        return numeros[0] if numeros[0] > maximo else maximo

minhaLista = [3,7,2,9,1]
print(encontrarMaximo(minhaLista))

#Limite de Profundidade da Recursão
#O Python tem um limite para a profundidade da recursão.
#  O limite padrão geralmente gira em torno de 1000 chamadas recursivas.

import sys 
print(sys.getrecursionlimit()) #1000

sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())