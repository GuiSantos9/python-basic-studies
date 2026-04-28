#O bloco 'try' te permite testar um bloco de código para erros
#O bloco 'except' te permite lidar com os erros
#O bloco 'else' te permite executar o código quando não houver erros
# O bloco 'finally' te permite executar código, independentemente do resultado dos blocos 'try' e 'except'

#Lindando com excessões
#Quando ocorre um erro, ou exceção, como chamamos, o Python normalmente para e gera uma mensagem de erro.
#Essas exceções podem ser tratadas usando o bloco `try`:
x = 10

try: 
    print(x) #irá gerar uma excessão quando x não for definido
except: 
    print("Uma excessão ocorreu!")

#Como o bloco `try` gera um erro, o bloco `except` será executado.
#Sem o bloco `try`, o programa irá falhar e gerar um erro.

#Várias Exceções
#Você pode definir quantos blocos de exceção desejar, por exemplo,
#  se quiser executar um bloco de código específico para um tipo específico de erro:
try:
    print(x)
except NameError: #Verifica se a variável não existe
    print("A variavel 'x' não está definida")
except:
    print("Outra coisa deu errado!")

#Else
#Podemos usar a palavra chave 'else' para definir um bloco de codigo para ser executado quando
#não houver erros.
try: 
    print("Olá")
except:
    print("Deu pau")
else:
    print("Tá de boa")

#Finally
#O bloco `finally`, se especificado, será executado independentemente de o bloco `try` gerar um erro ou não.
try:
    print(x)
except: 
    print("Algo deu errado")
finally:
    print("O try-except foi finalizado")

#Isso pode ser útil para fechar objetos e liberar recursos:
try: 
    f = open("arquivo.txt")
    try:
        f.write("Lorem Ipsum")
    except: 
        print("Algo deu errado na escrita do arquivo")
    finally:
        f.close()
except:
    print("Algo deu errado em abrir o arquivo")

#Lançar uma exceção
#Como desenvolvedor Python, você pode optar por lançar uma exceção se uma condição for atendida.

#Para lançar (ou gerar) uma exceção, use a palavra-chave raise.

x = -1

if  x < 0:
    raise Exception("Desculpe, sem numeros abaixo de zero!")

#Você pode definir o tipo de erro a ser exibido e o texto a ser impresso para o usuário.
x = "hello"

if not type(x) is int:
    raise TypeError("Somente variaveis do tipo inteiro são permitidos")


    
