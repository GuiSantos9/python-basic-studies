# Métodos de Set (Conjuntos Mutáveis)

# add()         Adiciona um elemento ao conjunto.
# clear()       Remove todos os elementos do conjunto.
# copy()        Retorna uma cópia do conjunto.
# discard()     Remove o item especificado (não gera erro se o item não existir).
# pop()         Remove um elemento aleatório do conjunto.
# remove()      Remove o item especificado (gera erro se o item não existir).
# update()      Atualiza o conjunto com a união de si mesmo e outros (|=).

# --- Operações de Comparação (Retornam True/False) ---

# isdisjoint()  Retorna se dois conjuntos têm intersecção ou não.
# issubset()    Retorna se este conjunto está contido em outro (<=).
# issuperset()  Retorna se este conjunto contém outro (>=).

# --- Operações de Conjunto (Geram novo Set ou Atualizam o atual) ---

# difference()           Diferença (-): Itens que só existem no primeiro.
# difference_update()    Remove do original os itens presentes no outro (-=).
# intersection()         Intersecção (&): Itens presentes em ambos.
# intersection_update()  Mantém no original apenas o que está em ambos (&=).
# symmetric_difference() Diferença Simétrica (^): Itens que NÃO estão em ambos.
# symmetric_difference_update() Atualiza o original com a diferença simétrica (^=).
# union()                União (|): Junta todos os itens de ambos os conjuntos.