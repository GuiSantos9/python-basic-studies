# --- ESCOPO (SCOPE) ---

# Uma variável está disponível apenas dentro da região em que foi criada.
# Esse conceito de visibilidade e tempo de vida é chamado de 'escopo'.
# Existem, essencialmente, dois níveis principais de escopo:
# 1. Escopo Local: Variáveis criadas dentro de uma função.
# 2. Escopo Global: Variáveis criadas no corpo principal do arquivo.

#Por exemplo: uma variável criada dentro de uma função é disponível dentro da função
def minha_func():
    x = 300
    print(x)

minha_func()

# --- FUNÇÃO DENTRO DE FUNÇÃO (NESTED FUNCTIONS) ---

# Como visto anteriormente, uma variável criada dentro de uma função 
# não está disponível fora dela (escopo local).
# No entanto, essa variável ESTÁ disponível para qualquer função 
# que resida dentro da função original.
# A função interna pode ler as variáveis da função externa, 
# criando uma hierarquia de acesso aos dados.
def minha_funcao():
    x = 300
    def outra_func():
        print(x)
    outra_func()

minha_funcao()

# --- ESCOPO GLOBAL (GLOBAL SCOPE) ---

# Uma variável criada no corpo principal do código Python é uma 
# variável global e pertence ao escopo global.
# Variáveis globais estão disponíveis a partir de qualquer escopo, 
# tanto no global quanto no local (dentro de funções).
# Isso significa que você pode declarar uma variável no topo do seu 
# arquivo e lê-la dentro de qualquer função que criar depois.

x = 500 #variavel global

def mostre_x():
    print(x)

mostre_x()
print(x)

# --- NOMEANDO VARIÁVEIS (CONFLITO DE ESCOPO) ---

# Se você usar o mesmo nome de variável dentro e fora de uma função,
# o Python as tratará como duas variáveis SEPARADAS.
# 1. Variável Global: Disponível no corpo principal (fora da função).
# 2. Variável Local: Disponível apenas dentro da função.
# Alterar o valor da variável local NÃO afetará o valor da variável global,
# mesmo que elas tenham exatamente o mesmo nome.

x = 300

def myfunc():
    x = 200
    print(x)

myfunc()
print(x)

# --- A PALAVRA-CHAVE GLOBAL ---

# Se você precisar criar uma variável global, mas estiver "preso" 
# dentro de um escopo local (dentro de uma função), você pode 
# usar a palavra-chave 'global'.
# A palavra-chave 'global' torna a variável global, o que significa 
# que ela passará a existir e ser acessível fora da função também.
# Além disso, use 'global' se você quiser ALTERAR o valor de uma 
# variável que já existe no escopo global.

def myfunc():
    global x
    x = 300

myfunc()
print(x)

#Use a palavra-chave 'global' se voce quer mudar a variavel global dentro da funcao
x = 300 

def myfunc():
    global x
    x = 200

myfunc()
print(x)

# --- A PALAVRA-CHAVE NONLOCAL ---

# A palavra-chave 'nonlocal' é usada para trabalhar com variáveis 
# dentro de funções aninhadas (nested functions).
# Ela faz com que a variável não seja local para a função interna, 
# mas sim pertença à função externa (a função "pai").
# Sem o 'nonlocal', se você tentar mudar o valor de uma variável da 
# função pai, o Python criará uma nova variável local com o mesmo nome.

def myfunc1():
    x = "Jane"
    def myfunc2():
        nonlocal x
        x = "hello"
    myfunc2()
    return x

print(myfunc1())

# --- A REGRA LEGB (ORDEM DE BUSCA) ---

# O Python segue a regra LEGB ao procurar nomes de variáveis.
# A busca ocorre EXATAMENTE nesta ordem:
# 1. LOCAL (L): Dentro da função atual onde a variável é chamada.
# 2. ENCLOSING (E): Dentro de funções "pai" (em caso de funções aninhadas).
# 3. GLOBAL (G): No nível superior do arquivo (módulo).
# 4. BUILT-IN (B): No "espaço de nomes" interno do próprio Python (ex: print, len).
x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print("Inner:", x)
    inner()
    print("Outer:", x)

outer()
print("Global:", x)

