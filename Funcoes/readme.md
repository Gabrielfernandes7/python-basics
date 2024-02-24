# Funções

## Definindo uma função

```py
def nome_da_funcao(parametro1, parametro2, ...):
    # Corpo da função
    # Código a ser executado
    return resultado
```

### Função que aceita um número variável de argumentos

```py
def imprimirArgumentos(*args):
    for arg in args:
        print(arg)

imprimirArgumentos(1, 2, 3, 4, "Ola")
```

## Documentação da função

```py
def minha_funcao(parametro):
    """
    Documentação da função.
    Explica o que a função faz, seus parâmetros e o que ela retorna.
    """
    # Corpo da função
```
