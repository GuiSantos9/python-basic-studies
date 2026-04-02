# A Instrução pass
# Declarações if não podem estar vazias, mas se por algum motivo você 
# tiver uma declaração if sem conteúdo, insira a instrução pass 
# para evitar erro.

a = 33
b = 200

if b > a:
  pass

# A instrução pass é uma operação nula — nada acontece quando ela é 
# executada. Ela serve como um marcador de lugar (placeholder).

# Por que usar o pass?
# O pass é útil em várias situações:
# 1. Quando você está criando a estrutura do código, mas ainda não 
#    implementou a lógica.
# 2. Quando uma instrução é exigida sintaticamente, mas nenhuma 
#    ação é necessária.
# 3. Como um marcador de lugar (placeholder) para código futuro.
# 4. Em funções ou classes vazias que você planeja implementar depois.

# pass no Desenvolvimento
# Durante o desenvolvimento, você pode querer esboçar a estrutura do 
# seu programa antes de implementar os detalhes. O pass permite 
# que você faça isso sem erros de sintaxe.

age = 16

if age < 18:
  pass # TODO: Add underage logic later
else:
  print("Access granted")

# pass vs Comentários
# Um comentário é ignorado pelo Python, mas pass é uma instrução real 
# que é executada (embora não faça nada). Você precisa do pass onde 
# o Python espera uma instrução, não apenas um comentário.

score = 85

if score > 90:
  pass # This is excellent
print("Score processed")


#multiplas condições 
value = 50

if value < 0:
  print("Negative value")
elif value == 0:
  pass # Zero case - no action needed
else:
  print("Positive value")


#Em outros contextos 
def calculate_discount(price):
  pass # TODO: Implementa logica de desconto

#
