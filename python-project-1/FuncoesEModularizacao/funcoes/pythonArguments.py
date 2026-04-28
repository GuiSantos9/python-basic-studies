# --- ARGUMENTOS EM FUNÇÕES ---

# Informações podem ser passadas para dentro das funções como argumentos.
# Os argumentos são especificados após o nome da função, dentro dos parênteses.

# Você pode adicionar quantos argumentos quiser, basta separá-los com uma vírgula.

# No exemplo abaixo, a função tem um argumento chamado 'fname' (first name).
# Quando a função é chamada, passamos um nome, que é usado dentro dela 
# para compor e imprimir o nome completo.

def minha_funcao(fnome):
    print(fnome + " Refsnes")

minha_funcao("Email")
minha_funcao("Tobias")
minha_funcao("Linus")

# --- PARÂMETROS VS. ARGUMENTOS ---

# Ambos os termos podem ser usados para a mesma coisa: 
# informações que são passadas para dentro de uma função.

# Do ponto de vista da função:

# PARÂMETRO: É a variável listada dentro dos parênteses na 
# DEFINIÇÃO da função (o "espaço reservado").

# ARGUMENTO: É o valor real que é enviado para a função 
# quando ela é CHAMADA (o "dado real").
def minha_func(nome): # nome é uma parãmetro
    print(f"Olá {nome}")

minha_func("Guilherme") #"Guilherme é um argumento"

# Por padrão, uma função deve ser chamada com o número correto de argumentos.
# Isso significa que a chamada deve "espelhar" a definição da função.

# Se a sua função espera 2 argumentos, você deve chamá-la com exatamente 2 argumentos.
# Nem mais, nem menos.

# Caso o número de argumentos seja diferente do esperado, o Python retornará 
# um erro do tipo 'TypeError'.

def minha_func(nome1, nome2): # nome é uma parãmetro
    print(f"Olá {nome1} {nome2}")

minha_func("Guilherme", "Augusto")

# --- VALORES DE PARÂMETROS PADRÃO (DEFAULT) ---

# Você pode atribuir valores padrão aos parâmetros na definição da função.
# Se a função for chamada sem um argumento para aquele parâmetro, 
# ela usará automaticamente o valor padrão definido.

# Isso torna os argumentos "opcionais" na hora da chamada.

def minha_funcao(nome = "Guilherme"):
    print(nome)

minha_funcao()
minha_funcao("Email") #Opcional

# --- ARGUMENTOS DE PALAVRA-CHAVE (KEYWORD ARGUMENTS) ---

# Você pode enviar argumentos utilizando a sintaxe 'chave = valor' (key = value).
# Dessa forma, a ordem dos argumentos não importa para o Python.

# Ao especificar o nome do parâmetro na chamada da função, você deixa
# explícito qual valor pertence a qual variável.
def funcaoAnimal(animal, nome):
    print(f"Eu tenho um {animal}")
    print(f"O nome do meu {animal} é {nome}")

funcaoAnimal(animal = "cachorro", nome = "huguinho")

#Dessa forma com argumentos de palavra-chave , a ordem dos argumentos não importa.
funcaoAnimal(nome = "Toto", animal = "peixe")

# --- ARGUMENTOS POSICIONAIS (POSITIONAL ARGUMENTS) ---

# Quando você chama uma função com argumentos sem usar palavras-chave (keywords),
# eles são chamados de argumentos posicionais.
# Os argumentos posicionais devem estar na ordem correta, conforme definido
# na criação da função.
# O primeiro argumento da chamada será atribuído ao primeiro parâmetro,
# o segundo ao segundo, e assim por diante.
funcaoAnimal("gato","floquinho")

#ou 

funcaoAnimal("floquinho", "gato")

# --- MISTURANDO ARGUMENTOS POSICIONAIS E DE PALAVRA-CHAVE ---

# Você pode misturar argumentos posicionais e de palavra-chave em uma 
# única chamada de função.
# REGRA CRUCIAL: Argumentos posicionais DEVEM vir antes dos argumentos 
# de palavra-chave (keyword arguments).
# Se você tentar colocar um argumento posicional após um de palavra-chave,
# o Python gerará um erro de sintaxe (SyntaxError).
def meu_animal(animal, nome, idade):
    print(f"Eu tenho um {animal}, seu nome é {nome} e sua idade é de {idade} anos.")

meu_animal("cachorro", nome = "buddy", idade = 2)

# --- PASSANDO DIFERENTES TIPOS DE DADOS ---

# Você pode enviar qualquer tipo de dado como argumento para uma função.
# Isso inclui strings, números, listas, dicionários, objetos, etc.

# O tipo de dado original será preservado dentro da função.
# Se você passar uma lista, ela continuará sendo uma lista dentro da função,
# permitindo que você use métodos como .append() ou faça loops nela.
#lista
def funcao_frutas(frutas):
    for fruta in frutas:
        print(frutas)

minhasfrutas = ["banana", "maça", "melancia"]
funcao_frutas(minhasfrutas)

#dicionario
def funcao_pessoa(pessoa):
    print("Nome:", pessoa["nome"])
    print("Idade:", pessoa["idade"])

minhaPessoa = {
    "nome": "Guilherme",
    "idade":20
}

funcao_pessoa(minhaPessoa)

#Funções podem retornar valores usando a declaração return 
def soma(x,y):
    return x + y

resultado = soma(33, 90)
print(resultado)

#Retornando diferentes tipos de dados 
#Listas 
def minha_func():
    return ["banana", "maça", "morango"]

frutas = minha_func()
for x in frutas:
    print(x)

#Tuplas
def minha_func():
    return (9,10)

x, y = minha_func()
print(x)
print(y)

# --- ARGUMENTOS APENAS POSICIONAIS (POSITIONAL-ONLY) ---

# Você pode especificar que uma função aceite APENAS argumentos posicionais.
# Isso significa que o usuário NÃO poderá usar a sintaxe 'chave = valor'.
# Para definir isso, adicione uma barra ', /' após os argumentos 
# na definição da função.
# Qualquer argumento antes da '/' é restrito a ser apenas posicional.
def my_function(name, /):
    print("Hello", name)

my_function("Email")

# --- ARGUMENTOS APENAS DE PALAVRA-CHAVE (KEYWORD-ONLY) ---

# Para especificar que uma função aceite APENAS argumentos de palavra-chave,
# adicione um asterisco '*' antes dos argumentos na definição da função.
# Isso força o usuário a sempre escrever 'nome_do_parametro = valor' 
# ao chamar a função.
# Tentar passar um argumento de forma posicional para um parâmetro que
# venha após o '*' resultará em um erro 'TypeError'.

def my_function(*, name):
    print("Hello", name)

my_function(name = "Email")

# --- COMBINANDO ARGUMENTOS APENAS POSICIONAIS E APENAS KEYWORD ---

# Você pode combinar os dois tipos de restrição na mesma função.
# Isso cria três "zonas" de argumentos:
# 1. Argumentos ANTES da barra '/' -> Devem ser APENAS POSICIONAIS.
# 2. Argumentos DEPOIS do asterisco '*' -> Devem ser APENAS KEYWORD.
# 3. Argumentos ENTRE a '/' e o '*' -> Podem ser de QUALQUER tipo (padrão).
def my_function(a, b, /, *, c, d):
    return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result)
