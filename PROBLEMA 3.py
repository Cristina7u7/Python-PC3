import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        return math.pi * (self.radio ** 2)

if __name__ == "__main__":
    try:
        r1 = float(input("Ingrese el radio del 1er círculo en metros: "))
        r2 = float(input("Ingrese el radio del 2do círculo en metros: "))
        
        circulo1 = Circulo(r1)
        circulo2 = Circulo(r2)
        
        print(f"El área del círculo con radio {circulo1.radio} es: {circulo1.calcular_area():.2f} en metros cuadrados")
        print(f"El área del círculo con radio {circulo2.radio} es: {circulo2.calcular_area():.2f} en metros cuadrados")
    
    except ValueError:
        print("Error: Ingrese correctamente el valor numérico para el radio")