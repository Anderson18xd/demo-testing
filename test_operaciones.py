 # test_operaciones.py
import pytest
from operaciones import dividir, calcular_descuento

def test_dividir_exitoso():
    assert dividir(10, 2) == 5.0
    assert dividir(9, 3) == 3.0

def test_dividir_por_cero():
    # Verificamos que Python lance la excepción correcta cuando dividimos por cero
    with pytest.raises(ValueError, match="No se puede dividir entre cero."):
        dividir(10, 0)

def test_calcular_descuento():
    assert calcular_descuento(100, 20) == 80.0
    assert calcular_descuento(200, 50) == 100.0