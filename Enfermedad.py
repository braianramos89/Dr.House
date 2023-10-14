from random import randint


class Enfermedad:
    def __init__(self,nombre):
        self.nombre = nombre

    def efecto(self):
        pass
    def atenuar(self, x):
        pass


class Infecciosa(Enfermedad):
    def __init__(self,nombre, celuAfectadas):
        super().__init__(nombre)
        self.celuAfectadas = 5000

    def efecto(self):
        reproducirse = randint(0,1)
        if reproducirse == 1:
            return self.celuAfectadas * 2
        return self.celuAfectadas / 1000
    def atenuar(self, x):
        self.celuAfectadas -= x
        return f'Se atenuo {self.celuAfectadas}'

class Autoinmune(Enfermedad):
    def __init__(self,nombre, celuAfectadas):
        super().__init__(nombre)
        self.celuAfectadas = 10000

    def efecto(self):
        return self.celuAfectadas / 100

    def atenuar(self, x):
        self.celuAfectadas -= x
        return f'Se atenuo {self.celuAfectadas}'

