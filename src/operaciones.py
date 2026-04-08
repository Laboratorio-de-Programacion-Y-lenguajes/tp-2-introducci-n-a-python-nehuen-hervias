# ============================================================
# MÓDULO 7: Operaciones con Strings
# ============================================================


import string


def es_palindromo(texto: str) -> bool:
    """
    Retorna True si el texto es palíndromo (ignorando espacios y mayúsculas).
    Ejemplo: es_palindromo("Anita lava la tina") -> True
    """
    cleaned = texto.replace(' ', '').lower()
    return cleaned == cleaned[::-1]
    


def capitalizar_palabras(texto: str) -> str:
    """
    Capitaliza la primera letra de cada palabra.
    Ejemplo: capitalizar_palabras("hola mundo") -> "Hola Mundo"
    """
    palabras = texto.split()
    return ' '.join(palabra.capitalize() for palabra in palabras)
    


def contar_vocales(texto: str) -> int:
    """
    Retorna la cantidad de vocales (a,e,i,o,u) en el texto,
    sin distinguir mayúsculas/minúsculas.
    """
    contador = 0
    for caracter in texto.lower():
        if caracter in 'aeiou':
            contador += 1
    return contador
    


def caesar_cipher(texto: str, desplazamiento: int) -> str:
    """
    Aplica el cifrado César al texto con el desplazamiento dado.
    Solo desplaza letras (a-z, A-Z), los demás caracteres no cambian.
    Ejemplo: caesar_cipher("abc", 1) -> "bcd"
    """
    resultado = ""
    minusculas = string.ascii_lowercase
    mayusculas = string.ascii_uppercase
    
    for char in texto:
        if char in minusculas:
            idx = minusculas.index(char)
            resultado += minusculas[(idx + desplazamiento) % 26]
        elif char in mayusculas:
            idx = mayusculas.index(char)
            resultado += mayusculas[(idx + desplazamiento) % 26]
        else:
            resultado += char
    
    return resultado
    
