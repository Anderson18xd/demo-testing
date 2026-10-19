# operaciones.py

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero.")
    return a / b

def calcular_descuento(precio, porcentaje):
    if precio < 0 or porcentaje < 0:
        raise ValueError("Los valores no pueden ser negativos.")
    return precio - (precio * (porcentaje / 100))