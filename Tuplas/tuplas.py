tuplaA = (1, 2, 3, 4, 4, 4, 5)
tuplaB = ("a", "b", "c", "d")

tupla_concatenada = tuplaA + tuplaB

print(tupla_concatenada)

ocorrencias_do_quatro = tuplaA.count(4)
print(f"O 4 se repetiu: {ocorrencias_do_quatro}")

# imutabilidade das tuplas
tuplaC = (1, 2, 3)
tuplaC[0] = -1

try:
    # Tenta modificar a tupla
    tuplaC[0] = 5
except TypeError:
    # Trata o erro caso a tentativa de modificação falhe
    print("Não é possível modificar uma tupla. Convertendo para lista...")
