# A Palavra-chave Elif
# A palavra-chave elif é a maneira do Python de dizer "se as condições 
# anteriores não forem verdadeiras, então tente esta condição".
# A palavra-chave elif permite verificar múltiplas expressões para 
# True e executar um bloco de código assim que uma das condições 
# for avaliada como True.

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

# Múltiplas Declarações Elif
# Você pode ter quantas declarações elif precisar. O Python verificará 
# cada condição em ordem e executará a primeira que for verdadeira.
score = 75

if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")

# Como o Elif Funciona
# Quando você usa elif, o Python avalia as condições de cima para baixo. 
# Assim que encontra uma condição verdadeira, ele executa aquele bloco 
# e ignora todas as condições restantes.
age = 25

if age < 13:
  print("You are a child")
elif age < 20:
  print("You are a teenager")
elif age < 65:
  print("You are an adult")
elif age >= 65:
  print("You are a senior")

# Quando usar Elif
# Use elif quando você tiver múltiplas condições mutuamente exclusivas 
# para verificar. Isso é mais eficiente do que usar várias declarações 
# if separadas, porque o Python para de verificar assim que encontra 
# uma condição verdadeira.

day = 3

if day == 1:
  print("Monday")
elif day == 2:
  print("Tuesday")
elif day == 3:
  print("Wednesday")
elif day == 4:
  print("Thursday")
elif day == 5:
  print("Friday")
elif day == 6:
  print("Saturday")
elif day == 7:
  print("Sunday")