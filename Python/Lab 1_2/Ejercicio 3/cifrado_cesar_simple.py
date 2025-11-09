# Lista del alfabeto en mayúsculas (referencia)
alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
            'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
            'Y', 'Z']

def cifrado_cesar(texto, desplazamiento):
    texto_cifrado = ""
    for char in texto:
        # Si es una letra del alfabeto (mayúscula)
        if char in alfabeto:
            indice = alfabeto.index(char)
            nuevo_indice = (indice + desplazamiento) % len(alfabeto)
            texto_cifrado += alfabeto[nuevo_indice]
        # Si es uno de los caracteres permitidos que se copian tal cual
        elif char in [' ', ',', '.', ':']:
            texto_cifrado += char
        # Cualquier otro carácter (por ejemplo letra minúscula, ñ, acentos, otros símbolos)
        else:
            return "Todos los caracteres deben estar en mayúsculas y dentro del alfabeto."
    return texto_cifrado

# Validación del código:
mensaje_valido = "HOLA MUNDO."
print(cifrado_cesar(mensaje_valido, 3))   # Resultado esperado: "KROD PXQGR."

mensaje_invalido = "Hola Mundo"  # contiene minúsculas -> error
print(cifrado_cesar(mensaje_invalido, 3))  # Resultado: mensaje de error
