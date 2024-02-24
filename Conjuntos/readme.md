# Conjuntos

## Criando um conjunto

```py
conjuntoA = {1, 2, 3, 4, 5, 6}
```

```py
conjuntoB = set([1, 2, 3])
```

## Operações básicas com conjuntos

### Adição de elementos

```py
conjuntoA.add(6)
```

### Remoção de elementos

```py
conjuntoB.remove(6)
```

### Verificação de pertencimento

```py
if elemento in conjuntoB:
    return True
```

## Funções e métodos úteis

### União de conjuntos
```py
conjuntoA = {1, 2, 3}
conjuntoB = {3, 4, 5}
uniao = conjuntoA.union(conjuntoB)

# ou utilizando o operador "|"
uniao = conjuntoA | conjuntoB
```

### Interseção de conjuntos

```py
intersecao = conjuntoA.intersection(conjuntoB)

# ou utilizando o operador &
intersection = conjuntoA & conjuntoB
```

### Diferenças de conjuntos

```py
diferenca = conjunto1.difference(conjunto2)
# ou usando o operador -
diferenca = conjunto1 - conjunto2
```

### Conjuntos de elementos diferentes

```py
diferentes = conjunto1.symmetric_difference(conjunto2)
# ou usando o operador ^
diferentes = conjunto1 ^ conjunto2
```

### Verificação de Subconjunto ou Superconjunto

```py
if conjunto1.issubset(conjunto2):
    print("conjunto1 é um subconjunto de conjunto2")
    
if conjunto2.issuperset(conjunto1):
    print("conjunto2 é um superconjunto de conjunto1")
```

## Observação

* Os elementos de um conjunto devem ser imutáveis (por exemplo, inteiros, strings, tuplas), mas o próprio conjunto é mutável.
* Como os conjuntos não são ordenados, não se pode acessar elementos por índice ou fazer slicing.
* Conjuntos não suportam elementos mutáveis, como listas ou outros conjuntos.
