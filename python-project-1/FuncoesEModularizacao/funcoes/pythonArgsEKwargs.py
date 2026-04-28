# --- *ARGS E **KWARGS (ARGUMENTOS ARBITRÁRIOS) ---

# Por padrão, uma função deve ser chamada com o número exato de argumentos.
# No entanto, às vezes você não sabe quantos argumentos serão passados.

# *args: Permite que a função aceite um número ilimitado de argumentos POSICIONAIS.
# Os dados são recebidos dentro da função como uma TUPLA.

# **kwargs: Permite que a função aceite um número ilimitado de argumentos de 
# PALAVRA-CHAVE (Keyword Arguments).
# Os dados são recebidos dentro da função como um DICIONÁRIO.


# --- ARGUMENTOS ARBITRÁRIOS (*args) ---

# Se você não sabe quantos argumentos serão passados para a sua função,
# adicione um asterisco '*' antes do nome do parâmetro.
# Dessa forma, a função receberá uma TUPLA de argumentos.
# Você pode acessar os itens individualmente através de índices ou loops.
# O nome 'args' é apenas uma convenção, o que importa é o '*' inicial.

def minha_funcao(*criancas):
    print("A criança mais nova é",criancas[2])

minha_funcao("Charles", "Tiago", "Hugo")

# --- O QUE É *args? ---

# O parâmetro *args permite que uma função aceite qualquer número 
# de argumentos posicionais.
# Dentro da função, o 'args' se torna uma TUPLA contendo todos 
# os argumentos passados.
# Isso é ideal para quando você não sabe de antemão quantos valores 
# o usuário irá enviar para a função.
def minha_funcao(*args):
    print("Primeiro Argumento",args[0])
    print("Segundo Argumento",args[1])
    print("Terceiro Argumento",args[2])
    print("Todos os Argumentoa",args)

minha_funcao("Bom","Dia", "Meu","Povo", "Querido")

#Podemos usar argumentos regulares junto com os *args
#Os argumentos regulares devem vir primeiro do que o *args
def minha_funcao(comprimentos,*names):
    for name in names:
        print(comprimentos, name)   

minha_funcao("Hello", "Emil", "Tobias", "Linus")

#Exemplos práticos
def my_function(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5))

#Encontrando o valor maximo
def my_function(*numbers):
    if len(numbers) == 0:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

print(my_function(3, 7, 2, 9, 1))

# --- ARGUMENTOS DE PALAVRA-CHAVE ARBITRÁRIOS (**kwargs) ---

# Se você não sabe quantos argumentos de palavra-chave (nomeados) serão 
# passados para a função, adicione dois asteriscos '**' antes do nome do parâmetro.
# Dessa forma, a função receberá um DICIONÁRIO de argumentos.
# Você pode acessar os valores através de suas respectivas chaves.
# O nome 'kwargs' é uma convenção para "Keyword Arguments".

def my_function(**kid):
    print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")



def my_function(**myvar):
    print("Type:", type(myvar))
    print("Name:", myvar["name"])
    print("Age:", myvar["age"])
    print("All data:", myvar)

my_function(name = "Tobias", age = 30, city = "Bergen")


#Combinando os dois 
def my_function(title, *args, **kwargs):
    print("Title:", title)
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo")


#unpacking de uma lista dentro de um argumento
def my_function(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
result = my_function(*numbers) # Same as: my_function(1, 2, 3)
print(result)


#unpacking um dicionario 
def my_function(fname, lname):
    print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refsnes"}
my_function(**person) # Same as: my_function(fname="Emil", lname="Refsnes")