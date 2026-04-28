# Nota: O Python não possui suporte nativo (built-in) para 'Arrays' tradicionais.
# Em vez disso, as 'Python Lists' (Listas) são usadas para essa finalidade.

# Arrays vs. Lists:
# Este guia foca em como usar LISTAS como se fossem ARRAYS.
# No entanto, para trabalhar com arrays reais (com performance otimizada),
# é necessário importar uma biblioteca externa, como a 'NumPy'.

#Arrays são usados para guardar mutiplos valores em uma única variàvel
carros = ["Mercedes","Audi","BMW"]

#O que é um Array?
#É uma variavel especial, que pode guardar mais de um valor ao mesmo tempo em uma unica variavel 
#Se temos uma lista de itens, guardando os itens em variaveis únicas ficara dessa forma
carro1 = "Mercedes"
carro2 = "Audi"
carro3 = "BMW"

# O que fazer se você precisar percorrer (loop) os carros para encontrar um específico?
# E se você tivesse 300 carros em vez de apenas 3?
# A solução é o uso de um Array (ou Lista, no caso do Python)!
# Um array pode armazenar muitos valores sob um único nome de variável.
# Você pode acessar cada um desses valores referenciando um número de índice.
# Isso permite manipular grandes volumes de dados de forma organizada e eficiente.

#Podemos acessar os elementos de um array referenciando seu índice
x = carros[2]

#Modifique o valor do primeiro item do Array
carros[0] = "McLaren"

#Tamanho de um Array
x = len(carros)

#Percorrendo os elementos de um array
for x in carros:
    print(x)

#Adicionando elementos ao final do array
carros.append("Mitsubushi")

#Removendo elementos do Array
carros.pop(3)
carros.remove("McLaren")

#Metodos de arrays são os mesmos das listas
# --- MÉTODOS DE LISTA EM PYTHON ---

# append(): Adiciona um elemento ao final da lista.
# clear(): Remove todos os elementos da lista (deixa-a vazia).
# copy(): Retorna uma cópia da lista (útil para evitar alterar a original).
# count(): Retorna o número de elementos com um valor específico.

# extend(): Adiciona os elementos de outra lista (ou iterável) ao final da lista atual.
# index(): Retorna o índice do primeiro elemento com o valor especificado.
# insert(): Adiciona um elemento em uma posição (índice) específica.

# pop(): Remove o elemento em uma posição específica (e o retorna).
# remove(): Remove o primeiro item que encontrar com um valor específico.
# reverse(): Inverte a ordem dos elementos na lista.
# sort(): Ordena a lista (em ordem alfabética ou numérica).