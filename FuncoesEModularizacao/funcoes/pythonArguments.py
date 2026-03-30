# --- ARGUMENTOS EM FUNÇÕES ---

# Informações podem ser passadas para dentro das funções como argumentos.
# Os argumentos são especificados após o nome da função, dentro dos parênteses.

# Você pode adicionar quantos argumentos quiser, basta separá-los com uma vírgula.

# No exemplo abaixo, a função tem um argumento chamado 'fname' (first name).
# Quando a função é chamada, passamos um nome, que é usado dentro dela 
# para compor e imprimir o nome completo.

def minha_funcao(fnome):
    print(fnome + " Refsnes")

minha_funcao("Email")
minha_funcao("Tobias")
minha_funcao("Linus")

# --- PARÂMETROS VS. ARGUMENTOS ---

# Ambos os termos podem ser usados para a mesma coisa: 
# informações que são passadas para dentro de uma função.

# Do ponto de vista da função:

# PARÂMETRO: É a variável listada dentro dos parênteses na 
# DEFINIÇÃO da função (o "espaço reservado").

# ARGUMENTO: É o valor real que é enviado para a função 
# quando ela é CHAMADA (o "dado real").
def minha_func(nome): # nome é uma parãmetro
    print(f"Olá {nome}")

minha_func("Guilherme") #"Guilherme é um argumento"

# Por padrão, uma função deve ser chamada com o número correto de argumentos.
# Isso significa que a chamada deve "espelhar" a definição da função.

# Se a sua função espera 2 argumentos, você deve chamá-la com exatamente 2 argumentos.
# Nem mais, nem menos.

# Caso o número de argumentos seja diferente do esperado, o Python retornará 
# um erro do tipo 'TypeError'.

def minha_func(nome1, nome2): # nome é uma parãmetro
    print(f"Olá {nome1} {nome2}")

minha_func("Guilherme", "Augusto")

