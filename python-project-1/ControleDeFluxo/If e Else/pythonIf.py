# Condições Python e declarações If
# O Python suporta as condições lógicas usuais da matemática:
# Igual: a == b
# Diferente: a != b
# Menor que: a < b
# Menor ou igual a: a <= b
# Maior que: a > b
# Maior ou igual a: a >= b

# Essas condições podem ser usadas de várias maneiras, mais comumente 
# em "declarações if" (if statements) e loops.
# Uma "declaração if" é escrita usando a palavra-chave if.
a = 33
b = 200
if b > a:
  print("b is greater than a")

# Como as Declarações If Funcionam
# A declaração if avalia uma condição (uma expressão que resulta em 
# True ou False). Se a condição for verdadeira, o bloco de código dentro 
# da declaração if é executado. Se a condição for falsa, o bloco de 
# código é ignorado (pulado).
number = 15
if number > 0:
  print("The number is positive")

# Indentação (Indentation)
# O Python depende da indentação (espaço em branco no início de uma linha) 
# para definir o escopo no código. Outras linguagens de programação 
# frequentemente usam chaves para essa finalidade.

age = 20
if age >= 18:
  print("You are an adult")
  print("You can vote")
  print("You have full legal rights")

# Usando Variáveis em Condições
# Variáveis booleanas podem ser usadas diretamente em declarações if 
# sem operadores de comparação.
is_logged_in = True 
if is_logged_in:
  print("Welcome back!")

