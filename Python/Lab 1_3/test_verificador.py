import pytest
from verificador import (
    comprueba_longitud,
    comprueba_simbolos,
    comprueba_numero,
    comprueba_espacios,
    validar_password
)

# --- Tests individuales de funciones básicas ---

def test_comprueba_longitud():
    assert comprueba_longitud("abcd1234") is True
    assert comprueba_longitud("abc") is False

def test_comprueba_simbolos():
    assert comprueba_simbolos("abc123") is True
    assert comprueba_simbolos("abc@123") is False
    assert comprueba_simbolos("abc#123") is False

def test_comprueba_numero():
    assert comprueba_numero("abc123") is True
    assert comprueba_numero("abcdef") is False

def test_comprueba_espacios():
    assert comprueba_espacios("abc123") is True
    assert comprueba_espacios("abc 123") is False

# --- Test de la función principal validar_password ---

@pytest.mark.parametrize(
    "password,expected",
    [
        ("abc12345", True),        # válida
        ("abc123", False),         # demasiado corta
        ("abcdefghi", False),      # sin número
        ("abc@1234", False),       # contiene símbolo prohibido
        ("abc 1234", False),       # contiene espacio
    ]
)
def test_validar_password(password, expected):
    assert validar_password(password) == expected
