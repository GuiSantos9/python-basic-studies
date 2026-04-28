# --- TRABALHANDO COM JSON EM PYTHON ---

# JSON é uma sintaxe para armazenar e trocar dados.
# Embora o nome venha do JavaScript, ele é independente de linguagem.

# Em Python, usamos o pacote integrado 'json'.
# Ele permite converter:
# 1. JSON (Texto) para Python (Dicionários/Listas) -> Deserialização
# 2. Python (Dicionários/Listas) para JSON (Texto) -> Serialização

import json

#Analisar JSON - Converter de JSON para Python
#Se você tiver uma string JSON, poderá analisá-la usando o método json.loads().

# "x" é um JSON  
x =  '{ "name":"John", "age":30, "city":"New York"}'

#Analise "x"
y = json.loads(x)

#O resultado é um dicionario em Python 
print(y["age"])

#Converter de Python para JSON
#Se você tiver um objeto Python, poderá convertê-lo em uma string JSON usando o método json.dumps().

#objeto em python (dicionarioi)
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

y = json.dumps(x)
print(y)

#Você pode converter objetos Python dos seguintes tipos em strings JSON:

#dict
#list
#tuple
#string
#int
#float
#True
#False
#None

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))


#JSON em Python
#dict -> Objeto
#lista -> Array
#tupla -> Array
#str -> String
#int -> Número
#float -> Número
#True -> true
#False -> false
#None -> null

x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann","Billy"),
    "pets": None,
    "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
    ]
}

print(json.dumps(x))


#Formatar o Resultado
#O exemplo acima imprime uma string JSON, mas não é muito fácil de ler, pois não possui recuos nem quebras de linha.
#O método `json.dumps()` possui parâmetros para facilitar a leitura do resultado:

#Utilize o parâmetro de recuo para definir o número de recuos:
json.dumps(x, indent=4)

#Você também pode definir os separadores. O valor padrão é (", ", ": "), o que significa usar uma vírgula 
#e um espaço para separar cada objeto e dois pontos e um espaço para separar chaves de valores:

#Exemplo: Use o parâmetro `separators` para alterar o separador padrão:
json.dumps(x, indent=4, separators=(". ", " = "))

#O método `json.dumps()` possui parâmetros para ordenar as chaves no resultado:
#Exemplo: Use o parâmetro `sort_keys` para especificar se o resultado deve ser ordenado ou não:
json.dumps(x, indent=4, sort_keys=True)
