# Disease Simulator

This Python project simulates the effects of diseases on a person's health and the use of medication to treat those diseases. The simulation involves diseases that affect the number of threatened cells, temperature changes, and the attenuation of diseases over time.

## Disease Types

### Infections Diseases (e.g., Malaria)

- **Effect:** Increases the infected person's temperature by a fraction of the threatened cells.
- **Reproduction:** Infections diseases can reproduce by doubling the number of threatened cells.

### Autoimmune Diseases (e.g., Lupus)

- **Effect:** Decreases the number of threatened cells.

## Person

A person in the simulation has the following attributes:

- Temperature
- Number of cells
- List of diseases

## Operations

The project includes the following operations:

1. **Infecting and Living a Day:** You can make a person contract multiple diseases and simulate a day in their life to observe the effects of diseases.
2. **Disease Attenuation:** You can attenuate specific diseases and check if the person is healthy.
3. **Medication:** The person can receive medication to treat the diseases they have.

## Example Usage

```python
from Medicina import Medicina
from Enfermedad import Infecciosa, Autoinmune
from Persona import Persona

enfermedad1 = Infecciosa('malaria', 5000)
enfermedad2 = Autoinmune('lupus', 10000)
persona1 = Persona(36, 3000000, enfermedad1, 8)

# Simulate a day in the person's life
persona1.enfermar(enfermedad2)
enfermedad2.atenuar(500)
persona1.enfermar(enfermedad1)
enfermedad1.atenuar(5000)
persona1.medicar(Medicina(300))

# Check if the person is healthy
print(persona1.estaSano())
