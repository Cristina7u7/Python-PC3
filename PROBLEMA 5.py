class Alumno:
    def __init__(self, nombre, registro):
        self.nombre = nombre
        self.registro = registro
        self.edad = None
        self.nota = None
    
    def display(self):
        print(f"Nombre: {self.nombre}")
        print(f"Número de Registro: {self.registro}")
        if self.edad is not None:
            print(f"Edad: {self.edad}")
        if self.nota is not None:
            print(f"Nota: {self.nota}")
    
    def set_age(self, edad):
        self.edad = edad
    
    def set_nota(self, nota):
        self.nota = nota

if __name__ == "__main__":
    nombre = input("Ingrese el nombre del alumnx: ")
    registro = input("Ingrese el número de registro del alumnx: ")

    alumno = Alumno(nombre, registro)

    print("\nInformación inicial del alumnx:")
    alumno.display()
    
    try:
        edad = int(input("Ingrese la edad del alumnx: "))
        alumno.set_age(edad)
        
        nota = float(input("Ingrese la nota del alumnx: "))
        alumno.set_nota(nota)
    
    except ValueError:
        print("Error: Ingrese solo valores numéricos válidos para la edad y la nota.")
    
    print("\nInformación actualizada del alumnx:")
    alumno.display()