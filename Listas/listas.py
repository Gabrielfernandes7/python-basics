# criei minha lista
listaA = ["item 1", "item 2", "item 3"]

# adiciona um item na lista
listaA.append("item 4")

# remove elementos da lista
# remove o primeiro elemento da lista e guarda em uma variável
item_removido_pop = listaA.pop(0)
print(f"O item removido é: {item_removido_pop}")

# remove elementos da lista e não armazena o item removido
item_removido_remove = listaA.remove("item 3")
print(f"O item removido: {item_removido_remove}")

# número de elementos da lista
numero_elementos = len(listaA)
print(f"Número de elementos da lista: {numero_elementos}")

# mostrar todos items da lista por um loop
for item in listaA:
    print(item)
