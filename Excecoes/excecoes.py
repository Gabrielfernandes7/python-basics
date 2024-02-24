try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Erro: Divisão por zero")
finally:
    print("Execução finalizada")
