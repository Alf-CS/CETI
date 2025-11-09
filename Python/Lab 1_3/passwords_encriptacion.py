# Este programa permite almacenar y recuperar contraseñas de forma segura utilizando cifrado simétrico con la biblioteca 'cryptography'.
# Asegúrate de tener instalada la biblioteca 'cryptography' ejecutando: pip install cryptography
# El programa genera una clave secreta la primera vez que se ejecuta y la guarda en 'key.key'.
# Las contraseñas cifradas se almacenan en 'passwords.txt'.
# Puedes añadir nuevas contraseñas y listar las contraseñas descifradas a través de un menú interactivo.
# Importante: Mantener segura la clave en 'key.key', ya que es necesaria para descifrar las contraseñas.

from cryptography.fernet import Fernet
import os
from verificador import validar_password   # Importamos la función de validación desde el módulo externo verificador.py
#Vamos a reutilizar el código del verificador del ejercicio 1 (Lab_2_1) para validar las contraseñas antes de guardarlas.

# --- Generar o cargar la clave secreta ---
def load_key():
    """Carga la clave de cifrado desde 'key.key', o la genera si no existe."""
    if not os.path.exists("key.key"):
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:   # 'wb' = write binary
            key_file.write(key)
    else:
        with open("key.key", "rb") as key_file:
            key = key_file.read()
    return key


def add_password(password, fernet):
    """Cifra y guarda la contraseña en passwords.txt."""
    encrypted = fernet.encrypt(password.encode())
    with open("passwords.txt", "ab") as file:  # 'ab' = append binary
        file.write(encrypted + b"\n")


def list_passwords(fernet):                     #fernet es el objeto de cifrado
    """Lee y descifra las contraseñas guardadas."""
    if not os.path.exists("passwords.txt"):
        return []
    with open("passwords.txt", "rb") as file:
        lines = file.readlines()
    return [fernet.decrypt(line.strip()).decode() for line in lines]

# Vamos a crear la comprobación de contraseña robusta
# VAmos a usar el codigo del ejercicio 1 (Lab_2_1) para validar las contraseñas antes de guardarlas
# Utilizaremos las mismas funciones de validación


def main():
    key = load_key()
    fernet = Fernet(key)

    while True:
        print("\n--- Menú ---")
        print("1. Añadir contraseña")
        print("2. Listar contraseñas")
        print("3. Salir")

        choice = input("Elige una opción: ")

        if choice == "1":
            password = input("Introduce la contraseña que deseas añadir: ")
            if validar_password(password):  # Validamos la contraseña antes de guardarla llamanado a la función del módulo verificador.py
                add_password(password, fernet)
                print("Contraseña cifrada y guardada.")
            else:
                print("La contraseña ha fallado la validación y no se ha guardado.")


        elif choice == "2":
            passwords = list_passwords(fernet)
            if not passwords:
                print("No hay contraseñas guardadas.")
            else:
                print("\nContraseñas guardadas (descifradas):")
                for pw in passwords:
                    print(pw)
        elif choice == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":  #__name__ es una variable especial en Python que indica si el archivo se está ejecutando como programa principal
    main()                  #Si el archivo se está ejecutando como programa principal, llama a la función main()


