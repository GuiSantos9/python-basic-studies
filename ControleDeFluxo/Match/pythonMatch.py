# O comando match é usado para executar diferentes ações com base 
# em diferentes condições.
# Em vez de escrever muitas declarações if..elif..else, você 
# pode usar a declaração match.
# O comando match seleciona um de muitos blocos de código para 
# ser executado.

#match expression:
#  case x:
#    code block
#  case y:
#    code block
#  case z:
#    code block

day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")


# Valor Padrão (Default Value)
# Use o caractere de sublinhado _ como o último valor de caso (case) 
# se você quiser que um bloco de código seja executado quando não 
# houver outras correspondências:

day = 4
match day:
  case 6:
    print("Hoje é Sábado")
  case 7:
    print("Hoje é Domingo")
  case _:
    print("Ansioso pelo fim de semana")

# Combinar Valores
# Use o caractere pipe | como um operador "or" (ou) na avaliação do case 
# para verificar mais de uma correspondência de valor em um único case:

day = 4
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Hoje é um dia útil")
  case 6 | 7:
    print("Eu amo fins de semana!")


# Declarações If como Guards (Guardas)
# Você pode adicionar declarações if na avaliação do case como 
# uma verificação de condição extra:

month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("Um dia útil em Abril")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("Um dia útil em Maio")
  case _:
    print("Nenhuma correspondência")

    