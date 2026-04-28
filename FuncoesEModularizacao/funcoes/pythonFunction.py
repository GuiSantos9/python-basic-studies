#Uma função é um bloco de codigo que é rodado somente quando é chamado
#Uma função pode retornar um dado 
#Uma função ajuda resolvendo repetição de código 

#Criando uma função 
#No Python nós criamos e definimos uma função usando a palavra chave 'def', acompanhado pelo nome da função
# e parênteses 
def minha_funcao():
    print("Minha primeira função em Python!")

#Essa é uma função chamada minha_funcao que printa "Minha primeira função em Python!" quando é chamada

#para chamarmos a função escrevemos seu nome com parenteses
minha_funcao()

#eu posso chamar uma função multiplas vezes 
minha_funcao()
minha_funcao()
minha_funcao()

#Nomes de Funções
#Os nomes de funções seguem as mesmas regras dos nomes das variaveis em Python
# - O nome de uma função deve começar com uma  letra ou underscore(_)
# - O nome de uma função só pode conter letras, números e underscore
# - O nome das funções são case sensitive(Minha_funcao e minha_Funcao são diferentes)

#Porque usamos funções
#Imagine que você precise converter temperaturas de Fahrenheit para Celsius multiplas vezes no programa.
#Sem as funções deriamos que escrever a mão todas os calculos para cada situação 
#Com as funções, escrevemos o código e o reutilizamos
def fahrenheit_to_Celsius(fahrenheit):
    return(fahrenheit - 32) * 5/9

print(fahrenheit_to_Celsius(77))
print(fahrenheit_to_Celsius(95))
print(fahrenheit_to_Celsius(50))

#Retorno de valores 
#Funções podem enviar dados de volta para o código, para isso nós chamamos a declaração return
#Quando uma função alcaça uma declaração de return, ele para de executar e envia o resultado devolta
def comprimento():
    return "Olá eu sou uma função"

message = comprimento()
print(message)

#Você pode retornar o valor diretamente
print(comprimento())

#declaração pass 
#As definições de função não podem estar vazias. Se precisar criar um espaço reservado
# para uma função sem nenhum código, use a instrução `pass`:
def funcao():
    pass

