# Verificador de contraseña segura

# password = "longitud$"
# Sustituir la cadena con la password a evaluar
password = input("Introduce la contraseña a evaluar: ")
# mejor con input para probar distintas contraseñas


def comprueba_longitud(cadena):
    if len(cadena)>=8:
        return True
    else:
        return False
    
def comprueba_simbolos(cadena):
    if ("@" not in cadena) and ("#" not in cadena):
        return True
    else:
        return False

def comprueba_numero(cadena):
    for caracter in cadena:
        if caracter.isdigit():
            return True
    return False

def comprueba_espacios(cadena):
    if " " not in cadena:
        return True
    else:
        return False    
    

longitud_ok=comprueba_longitud(password)
simbolos_ok=comprueba_simbolos(password)
numero_ok=comprueba_numero(password)
sin_espacios_ok=comprueba_espacios(password)    

# Evaluar seguridad
if longitud_ok and simbolos_ok and numero_ok and sin_espacios_ok:
    print("Contraseña segura.")
else:
    print("Contraseña insegura o incorrecta. Revise las siguientes condiciones:")
    if not longitud_ok:
        print("- Debe tener al menos 8 caracteres.")
    if not simbolos_ok:
        print("- No debe contener '@' ni '#'.")
    if not numero_ok:
        print("- Debe contener al menos un número.")
    if not sin_espacios_ok:
        print("- No debe contener espacios.")
