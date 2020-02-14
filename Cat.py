import Animal


class Cat(Animal.Animal):
    def __init__(self, nombre, tipoSonido):
        Animal.Animal.__init__(self, nombre, tipoSonido)

