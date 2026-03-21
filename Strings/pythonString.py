#As strings em Python são delimitadas por aspas simples ou aspas duplas.
#'hello' é o mesmo que "hello".
#Você pode exibir uma string literal com a função print():

#Você pode usar aspas dentro de uma string, desde que elas não coincidam
#  com as aspas que envolvem a string:
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

#Atribuir uma string a uma variável
#Atribuir uma string a uma variável é feito digitando o nome da variável, 
# seguido por um sinal de igual e a string:
x = "hello world!"
print(x)

#Strings multilinhas
#Você pode atribuir uma cadeia de caracteres multilinhas a uma variável 
# usando três aspas duplas:
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#ou usando três aspas simples
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#Note: No resultado, as quebras de linha são inseridas na mesma posição que no código.

#Strings e Arrays
#Assim como em muitas outras linguagens de programação populares, 
# as strings em Python são arrays de caracteres Unicode.

#No entanto, Python não possui um tipo de dado específico para caracteres; 
# um único caractere é simplesmente uma string com comprimento 1.

#Os colchetes podem ser usados ​​para acessar elementos da string.

#Exemplo: Pegue o caracter da posição 1 (primeiro caracter esta na posicao 0)
a = "Hello, World!"
print(a[1]) # 'e'

#Percorrendo uma string
#Como as strings são arrays, podemos percorrer os caracteres 
#de uma string usando um loop for.
for x in "banana":
    print(x)

#Tamanho da String 
#para peguar o tamanho da string usamos a função len()
#Ela ira retornar o tamanho da String
a = "Jesus é bom"
print(len(a))

#Verificar string
#Para verificar se uma determinada frase ou caractere está presente em uma string,
#podemos usar a palavra-chave "in".
#Ela ira retornar True se determinada palavra estiver na frase, caso contrario False
txt = "Por que Deus amou o mundo de tal maneira..."
print("Deus" in txt) 

#Use-o em uma instrução if:
#Printe somente se "Deus" estiver na frase
txt = "Por que Deus amou o mundo de tal maneira..."
if "Deus" in txt:  
    print("Sim a palavra está na frase")
else:
    print("Não está na frase")

#Verificar se NÃO
#Para verificar se uma determinada frase ou caractere NÃO está presente em uma 
# string, podemos usar a palavra-chave not in.
#Ela ira retornar True se determinada palavra  NÃO estiver na frase, 
#caso contrario  retorna False
txt = "Bom dia"
print("Oi" not in txt)

#Use-o em uma instrução if:
#Printe somente se "Oi" NÃO estiver na frase
txt = "Bom dia"
if "Oi" not in txt:
    print("A palavra não está na frase")
else:
    print("A palavra está na frase")
