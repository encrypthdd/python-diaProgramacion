from datetime import datetime, timedelta

def dia_de_la_programacion(año):
    # El primer día del año
    fecha_inicio = datetime(año, 1, 1)

    # Contamos hasta 256 días
    fecha_programacion = fecha_inicio + timedelta(days=255)  

    return fecha_programacion

# Solicitar el año al usuario
año = int(input("Introduce el año: "))
fecha = dia_de_la_programacion(año)

# Mostrar el resultado
print(f"El Día de la Programación en el año {año} es el: {fecha.strftime('%d de %B de %Y')}")