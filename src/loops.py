# ============================================================
# MÓDULO 5: Loops
# ============================================================


def contar_hasta(n: int) -> list:
    """
    Retorna una lista con los números del 1 al n (inclusive).
    """
    if n < 0:
        raise ValueError("n debe ser un entero no negativo")
    return list(range(1, n + 1))
    pass


def tabla_multiplicar(n: int) -> list:
    """
    Retorna una lista con los primeros 10 múltiplos de n.
    Ejemplo: tabla_multiplicar(3) -> [3, 6, 9, ..., 30]
    """
    if not isinstance(n, int) or n == 0:
        raise ValueError("n debe ser un entero distinto de cero")
    return [n * i for i in range(1, 11)]
    pass


def suma_digitos(n: int) -> int:
    """
    Retorna la suma de los dígitos de un número entero positivo.
    Ejemplo: suma_digitos(123) -> 6
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("n debe ser un entero no negativo")
    suma = 0
    while n > 0:
        suma += n % 10
        n //= 10
    return suma
    pass


def es_primo(n: int) -> bool:
    """
    Retorna True si n es un número primo.
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Verificar divisores impares hasta sqrt(n)
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True
    pass


def fibonacci(n: int) -> list:
    """
    Retorna los primeros n números de la serie de Fibonacci.
    Ejemplo: fibonacci(6) -> [0, 1, 1, 2, 3, 5]
    """
    if n <= 0:
        return []
    
    resultado = []
    a, b = 0, 1
    for _ in range(n):
        resultado.append(a)
        a, b = b, a + b
    return resultado
    pass
