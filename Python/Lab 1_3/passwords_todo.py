from cryptography.fernet import Fernet
import os

# --- Generar o cargar la clave secreta ---
def load_key():
    """Carga la clave de cifrado desde 'key.key', o la genera si no existe."""
    if not os.path.exists("key.key"):
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
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


def list_passwords(fernet):
    """Lee y descifra las contraseñas guardadas."""
    if not os.path.exists("passwords.txt"):
        return []
    with open("passwords.txt", "rb") as file:
        lines = file.readlines()
    return [fernet.decrypt(line.strip()).decode() for line in lines]


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
            add_password(password, fernet)
            print("✅ Contraseña cifrada y guardada.")
        elif choice == "2":
            passwords = list_passwords(fernet)
            if not passwords:
                print("⚠️ No hay contraseñas guardadas.")
            else:
                print("\nContraseñas guardadas (descifradas):")
                for pw in passwords:
                    print(pw)
        elif choice == "3":
            print("👋 Saliendo del programa.")
            break
        else:
            print("❌ Opción no válida.")


if __name__ == "__main__":
    main()
