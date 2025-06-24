# Herança em POO (Programação Orientada a Objetos) é um conceito que permite criar novas classes baseadas em classes existentes, reutilizando e estendendo seu comportamento. Isso promove a reutilização de código e a criação de hierarquias de classes.
# Herança Simples: Uma classe herda de uma única classe base.
# Herança Múltipla: Uma classe herda de várias classes base.
# Herança Multinível: Uma classe herda de uma classe base, que por sua vez herda de outra classe base.
# Herança Híbrida: Combina herança simples e múltipla.

# Exemplo de Herança Simples
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        return f"{self.nome} faz um som."
    
class Cachorro(Animal):
    def fazer_som(self):
        return f"{self.nome} late."
class Gato(Animal):
    def fazer_som(self):
        return f"{self.nome} mia."
    
# Exemplo de Herança Múltipla
class Mamifero:
    def amamentar(self):
        return "Amamentando."

class Cachorro(Mamifero):
    def fazer_som(self):
        return f"{self.nome} late."

class Gato(Mamifero):
    def fazer_som(self):
        return f"{self.nome} mia."

# Exemplo de Herança Multinível
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        return f"{self.nome} faz um som."
class Mamifero(Animal):
    def amamentar(self):
        return "Amamentando."
class Cachorro(Mamifero):
    def fazer_som(self):
        return f"{self.nome} late."
class Gato(Mamifero):
    def fazer_som(self):
        return f"{self.nome} mia."

# Exemplo de Herança Híbrida
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        return f"{self.nome} faz um som."
class Mamifero(Animal):
    def amamentar(self):
        return "Amamentando."   
class Ave(Animal):
    def voar(self):
        return f"{self.nome} está voando."
class Pinguim(Ave, Mamifero):
    def fazer_som(self):
        return f"{self.nome} faz um som de pinguim."
    
# Exemplo de uso das classes
cachorro = Cachorro("Rex")  
print(cachorro.fazer_som())  # Saída: Rex late.
gato = Gato("Mia")
print(gato.fazer_som())  # Saída: Mia mia.
mamifero = Mamifero("Bicho")
print(mamifero.amamentar())  # Saída: Amamentando.
pinguim = Pinguim("Pingu")
print(pinguim.fazer_som())  # Saída: Pingu faz um som
print(pinguim.voar())  # Saída: Pingu está voando.  