# Polimorfismo com Herança 
# O polimorfismo com herança permite que subclasses implementem ou sobrescrevam métodos definidos na superclasse, possibilitando que objetos de diferentes classes sejam tratados de forma uniforme.

class Animal:
    def fazer_som(self):
        raise NotImplementedError("Subclasses devem implementar este método")

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

