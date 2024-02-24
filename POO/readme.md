# POO (Programação Orientada à Objetos)

## Classe

É um modelo para criar objetos

```py
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
```

## Objeto

É uma instância de uma classe

```py
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

carro1 = Carro("Toyota", "Corolla")

print(carro1.marca) # Toyota
```

## Método

São funções definidas dentro de uma classe que representam comportamentos dos objetos.

```py
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def acelerar(self):
        print("Acelerando...")


carro1 = Carro()
carro1.acelerar()  # Saída: Acelerando...
```

## Herança

Permite que uma classe herde atributos e métodos de outra classe. 
A classe que herda é chamada de classe filha ou subclasse.

```py
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def acelerar(self):
        print("Acelerando...")

class CarroEletrico(Carro):
    def __init__(self, marca, modelo, autonomia):
        super().__init__(marca, modelo)
        self.autonomia = autonomia
```

## Polimorfismo

Permite que objetos de diferentes classes que compartilham o mesmo método tenham comportamentos diferentes.

```py
class Animal:
    def som(self):
        pass

class Cachorro(Animal):
    def som(self):
        print("Au au!")

class Gato(Animal):
    def som(self):
        print("Miau!")

def fazer_som(animal):
    animal.som()

cachorro = Cachorro()
gato = Gato()

fazer_som(cachorro)  # Saída: Au au!
fazer_som(gato)      # Saída: Miau!
```