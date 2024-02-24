def soma(a, b):
    return a + b

print(f"33.2 + 23.4 = {soma(33.2, 23.4)}")

# função que aceita mais de um argumento
def quadradoElementos(*args):
    for arg in args:
        arg *= arg
        print(arg)

print("Quadrado dos elementos")
quadradoElementos(1, 2, 3, 4)

# documentação da função
def minhaFuncao(parametro):
    """
    Documentação da função
    Essa funcao serve apenas para retonar o seu parâmetro
    """
    return parametro
