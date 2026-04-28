#Generators 
#Generators são funções que podem pausar e encerrar suas execuções
#Quando uma função generator é chamada, ele irá retornar um objeto generator, que é um interador
#O código dentro da função não é executada ainda, é somente compilada. 
#A função somente executa quando você itera no generator
def meuGenerator():
    yield 1
    yield 2
    yield 3

for valor in meuGenerator():
    print(valor)

#Os geradores permitem iterar sobre os dados sem armazenar todo o conjunto de dados na memória.
#Em vez de usar `return`, os geradores usam a palavra-chave `yield`.

#A palavra-chave `yield`
#A palavra-chave `yield` é o que transforma uma função em um gerador.
#Quando `yield` é encontrada, o estado da função é salvo e o valor é retornado. 
# Na próxima vez que o gerador for chamado, ele continuará de onde parou.

def conte_ate(n):
    contador = 1
    while contador <= n:
        yield contador
        contador+= 1

for numero in conte_ate(7):
    print(numero)

#Diferente do 'return' a palavra-chave 'yield' pode ser chamada multiplas vezes 

#Geradores economizam memória
#Os geradores são eficientes em termos de memória porque geram valores dinamicamente, 
#em vez de armazenar tudo na memória.
#Para grandes conjuntos de dados, os geradores economizam memória:

def sequencia_grande(n):
    for i in range(n):
        yield i

#isso não cria 1milhão de numeros na memória
gen = sequencia_grande(1000000)
print(next(gen))
print(next(gen))
print(next(gen))

#Usando next() com geradores
#Você pode iterar manualmente por um gerador usando a função next():
def gen_simples():
    yield "Guilherme"
    yield "Matheus"
    yield "Camila"
    yield "Thiago"
    yield "Marcelo"

gen = gen_simples()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
#Se eu colocar mais um print(next(gen)) ele chama o StopIteration exeception

#Expressões Geradoras
#Semelhante às compreensões de lista, você pode criar geradores usando 
# expressões geradoras com parênteses em vez de colchetes:

#Compreensão de lista versus expressão geradora:
#cria uma lista
compreensao_lista = [x * x for x in range(5)]
print(compreensao_lista)

#cria um gerador
expressao_geradora = (x * x for x in range(5))
print(expressao_geradora)
print(list(expressao_geradora))

#usando uma expressão geradora para a soma dos quadrados
soma_quadrados = sum(x * x for x in range(5))
print(soma_quadrados)

#Os geradores podem ser usadas para criar uma sequencia de Fibonacci 
#Ela pode continuar gerando valores indefinidamente, sem que fique sem memória
def fibonacci():
    a,b = 0, 1
    while True:
        yield a
        a,b = b, a + b

#gere os primeiro 100 numeros de fibonacci
gen = fibonacci()
for _ in range(100):
    print(next(gen))

#Metodos
#O método send() permite que enviemos um valor a um gerador 
def echo_generator():
    while True:
        recebido = yield
        print("Rebebido:",recebido)

gen = echo_generator()
next(gen) #prepara o gerador
gen.send("Olá")
gen.send("World")

#O metodo close() para o gerador 
def my_gen():
    try:
        yield 1
        yield 2
        yield 3
    finally:
        print("Generator closed")

gen = my_gen()
print(next(gen))
gen.close()

