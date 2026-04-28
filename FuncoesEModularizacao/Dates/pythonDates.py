# --- TRABALHANDO COM DATAS (DATETIME) ---

# Em Python, data não é um tipo de dado nativo (como int ou str).
# Para trabalhar com datas, devemos importar o módulo 'datetime'.

# Esse módulo nos permite criar "objetos de data" que facilitam 
# a manipulação de anos, meses, dias, horas e minutos.

import datetime

x = datetime.datetime.now()
print(x)


# --- EXPLORANDO O OBJETO DATETIME ---

# O resultado padrão (ex: 2026-04-21 20:06:14.075629) inclui:
# Ano, Mês, Dia, Hora, Minuto, Segundo e Microssegundo.

# O módulo 'datetime' fornece vários métodos e atributos para 
# extrair apenas a informação que nos interessa de forma isolada.

x = datetime.datetime.now()

print(x.year) #ano
print(x.strftime("%A")) #dia daa semana

# --- CRIANDO OBJETOS DE DATA ESPECÍFICOS ---

# Para criar uma data manualmente, usamos a classe 'datetime()' 
# dentro do módulo 'datetime'.

# O construtor exige, no mínimo, TRÊS parâmetros:
# 1. year (ano)
# 2. month (mês)
# 3. day (dia)

# Você também pode adicionar opcionalmente: hour, minute, second, 
# microsecond e tzinfo (fuso horário).

x = datetime.datetime(2020, 5, 17)

print(x)

# --- FORMATANDO DATAS COM STRFTIME() ---

# O objeto datetime possui o método strftime() para formatar datas 
# em strings legíveis.

# O método aceita um parâmetro chamado 'format', que é uma string 
# contendo códigos especiais (máscaras) que definem como a data 
# deve ser exibida.

# Cada código (começando com %) representa uma parte específica da 
# data ou hora.

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))