import random  # Para generar un número aleatorio

# 1. Generamos un número aleatorio entre 1 y 10
numero_secreto = random.randint(1, 10)

# 2. Inicializamos la variable para almacenar la suposición del usuario y mostramos un mensaje inicial
suposicion = None

print("¡Adivina el número entre 1 y 10!")

# 3. Usamos un bucle while hasta que el usuario acierte
while suposicion != numero_secreto:
    # Pedimos un número al usuario y lo forzamos a entero
    suposicion = int(input("¿Cuál crees qué es?: "))

    # 4. Verificamos la suposición y damos retroalimentación
    if suposicion < numero_secreto:
        print("Demasiado bajo. Intenta de nuevo.")
    elif suposicion > numero_secreto:
        print("Demasiado alto. Intenta de nuevo.")
    else:
        print("¡Correcto! El número es el ", numero_secreto)
