# Polimorfismo em Python é a capacidade de diferentes classes responderem ao mesmo método de maneira diferente. Isso é alcançado através da herança e da sobrescrita de métodos. O polimorfismo permite que você escreva código mais flexível e reutilizável, onde o mesmo método pode ser chamado em diferentes objetos, cada um com seu próprio comportamento.

class Animal:
    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        return "Au Au"

class Gato(Animal):
    def fazer_som(self):
        return "Miau"

def emitir_som(animal):
    print(animal.fazer_som())

cachorro = Cachorro()
gato = Gato()

emitir_som(cachorro)
emitir_som(gato)