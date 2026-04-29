import pytest
from app.calculator import aplicar_descuento

# Caso Exitoso (Happy Path)
def test_aplicacion_cupon_valido():
    assert aplicar_descuento(100, "DESC10") == 90.0

# Caso de Error (Excepción por código inexistente)
def test_error_cupon_inexistente():
    with pytest.raises(ValueError, match="Código de descuento inválido"):
        aplicar_descuento(100, "NO_EXISTE")

# Caso Borde (Monto en el límite inferior)
def test_monto_limite_cero():
    assert aplicar_descuento(0, "DESC20") == 0.0

# Caso Borde/Error (Monto fuera de rango)
def test_error_monto_negativo():
    with pytest.raises(ValueError, match="El monto no puede ser negativo"):
        aplicar_descuento(-1, "DESC10")