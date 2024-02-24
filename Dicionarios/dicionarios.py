dicionario_vazio = {}

dicionario_por_dict = dict(chave1="valor1", chave2="valor2")

meu_dicionario = {
    "nome": "João",
    "idade": 60
}

print("Nome e idade de joão")
print(meu_dicionario["nome"])
print(meu_dicionario["idade"])

# adicionando elemento
meu_dicionario["cidade"] = "Fortaleza"

# atualizando idade
meu_dicionario["idade"] = 50

print(meu_dicionario)

# removendo um elemento
del meu_dicionario["idade"]
cidade = meu_dicionario["cidade"]

print(meu_dicionario)
print(cidade)

# iterando sobre odicionário
for chave, valor in dicionario_por_dict.items():
    print(chave, valor)

# verificando a existência de uma chave
meu_dicionarioA = {'nome': 'João', 'idade': 60, 'cidade': 'Fortaleza'}

if "nome" in meu_dicionario:
    print("A chave existe")
