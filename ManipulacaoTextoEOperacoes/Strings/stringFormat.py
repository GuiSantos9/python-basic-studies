#Como aprendemos no capítulo sobre variáveis ​​em Python, não podemos combinar strings
#  e números desta forma:

#age = 36
#This will produce an error:
#txt = "My name is John, I am " + age
#print(txt)

#Mas podemos combinar strings e números usando f-strings ou o método format()!
#F-Strings
#A formatação de f-strings foi introduzida no Python 3.6 e agora é o método preferido
# para formatar strings.

#Para especificar uma string como uma F-string, basta colocar
# um "f" antes da string literal e adicionar chaves {} como marcadores 
# para variáveis ​​e outras operações.
age = 20
txt = f"Minha idade é {age}"
print(txt)


#PlaceHolders(Marcadores de Posição) e modificadores
#Um marcador de posição pode conter variáveis, operações, funções e 
# modificadores para formatar o valor.
price = 59
txt = f"The price is {price} dollars"
print(txt)

#Um marcador de posição pode incluir um modificador para formatar o valor.
#Um modificador é incluído adicionando dois pontos (:) seguidos por um 
# tipo de formatação válido, como .2f, que significa número de ponto fixo
# com 2 casas decimais.
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

#Um placeholder pode conter python codes como operadores matematicos
txt = f"The price is {20 * 59} dollars"
print(txt)