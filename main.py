from Medicina import Medicina
from Enfermedad import *
from Persona import Persona

enfermedad1 = Infecciosa('malaria', 5000)
enfermedad2 = Autoinmune('lupus', 10000)
persona1 = Persona(36,3000000,enfermedad1, 8)
print(persona1.estaSano())
print('------------------------------------------------')
persona1.enfermar(enfermedad2)
enfermedad2.atenuar(500)
print(persona1.estaSano())
print('------------------------------------------------')
persona1.enfermar(enfermedad1)
enfermedad1.atenuar(5000)
print(persona1.estaSano())
print('------------------------------------------------')
persona1.medicar(Medicina(300))
print(persona1.estaSano())