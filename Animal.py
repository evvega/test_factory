
class Animal:
    __nombre: str
    __tipoSonido: str

    def __init__(self, nombre, tipoSonido):
        self.__nombre = nombre
        self.__tipoSonido = tipoSonido

    def getNombre(self):
        print(self.__nombre)

    def makeSound(self):
        print([self.__tipoSonido for i in range(1, 5)])


