#Frozenset é uma versão imutável do set
#Como os sets, ele contem elementos únicos, sem ordem e imutáveis 
#Diferente dos sets, elementos não podem ser adicionados ou removidos

#Usamos o contrutor frozenset para criar um frozenset em qualquer objeto iteravel
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))

# Métodos de Frozenset (Conjuntos Imutáveis)

# copy()                 Retorna uma cópia rasa (shallow copy).
# difference()           Retorna um novo frozenset com a diferença.
# intersection()         Retorna um novo frozenset com a interseção.
# isdisjoint()           Retorna se dois frozensets têm uma interseção (True/False).
# issubset()             Retorna True se este frozenset for um subconjunto de outro.
# issuperset()           Retorna True se este frozenset for um superconjunto de outro.
# symmetric_difference() Retorna um novo frozenset com a diferença simétrica.
# union()                Retorna um novo frozenset contendo a união.copy() -> retorna uma cópia raza
