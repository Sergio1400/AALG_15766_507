def calcular_cambio(monto, denominaciones):
    print("\nCambio necesario:")
    for valor in denominaciones:
        cantidad = int(monto // valor)
        if cantidad > 0:
            print(str(cantidad) + " de $" + str(valor))
            monto = monto - (cantidad * valor)
            monto = round(monto, 2)

denominaciones = [200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05]
monto = float(input("Ingrese el monto a pagar: "))
cambio = calcular_cambio(monto,denominaciones)