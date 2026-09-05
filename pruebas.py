"""Funciones sencillas del proyecto para validar mediante pruebas automatizadas."""


def sumar(primer_numero: float, segundo_numero: float) -> float:
    """Devuelve la suma de dos numeros."""
    return primer_numero + segundo_numero


def es_par(numero: int) -> bool:
    """Indica si un numero entero es par."""
    return numero % 2 == 0


def saludar(nombre: str) -> str:
    """Construye un saludo para la persona indicada."""
    return f"Hola, {nombre}!"