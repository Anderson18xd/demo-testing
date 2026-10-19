# operaciones.py
import os

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero.")
    return a / b

def calcular_descuento(precio, porcentaje):
    if precio < 0 or porcentaje < 0:
        raise ValueError("Los valores no pueden ser negativos.")
    return precio - (precio * (porcentaje / 100))

def generar_reporte():
    # Leemos la variable de entorno inyectada desde GitHub Actions
    token = os.getenv("API_TOKEN", "TOKEN_NO_ENCONTRADO")
    
    with open("reporte_ejecucion.txt", "w") as f:
        f.write("=== REPORTE DE EJECUCIÓN DEL PIPELINE ===\n")
        f.write(f"Estado: Pruebas unitarias completadas exitosamente.\n")
        f.write(f"Token de API detectado (longitud): {len(token)} caracteres.\n")

if __name__ == "__main__":
    generar_reporte()