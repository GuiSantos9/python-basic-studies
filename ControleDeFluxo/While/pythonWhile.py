#O python tem dois loops primitivos: o while e o for 

#Com o while nos conseguimos executar um conjunto de declarações enquanto a codição proposta for verdadeira (True)
# Por exemplo printe i enquanto i for menor do que 6

i = 1
while i < 6:
    print(i) 
    i += 1

#Lembre-se de incrementar o valor de i, se não temos um loop infinito
#O laço while requer que as variaveis relevantes já estejam prontas, neste exemplo, nós precisamos definir 
#um valor de indexação, i, que atribumos o valor 1.

print("\n ====\n")

#Com a declaração break nós podemos parar o loop se a condição for verdadeira
#Saia do loop quando i for 3
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

print("\n ====\n")

#Com a declaração "continue" podemos parar a iteração atual, e continuar com o próximo 
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

print("\n ====\n")

#Com a declaração else nos podemos rodar um bloco de codigo mesmo quando a condição não for mais verdadeira 
i = 1 
while i < 6:
    print(i)
    i += 1
else:
    print("O i não é mais menor que 6")

#O bloco else NÃO será executado se o loop for interrompido por uma instrução break.

