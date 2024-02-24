# Tuplas

As tuplas são semelhantes as listas, porém, eles são imutáveis

```py
# declarandon uma tupla
tuplaA = (1, 2, 3, 4, 5)

# acessando o elemento da tupla
primeiro_elemento = tuplaA[0]
```

## Operações com tuplas

### Concatenação de tuplas

```py
# concatenação de tuplas
tuplaA = (1, 2, 3, 4)
tuplaB = ("a", "b", "c", "d")

tupla_concatenada = tuplaA + tuplaB
```

### Repetição de tuplas

```py
# repetição de tupla
tuplaA = (1, 2)

tupla_repetida = tuplaA * 3
```

## Métodos de tuplas

```py
tupla = (1, 2, 3, 1, 2, 1)
ocorrencias_de_1 = tupla.count(1)  # Retorna 3
```
