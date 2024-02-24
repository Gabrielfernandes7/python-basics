conjuntoA = {2, 4, 6, 8, 10}
conjuntoB = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(f"Conjunto A: {conjuntoA}")

print(f"Conjunto B: {conjuntoB}")

print("Adicionando elemento 12 no conjunto A")
conjuntoA.add(12)

print("Removendo elemento 7 no conjunto B")
conjuntoB.remove(7)

conjuntoC = conjuntoA.union(conjuntoB)
print(f"Interseção de AB: {conjuntoC}")

intersectionAB = conjuntoA.intersection(conjuntoB)
print(f"Interseção de AB: {intersectionAB}")

diferencaAB = conjuntoA.symmetric_difference(conjuntoB)
print(f"Diferença entre conjuntos A e B: {diferencaAB}")
