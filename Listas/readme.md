# Listas

Listas são estruturas de dados que podem armazernar múltiplos items em uma única variável

As listas são mutáveis

## Operaçções com listas

### Adição de elementos

```py
# adiciona elementos no final da lista
lista.append()
```

## Remoção de elementos

```py
# remove o elemento que você passou como argumento
# remove o primeiro elemento da lista
lista.remove(elemento[0])

# remove e armazena o elemento que foi removido
lista.pop(elemento[0])
```

## Fatiamento de listas (Slicing)

A sintaxe básica é lista[início:fim:passo]. Aqui está o que cada parte significa:

início: Índice de início da fatia (incluído).
fim: Índice de fim da fatia (excluído).
passo: Passo ou incremento (opcional).

```py
minha_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(minha_lista[2:5])  # Saída: [3, 4, 5]
print(minha_lista[::2])   # Saída: [1, 3, 5, 7, 9]
print(minha_lista[::-1])  # Saída: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

```
