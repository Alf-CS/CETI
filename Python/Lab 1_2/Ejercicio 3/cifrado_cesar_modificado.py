def cifrado_cesar(texto, desplazamiento):
    resultado = ""
    for char in texto:
        if char.isalpha():  # Solo ciframos letras
            base = 'A' if char.isupper() else 'a'
            resultado += chr((ord(char) - ord(base) + desplazamiento) % 26 + ord(base))
        else:
            resultado += char  # No ciframos espacios ni signos
    return resultado


def descifrado_cesar(texto_cifrado, desplazamiento):
    return cifrado_cesar(texto_cifrado, -desplazamiento)


# Ejemplo de uso
mensaje = "Hola Mundo"
desplazamiento = 3

cifrado = cifrado_cesar(mensaje, desplazamiento)
print("Texto cifrado:", cifrado)

descifrado = descifrado_cesar(cifrado, desplazamiento)
print("Texto descifrado:", descifrado)
