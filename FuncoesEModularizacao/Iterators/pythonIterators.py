#Um iterador é um objeto que possui um numero contável de valores 
#Um iterador é um objeto que pode ser iterado sobre, significando que você pode percorrer pelos valores 
#Tecnicamente em Python, um iterador é um objeto que implementa o protocolo de iteração, que consiste
#os métodos __iter__() e __next__().


#Iterador vs. Iterável
#Listas, tuplas, dicionários e conjuntos são todos objetos iteráveis. 
# São contêineres iteráveis ​​dos quais você pode obter um iterador.

#Todos esses objetos possuem um método `iter()` que é usado para obter um iterador.
minhaTupla = ("maça", "banana", "morango")
meu_iterador = iter(minhaTupla)

print(next(meu_iterador))
print(next(meu_iterador))
print(next(meu_iterador))

#Até mesmo Strings são objetos iteradores e podem retornar um iterador
nome = "Guilherme"
iterador = iter(nome)

while True:
    try: 
        item = next(iterador)
        print(item)
    except StopIteration:
        break

#Nos podemos percorrer nosso iteradores
minha_tupla = (1,2,3,4)

for x in minhaTupla:
    print(x)

#Podemos percorrer pelos caracteres de uma String
minha_string = "Guillherme"

for x in minha_string:
    print(x)

#Criar um Iterador
#Para criar um objeto/classe como um iterador, você precisa implementar os métodos 
# `__iter__()` e `__next__()` no seu objeto.

#Como você aprenderá no capítulo Classes/Objetos em Python, todas as classes possuem uma função chamada
#  `__init__()`, que permite realizar algumas inicializações quando o objeto está sendo criado.

#O método `__iter__()` funciona de forma semelhante: você pode realizar operações (inicialização etc.)
# , mas deve sempre retornar o próprio objeto iterador.

#O método `__next__()` também permite realizar operações e deve retornar o próximo item da sequência.

class MeusNumeros:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a += 1
        return x
    
minha_classe = MeusNumeros()
iterador = iter(minha_classe)

print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))

