# --- NOMEANDO E RENOMEANDO MÓDULOS ---

# 1. NOMEAÇÃO:
# Você pode dar o nome que quiser ao arquivo do módulo, 
# mas ele DEVE ter a extensão '.py'. 
# (Ex: ferramentas.py, utilitarios.py)

# 2. ALIAS (APELIDO) COM 'AS':
# Ao importar um módulo, você pode criar um apelido usando a 
# palavra-chave 'as'. Isso é útil para:
# - Encurtar nomes longos.
# - Evitar conflitos com nomes de variáveis que você já usa.

import pythonModules as pyM

a = pyM.pessoa1 = ["idade"]
print(a)


# --- MÓDULOS NATIVOS (BUILT-IN) ---

# O Python possui diversos módulos integrados que você pode importar 
# a qualquer momento. 

# Eles cobrem tarefas comuns como:
# - Matemática (math)
# - Datas e Horas (datetime)
# - Geração de números aleatórios (random)
# - Interação com o Sistema Operacional (os, sys)
# - Manipulação de JSON (json)

import platform

x = platform.system()
print(x)

#USANDO A FUNÇÃO DIR()
#Existe um função nativa para listar todos os nomes de funções(ou nomes de variaveis) em um modulo
#essa é a função dir()

import platform

y = dir(platform)
print(y)

#IMPORTAÇÃO DE UM MODULO
#Podemos escolher importar somente algumas partes de um modulo usando a palavra chave from

def comprimento(nome):
    print(f"Olá {nome}!")

pessoa1 = {
    "nome": "João",
    "idade": 23,
    "nacionalidade": "brasileiro"
}

from pythonModules import pessoa1

print(pessoa1["nome"])

