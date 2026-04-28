#Métodos de String 
#Python possui um conjunto de métodos integrados que você pode usar em strings.

#capitalize() -Converte o primeiro caracter em Maiúsculo
#casefold()   -Converte um String em minúsculo
#center(largura, caractere_de_preenchimento(opcional)) -Retorna uma string centralizada
txt = "banana"

x = txt.center(20, "O")

print(x) #irá retornar OOOOOOObananaOOOOOOO

                            #COUNT
#count() - O método retorna o número de vezes que um valor especificado aparece na string.

#sintaxe: string.count(value, start, end)

#value: Obrigatório. Uma string. A string para o valor a ser pesquisado.
#start: Opcional. Um número inteiro. A posição para iniciar a pesquisa. O padrão é 0.
#end: Opcional. Um número inteiro. A posição para finalizar a pesquisa. 
#O padrão é o final da string.
#ex: Pesquisar da posição 10 à 24:
txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple", 10, 24)

print(x) # 1


                            #ENCODE
#encode() - O método encode() é utilizado para transformar uma string
#(que é um texto legível por humanos em formato Unicode) em uma sequência de bytes.
#Pense nele como um "tradutor" que prepara o texto para ser armazenado em um arquivo, 
# enviado pela internet ou processado por sistemas que só entendem números binários.

#Sintaxe: string.encode(encoding=encoding, errors=errors)

#encoding: Opcional. Uma string especificando a codificação a ser usada. O padrão é UTF-8.
#errors: Opcional. Uma string especificando o método de erro. Os valores válidos são:
#'backslashreplace' - usa uma barra invertida no lugar do caractere que não pôde ser codificado
#'ignore' - ignora os caracteres que não podem ser codificados
#'namereplace' - substitui o caractere por um texto explicando o caractere
#'strict' - Padrão, gera um erro em caso de falha
#'replace' - substitui o caractere por um ponto de interrogação
#'xmlcharrefreplace' - substitui o caractere por um caractere XML

txt = "My name is Ståle"

print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))


#                            ENDSWITH
#endswith() - Ele chega se a string termina com um sinal de pontuação(.)
txt = "Hello, welcome to my world."

x = txt.endswith(".")

print(x) # retorna True

#Syntaxe: string.endswith(value, start, end)]

#value: Obrigatório. O valor com o qual a string deve terminar. Este parâmetro também
#pode ser uma tupla; nesse caso, o método retorna verdadeiro se a string terminar com 
#qualquer um dos valores da tupla.

#start: Opcional. Um número inteiro que especifica a posição inicial da busca.
#end: Opcional. Um número inteiro que especifica em qual posição a busca deve terminar.
txt = "Hello, welcome to my world."

x = txt.endswith("my world.", 5, 27)

print(x) # retorna True

#Verifique se a sequência termina com a frase "world." ou "castle.":
txt = "Hello, welcome to my castle."

x = txt.endswith(("my world.","my castle."))

print(x)


#                               EXPANDTABS

#O método expandtabs() define o tamanho da tabulação para o número especificado
#de espaços em branco.

#Sintaxe: string.expandtabs(tabsize)

#tabsize: Opcional. Um número que especifica o tamanho da tabulação.
# O tamanho padrão da tabulação é 8.

txt = "H\te\tl\tl\to"

print(txt)
print(txt.expandtabs(0)) #'Hello'
print(txt.expandtabs(10)) #'H         e         l         l         o'



#                           FIND 
# O método find() encontra a primeira ocorrência do valor especificado.
# O método find() retorna -1 se o valor não for encontrado.
# O método find() é quase igual ao método index(), a única diferença 
# é que o método index() gera uma exceção (erro) se o valor não for encontrado.

#Sintaxe: string.find(value, start, end)

# valor: Obrigatório. O valor a ser pesquisado.
# inicio: Opcional. Onde começar a busca. O padrão é 0.
# fim: Opcional. Onde terminar a busca. O padrão é o final da string.

txt = "Hello, welcome to my world."

x = txt.find("welcome")

print(x) #Retorna a posição da primeira letra da String solicitada: 7

#Encontrando a primeira ocorrencia de "e" entre as posições de 5 à 10
txt = "Hello, welcome to my world."

x = txt.find("e", 5, 10)

print(x)

#Se o valor não for encontrado o find() retorna -1 enquando o index() retorna um erro
txt = "Hello, welcome to my world."

print(txt.find("q"))
print(txt.index("q"))

# capitalize()    Converte o primeiro caractere para maiúsculo
# casefold()      Converte a string para letras minúsculas (modo agressivo para comparação)
# center()        Retorna uma string centralizada
# count()         Retorna o número de vezes que um valor específico ocorre na string
# encode()        Retorna uma versão codificada da string (em bytes)
# endswith()      Retorna verdadeiro se a string termina com o valor especificado
# expandtabs()    Define o tamanho da tabulação (\t) da string
# find()          Procura um valor específico e retorna a posição onde foi encontrado
# format()        Formata valores específicos em uma string
# format_map()    Formata valores específicos de um dicionário em uma string
# index()         Procura um valor específico e retorna a posição (gera erro se não achar)
# isalnum()       Retorna True se todos os caracteres da string forem alfanuméricos
# isalpha()       Retorna True se todos os caracteres da string estiverem no alfabeto
# isascii()       Retorna True se todos os caracteres da string forem caracteres ASCII
# isdecimal()     Retorna True se todos os caracteres da string forem decimais
# isdigit()       Retorna True se todos os caracteres da string forem dígitos
# isidentifier()  Retorna True se a string for um identificador (nome de variável válido)
# islower()       Retorna True se todos os caracteres da string forem minúsculos
# isnumeric()     Retorna True se todos os caracteres da string forem numéricos
# isprintable()   Retorna True se todos os caracteres da string forem imprimíveis
# isspace()       Retorna True se todos os caracteres da string forem espaços em branco
# istitle()       Retorna True se a string seguir as regras de um título
# isupper()       Retorna True se todos os caracteres da string forem maiúsculos
# join()          Converte os elementos de um iterável (como uma lista) em uma string
# ljust()         Retorna uma versão da string justificada à esquerda
# lower()         Converte uma string para letras minúsculas
# lstrip()        Retorna uma versão da string com o recorte (trim) à esquerda
# maketrans()     Retorna uma tabela de tradução para ser usada em traduções
# partition()     Retorna uma tupla onde a string é dividida em três partes
# replace()       Retorna uma string onde um valor específico é substituído por outro
# rfind()         Procura um valor e retorna a última posição onde foi encontrado
# rindex()        Procura um valor e retorna a última posição (gera erro se não achar)
# rjust()         Retorna uma versão da string justificada à direita
# rpartition()    Retorna uma tupla onde a string é dividida em três partes (da direita)
# rsplit()        Divide a string no separador especificado e retorna uma lista (da direita)
# rstrip()        Retorna uma versão da string com o recorte (trim) à direita
# split()         Divide a string no separador especificado e retorna uma lista
# splitlines()    Divide a string nas quebras de linha e retorna uma lista
# startswith()    Retorna verdadeiro se a string começa com o valor especificado
# strip()         Retorna uma versão da string aparada (remove espaços no início e fim)
# swapcase()      Inverte as caixas: minúscula vira maiúscula e vice-versa
# title()         Converte o primeiro caractere de cada palavra para maiúsculo
# translate()     Retorna uma string traduzida
# upper()         Converte uma string para letras maiúsculas
# zfill()         Preenche a string com um número especificado de valores 0 no início
