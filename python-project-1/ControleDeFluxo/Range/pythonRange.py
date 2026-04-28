# A função integrada range() retorna uma sequência imutável de números.
# É comumente utilizada para repetir um loop (laço) um número específico de vezes.

# Esse conjunto de números possui seu próprio tipo de dado, chamado 'range'.

# Nota: "Imutável" significa que a sequência não pode ser modificada
# após ter sido criada.



# Chamando range() com apenas um argumento:
# O argumento fornecido representa o valor de parada (stop).

# O argumento de início (start) é opcional.
# Se não for fornecido, o padrão (default) é 0.

# Exemplo: range(10) retorna uma sequência de 0 a 9.
# O início (0) é inclusivo (faz parte da sequência).
# O valor de parada (10) é exclusivo (não faz parte da sequência).

x = range(10) #cria um sequencia de números de 0 à 9

# Chamando range() com dois argumentos:
# O primeiro argumento representa o valor de início (start).
# O segundo argumento representa o valor de parada (stop).
# Exemplo: range(3, 10) retorna uma sequência de cada número de 3 a 9.
# O valor inicial (3) é incluído, mas o valor final (10) é excluído.
# Na prática, isso gera os números: 3, 4, 5, 6, 7, 8, 9.
x = range(3, 10)


# Chamando range() com três argumentos:
# O primeiro é o início (start), o segundo é a parada (stop) e o terceiro é o passo (step).
# O 'step' (passo) define a diferença entre cada número na sequência.
# Ele é opcional: se não for declarado, o padrão (default) é 1.
# Exemplo: range(3, 10, 2)
# Retorna uma sequência de 3 a 9, pulando de 2 em 2.
# Resultado: 3, 5, 7, 9.
x = range(3, 10, 2)


# Usando ranges:
# Os ranges são frequentemente utilizados em loops 'for'.
# Eles servem para iterar (percorrer) sobre uma sequência de números.
# Isso é ideal para quando você sabe exatamente quantas vezes 
# deseja que um bloco de código seja executado.
for x in range(10):
    print(x)


# Usando List para exibir Ranges:
# O objeto 'range' é um tipo de dado que representa uma sequência imutável.
# Ele não é "exibível" diretamente (se você der print, verá apenas 'range(0, 10)').
# Por isso, os ranges são frequentemente convertidos em listas para exibição.
# Isso "força" o Python a gerar todos os números da sequência de uma vez.

print(list(range(5)))
print(list(range(1, 6)))
print(list(range(5, 20, 3)))

# Fatiando (Slicing) Ranges:
# Assim como outras sequências (listas, strings), ranges podem ser fatiados.
# O fatiamento extrai uma subsequência do range original.
# A sintaxe de fatiamento é: range_objeto[inicio:parada:passo]
# O resultado de um fatiamento de um range é um novo objeto range.

r = range(10)
print(r[2])
print(r[:3])

# Teste de Pertencimento (Membership Testing):
# Ranges suportam o operador 'in' para verificar se um valor está na sequência.

# O operador 'in' retorna True se o valor existir no range, e False caso contrário.
# Também podemos usar 'not in' para verificar se um valor NÃO está presente.

# Diferente de uma lista comum, o range faz essa verificação de forma instantânea,
# usando cálculos matemáticos em vez de olhar item por item.
r = range(0, 10, 2)
print(6 in r)
print(7 in r)

# Comprimento (Length):
# Ranges suportam a função integrada len() para obter o número de elementos.

# O Python calcula o tamanho do range sem precisar gerar a sequência completa,
# o que torna essa operação extremamente rápida e eficiente em termos de memória.

# A lógica interna é basicamente: (parada - início) / passo (arredondado para cima).
r = range(0, 10, 2)
print(len(r))


