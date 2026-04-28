# --- DECORATORS (DECORADORES) ---

# Decoradores permitem adicionar comportamento extra a uma função,
# sem alterar o código original dessa função.

# Um decorador é, essencialmente, uma função que recebe outra função 
# como entrada e retorna uma nova função (uma versão "melhorada").

# É amplamente utilizado para:
# 1. Logging (registrar quando uma função é chamada).
# 2. Controle de acesso (verificar se um usuário está logado).
# 3. Medição de tempo (ver quanto tempo uma função demora para rodar).

# --- ORDEM DE APLICAÇÃO DO DECORADOR ---

# 1. PRIMEIRO, defina o decorador:
# O decorador deve ser criado como uma função que aceita outra função.

# 2. DEPOIS, aplique-o:
# Use a sintaxe '@nome_do_decorador' imediatamente acima da 
# definição da função que você deseja modificar.

# Essa ordem é obrigatória porque o Python precisa conhecer o 
# decorador antes de tentar aplicá-lo.

def mudarParaMaiusculo(funcao):
    def funcaoInterna():
        return funcao().upper()
    return funcaoInterna 

@mudarParaMaiusculo 
def minha_funcao():
    return "Olá Mundo!"

print(minha_funcao()) 

# --- TERMINOLOGIA DE DECORADORES ---

# @changecase      <- O DECORADOR (A função que adiciona o comportamento)
# def myfunction(): <- A FUNÇÃO DECORADA (A função que recebe o comportamento)
#     ...


# --- MÚLTIPLAS CHAMADAS DE DECORADORES ---

# Um decorador pode ser chamado (aplicado) várias vezes em funções diferentes.
# Basta colocar o @nome_do_decorador acima de cada função que você deseja decorar.

# Isso permite que você aplique a mesma lógica extra (como logs, travas de 
# segurança ou formatação) em diversos pontos do código sem repetir código.
def mudarParaMaiusculo(funcao):
    def funcaoInterna():
        return funcao().upper()
    return funcaoInterna 

@mudarParaMaiusculo
def minha_func():
    return "Hoje é Pascoa"
print(minha_func())

@mudarParaMaiusculo
def outra_func():
    return "Comemoramos a morte e ressureição de Cristo"
print(outra_func())

# --- ARGUMENTOS NA FUNÇÃO DECORADA ---

# Funções que exigem argumentos também podem ser decoradas.
# Para isso, você deve garantir que a função 'wrapper' aceite esses 
# argumentos e os repasse para a função original.

# A melhor prática é usar '*args' e '**kwargs' no wrapper. 
# Isso torna o seu decorador GENÉRICO, permitindo que ele decore 
# funções com qualquer quantidade de parâmetros.

def mudarParaMaiusculo(funcao):
    def funcaoInterna(x):
        return funcao(x).upper()
    return funcaoInterna 

@mudarParaMaiusculo
def minha_func(nome):
    return f"Olá {nome}"
print(minha_func("Guilherme"))

# --- TORNANDO O DECORADOR UNIVERSAL (*args, **kwargs) ---

# Muitas vezes, o decorador não sabe quais ou quantos argumentos a 
# função decorada irá receber.

# Para resolver isso, adicionamos (*args, **kwargs) à função 'wrapper'.
# 1. O wrapper COLECIONA todos os argumentos (posicionais e nomeados).
# 2. O wrapper REPASSA esses mesmos argumentos para a função original.

# Isso permite que o mesmo decorador funcione com QUALQUER função,
# independentemente da sua assinatura.

def mudarParaMaiusculo(funcao):
    def funcaoInterna(*arg, **kargs):
        return funcao(*arg, **kargs).upper()
    return funcaoInterna 

@mudarParaMaiusculo
def minha_func(nome):
    return f"Olá {nome}"
print(minha_func("Guilherme"))

# --- DECORADORES COM ARGUMENTOS (FÁBRICA DE DECORADORES) ---

# Para que um decorador aceite seus próprios argumentos, precisamos 
# adicionar MAIS UM nível de função (um "wrapper" externo).

# 1. A função mais externa recebe os ARGUMENTOS DO DECORADOR.
# 2. A função do meio recebe a FUNÇÃO DECORADA.
# 3. A função mais interna (wrapper) recebe os ARGUMENTOS DA FUNÇÃO.

# Isso permite criar decoradores dinâmicos e altamente configuráveis.
def mudarMaiusculoOuMinusculo(n):
    def mudarMaiusculoOuMinusculo(funcao):
        def funcaoInterna():
            if n == 1:
                a = funcao().lower()
            else:
                a = funcao().upper()
            return a 
        return funcaoInterna
    return mudarMaiusculoOuMinusculo

@mudarMaiusculoOuMinusculo(1) #Retorne e frase em minusculo 
def minha_func():
    return "Olá Guilherme"
print(minha_func())

# --- MÚLTIPLOS DECORADORES (EMPILHAMENTO) ---

# Você pode usar vários decoradores em uma única função.
# Para isso, basta colocar as chamadas uma em cima da outra.

# A ORDEM IMPORTA: Os decoradores são executados de baixo para cima 
# (do que está mais perto da função para o que está mais longe).

# Pense nisso como camadas de uma cebola: a função original está no centro,
# o decorador de baixo é a primeira camada, e o de cima envolve tudo.

def mudarparaMaiusculo(funcao):
    def funcaoInterna():
        return funcao().upper()
    return funcaoInterna 

def adicionarCumprimento(funcao):
    def funcaoInterna():
        return "Olá "+ funcao() + " Tenha um bom dia!"
    return funcaoInterna

@mudarparaMaiusculo
@adicionarCumprimento
def minha_funceao():
    return "Guilherme"

print(minha_funceao())

# --- PRESERVANDO METADADOS DA FUNÇÃO ---

# Funções em Python possuem metadados, como:
# __name__: O nome da função.
# __doc__: A string de documentação (docstring) da função.

# Quando usamos um decorador, a função original é substituída pela 
# função 'wrapper'. Isso faz com que os metadados da função original 
# sejam "escondidos" pelos metadados do wrapper.

# Para evitar isso, usamos o decorador 'functools.wraps'.
def minhaFuncao():
    return "Tenha um Bom Dia!"

print(minhaFuncao.__name__)

#No entanto, quando uma função é decorada, os metadados da função original são perdidos.
def changecase(func):
    def myinner():
        return func().upper()
    return myinner

@changecase
def myfunction():
    return "Have a great day!"

print(myfunction.__name__)

#Para corrigir isso, o Python possui uma função integrada chamada functools.wraps
# que pode ser usada para preservar o nome e a docstring da função original.
import functools

def mudarParaMaiusculO(funcao):
    @functools.wraps(funcao)
    def funcaoInterna():
        return funcao().upper()
    return funcaoInterna

@mudarParaMaiusculO
def myfunction():
    return "Have a great day!"

print(myfunction.__name__)



