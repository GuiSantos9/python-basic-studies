# --- FUNÇÕES LAMBDA (FUNÇÕES ANÔNIMAS) ---

# Uma função lambda é uma pequena função sem nome.
# Ela pode receber qualquer número de argumentos, mas pode ter 
# APENAS UMA expressão.

# Sintaxe:
# lambda argumentos : expressão

# A expressão é executada e o resultado é retornado AUTOMATICAMENTE.
# Você não usa a palavra-chave 'return' dentro de uma lambda.

x = lambda a : a + 10
print(x(5))

#Por que usar funções lambda ?
# --- O PODER DAS LAMBDAS DENTRO DE OUTRAS FUNÇÕES ---

# O verdadeiro potencial da lambda aparece quando ela é usada como uma 
# função anônima dentro de outra função.

# Imagine uma função que recebe um argumento 'n'. Esse 'n' será usado 
# para criar uma NOVA função (a lambda) que multiplica qualquer 
# número por esse 'n' específico.

# Isso permite criar "fábricas" de comportamentos matemáticos ou lógicos 
# de forma muito concisa.

def minha_funcao(n):
    return lambda a : a * n 

#Use essa função para fazer outra função que sempre dobra o número que você envia
def dobrar(n):
    return lambda a: a * n

variavelDobrada = dobrar(5)
print(variavelDobrada(11))

#Ou, use a mesma função para construir outra função que sempre triplica o número que você enviar
def triplicar():
    return lambda a: a * 3

variavelTriplicada = triplicar()
print(variavelTriplicada(3))

#Ou combine a função
def funcaoMath(n):
    return lambda b: b * n

vDobrada = funcaoMath(2)
vTriplicada = funcaoMath(3)

print(vDobrada(84))
print(vTriplicada(442))

# --- USANDO LAMBDA COM MAP() ---

# A função map() serve para transformar dados. 
# Ela aplica uma função a CADA item de um iterável (como uma lista).

# Sintaxe: map(função, iterável)

# Em vez de criar uma função com 'def' apenas para uma transformação 
# simples, usamos uma lambda para manter o código limpo e rápido.

# Importante: O map() retorna um objeto do tipo map, por isso 
# geralmente o convertemos de volta para uma lista usando list().

numeros = [1,2,3,4,5,6]
dobrado = list(map(lambda x: x * 2, numeros))

print(dobrado)

#LAMBDA COM FILTER()
#A Função filter() cria uma lista de itens para os quais a função retorna True.
numeros = [1,2,3,4,5,6,7,8,9,10]
impares = list(filter(lambda x: x % 2 != 0, numeros))

print(impares)

#LAMBDA COM SORTED()
#A função sorted() pode usar um lambda como uma chave para uma organização(sort) personalisada
estudantes = [("Guilherme",20),("Tiago",19),("Marcelo", 18)]
estudantesOrganizados = sorted(estudantes, key=lambda x: x[1]) #Oganize a lista a partir do segundo elemento da tupla

print(estudantesOrganizados)

#Organize a lista pelo tamanho
palavras = ["apple", "pie", "banana", "cherry"]
palavrasOrganizadas = sorted(palavras, key=lambda x: len(x))

print(palavrasOrganizadas)