def aplicar_descuento(monto, codigo):
    """
    Calcula el precio final aplicando un cupón.
    Maneja validaciones de monto y existencia de código.
    """
    cupones_validos = {
        "DESC10": 0.10,
        "DESC20": 0.20
    }
    
    # Validación de integridad de datos
    if monto < 0:
        raise ValueError("El monto no puede ser negativo")
    
    # Validación de regla de negocio
    if codigo not in cupones_validos:
        raise ValueError("Código de descuento inválido")
        
    descuento = monto * cupones_validos[codigo]
    return monto - descuento