# Exceções

## Tratamento de Exceções:

Em Python, você pode lidar com erros usando blocos `try`, `except` e `finally`.

O bloco try é onde você coloca o código que pode gerar uma exceção.

O bloco except é usado para capturar e lidar com exceções que ocorrem dentro do bloco try.

O bloco finally é opcional e é usado para executar código, independentemente de ocorrer uma exceção ou não.

## Utilizando tratamento de exceção

```py
try:
    # bloco de código que pode gerar uma exceção
    resultado = 10 / 0
except ZeroDivisionError:
    # bloco de código para lidar com a exceção ZeroDivisionError
    print("Erro: Divisão por zero!")
finally:
    # bloco de código opcional que sempre é executado
    print("Execução finalizada.")
```
