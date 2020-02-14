import Animal


class Dog(Animal.Animal):

    def __init__(self, nombre, tipoSonido):
        Animal.Animal.__init__(self, nombre, tipoSonido)

    def makeSound(self):
        return self.makeSound()

