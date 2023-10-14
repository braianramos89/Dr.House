
class Persona:
    def __init__(self, temperatura, cantCelu, enfermedad, dias):
        self.temperatura = temperatura
        self.cantCelu = cantCelu
        self.enfermedad = enfermedad
        self.dias = dias
        self.cantCeluAfectadas = 0

    def medicar(self,medicina):
        self.cantCelu += medicina.efecto()
        return f'Se medicó y ahora tiene {self.cantCelu} celulas'
    def enfermar(self, enfermedad):
        self.enfermedad = enfermedad
        return f'Ahora tiene {self.enfermedad.nombre}'

    def estaSano(self):
        for i in range(self.dias):

            if self.enfermedad.nombre == 'malaria':
                self.temperatura += self.enfermedad.efecto()
                self.cantCeluAfectadas = self.enfermedad.celuAfectadas
            if self.enfermedad.nombre == 'lupus':
                self.cantCelu -= self.enfermedad.efecto()

        if self.cantCeluAfectadas <= 0:
            return f'Esta sano y tiene {self.cantCelu} celulas'
        return f'Esta enfermo y tiene {self.cantCelu} celulas y {self.cantCeluAfectadas} celulas afectadas'