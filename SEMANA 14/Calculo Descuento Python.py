def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

if __name__ == "__main__":
    # Primer llamado con porcentaje por defecto
    monto1 = 100
    descuento1 = calcular_descuento(monto1)
    print(f"Monto total: ${monto1}")
    print(f"Descuento aplicado (10%): ${descuento1}")
    print(f"Monto final a pagar: ${monto1 - descuento1}")

    # Segundo llamado con descuento personalizado
    monto2 = 200
    porcentaje2 = 15
    descuento2 = calcular_descuento(monto2, porcentaje2)
    print(f"\nMonto total: ${monto2}")
    print(f"Descuento aplicado ({porcentaje2}%): ${descuento2}")
    print(f"Monto final a pagar: ${monto2 - descuento2}")
