# --- TRABALHANDO COM REGEX (EXPRESSÕES REGULARES) ---

# RegEx é uma sequência de caracteres que forma um PADRÃO DE BUSCA.
# Serve para validar dados (como e-mails) ou extrair informações de textos.

# Em Python, usamos o módulo integrado 're'.

import re # Passo 1: Sempre importe o módulo antes de usar

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

# --- DOMINANDO REGEX (RESUMO TÉCNICO) ---

# 1. FUNÇÕES: findall (lista tudo), search (acha o primeiro), 
#    split (divide), sub (substitui).

# 2. METACARACTERES: São os símbolos que dão poder ao padrão.
#    Ex: \d (dígito), \w (letra/número), \s (espaço).

# 3. MATCH OBJECT: Quando o 'search' encontra algo, ele não retorna 
#    apenas o texto, mas um objeto com a posição (.span()) e o 
#    conteúdo (.group()) da busca.

# 4. FLAGS: Alteram o comportamento global, como re.IGNORECASE 
#    para ignorar maiúsculas/minúsculas.
