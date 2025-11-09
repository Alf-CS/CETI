alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
            'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
            'Y', 'Z']

def descifrado_cesar(texto, desplazamiento):
    texto_descifrado = ""
    for char in texto:
        if char in alfabeto:
            indice = alfabeto.index(char)
            nuevo_indice = (indice - desplazamiento) % len(alfabeto)
            texto_descifrado += alfabeto[nuevo_indice]
        elif char in [' ', ',', '.', ':']:
            texto_descifrado += char
        else:
            return "Todos los caracteres deben estar en mayúsculas y dentro del alfabeto."
    return texto_descifrado


# Pruebas de validación del código:
mensaje_valido = "KROD PXQGR."
print(descifrado_cesar(mensaje_valido, 3))   # Resultado esperado: "HOLA MUNDO."

mensaje_no_valido = "Hola Mundo"  # contiene minúsculas -> error
print(descifrado_cesar(mensaje_no_valido, 3))  # Resultado: mensaje de error