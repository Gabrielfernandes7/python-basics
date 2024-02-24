# Dicionários

Dicionários são estruturas de dados que permitem armazenar pares de chaves-valor.

## Criando dicionários

```py
# criando um dicionário vazio
dicionario_vazio = {}
```

```py
# criando um dicionário com pares de chave-valor
meu_dicionario = {'chave1': 'valor1', 'chave2': 'valor2', 'chave3': 'valor3'}
```

```py
# criando um dicionário com a função dict
outro_dicionario = dict(chave1='valor1', chave2='valor2')
```

## Acessando valores

```py
meu_dicionario = {'nome': 'João', 'idade': 60, 'cidade': 'Fortaleza'}

# acessando valores
print(meu_dicionario['nome'])   # Saída: João
print(meu_dicionario['idade'])  # Saída: 60
```

## Adicionando e atualizando os elementos

```py
meu_dicionario = {'nome': 'João', 'idade': 60}

# adicionando um novo par chave-valor
meu_dicionario['cidade'] = 'Fortaleza'

# atualizando o valor de uma chave existente
meu_dicionario['idade'] = 50

print(meu_dicionario)  # saída: {'nome': 'João', 'idade': 50, 'cidade': 'Fortaleza'}
```

## Removendo elemento

```py
# removendo um par chave-valor
meu_dicionario = {'nome': 'João', 'idade': 60, 'cidade': 'Fortaleza'}
del meu_dicionario["idade"]

# removendo e retornando o valor de uma chave específica
cidade = meu_dicionario.pop('cidade')

print(meu_dicionario)  # Saída: {'nome': 'João'}
print(cidade)          # Saída: Fortaleza
```

## Iterando sobre o dicionário

```py
meu_dicionario = {'nome': 'João', 'idade': 60, 'cidade': 'Fortaleza'}

# iterando sobre chaves
for chave, valor in meu_dicionario.items():
    print(chave, valor)
```

## Verificando a existência de uma chave

```py
meu_dicionario = {'nome': 'João', 'idade': 60, 'cidade': 'Fortaleza'}

if "nome" in meu_dicionario:
    print("A chave existe")
```
