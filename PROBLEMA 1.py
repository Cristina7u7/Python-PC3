def porcentaje(fraccion):
    try:
        x, y = fraccion.split('/')
        x = int(x)
        y = int(y)
        
        # Las condiciones
        if y == 0:
            raise ZeroDivisionError("Y debe ser diferente de 0")
        if x > y:
            raise ValueError("X debe ser menor o igual a Y")
                
        # Porcentaje:
        porcentaje = (x / y) * 100
        
        # Casos especiales: E y F
        if porcentaje <= 1:
            return 'E'
        elif porcentaje >= 99:
            return 'F'
        else:
            return f"{round(porcentaje)}%"
    except ValueError:
        print("Error: Ingrese una fracción que sea de números enteros.")
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
    return None

if __name__ == "__main__":
    while True:
        fraccion = input("Ingrese cualquier fracción (X/Y): ")
        result = porcentaje(fraccion)
        if result:
            print("Resultado:", result)
            break