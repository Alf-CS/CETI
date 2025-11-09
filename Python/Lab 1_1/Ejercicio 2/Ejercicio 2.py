# Agenda de contactos
# Vamos a utilizar un diccionario para almacenar los contactos de una agenda telefónica.

# Cada contacto tendrá un nombre como clave y un número de teléfono como valor.
# El programa debe permitir al usuario:
# 1. Agregar un nuevo contacto.
# 2. Buscar un contacto por su nombre.
# 3. Eliminar un contacto.
# 4. Mostrar todos los contactos.
# 5. Salir del programa.

# FUNCIONES USADAS Y RELACIONADAS
# Estructuras de control: while, if, elif, else, for
# Funciones básicas: print(), input(), len(), range(), break, continue
# Manejando texto: input(), strip(), capitalize(), title(), upper(), lower()
# Manejando diccionario: dict(), keys(), values(), items(), in, del

# definimos el diccionario
agenda = {}

def mostrar_menu():
    print("\n\n --- AGENDA DE CONTACTOS ---")
    print("1 -  Agregar contacto")
    print("2 -  Buscar contacto")
    print("3 -  Eliminar contacto")
    print("4 -  Mostrar todos los contactos")
    print("5 -  Salir")

while True:
    mostrar_menu()
    opcion = input("Elige una opción (1-5): ")

                                                    # CARGAR AGENDA DESDE UN ARCHIVO AL INICIO DEL PROGRAMA
                                                    # Habría que comprobar si el archivo existe y cargar los datos en el diccionario agenda
    if opcion == "1":
        nombre = input("Nombre del contacto: ").strip().capitalize()
        telefono = input("Número de teléfono: ").strip()
        if nombre in agenda:
            print("ESTE CONTACTO YA EXISTE. Verifica nombre y teléfono nuevos.")
        else:
            agenda[nombre] = telefono
            print(f"Contacto '{nombre}' agregado correctamente.")

    elif opcion == "2":
        nombre = input("Nombre del contacto a buscar: ").strip().capitalize()
        if nombre in agenda:
            print(f"{nombre}: {agenda[nombre]}")
        else:
            print("ATENCIÓN: Contacto no encontrado.")

    elif opcion == "3":
        nombre = input("Nombre del contacto a eliminar: ").strip().capitalize()
        if nombre in agenda:
            del agenda[nombre]
            print(f"🗑️ Contacto '{nombre}' eliminado.")
        else:
            print("ERROR: No existe ese contacto.")

    elif opcion == "4":
        if agenda:
            print("\n Lista de contactos:")
            for nombre, telefono in agenda.items():
                print(f"- {nombre}: {telefono}")
        else:
            print("AVISO: La agenda está vacía.")

    elif opcion == "5":
        print("CERRANDO AGENDA")
        break 
        # Salir del bucle y terminar el programa
                                                            # AÑADIR CODIGO PARA GUARDAR LA AGENDA EN UN ARCHIVO

    else:
        print("OPCIÓN NO VÁLIDA. Intenta de nuevo.")
