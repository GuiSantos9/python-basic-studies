#Escape Character
#Para inserir caracteres inválidos em uma string, use um caractere de escape.

#Um caractere de escape é uma barra invertida \ seguida pelo caractere que você 
#deseja inserir.

#Um exemplo de caractere inválido é uma aspa dupla dentro de uma string que está
#entre aspas duplas:

#Você receberá um erro se usar aspas duplas dentro de uma string que já esteja 
# entre aspas duplas:
#txt = "We are the so-called "Vikings" from the north."

#Para concertar isso uso o escape character \"
txt = "We are the so-called \"Vikings \" from the north."
#We are the so-called "Vikings" from the north.

#Outros escape character usados em python 
#'\ - Aspa única
#\\	- Barra Invertida	
#\n	- Nova linha	
#\r	- Carriage Return	
#\t	- Tab	
#\b	- Backspace	
#\f	- Form Feed	
#\ooo - Octal value	
#\xhh - Valor Hexadecimal


