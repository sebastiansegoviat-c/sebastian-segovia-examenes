#Caso 3: Calculadora de propinas

while True:
    try:
        cuenta = float(input("La cuenta total es de: "))
        propina = float(input("El porcentaje de propina que desea dejar es de: "))
        personas = int(input("El número de personas que dividiran la cuenta es de: "))

        cuenta_total = float(cuenta + (cuenta * propina) / 100)

        if type(cuenta) == float and type(propina) == float:
            print("____________________________________________________________________________")
            print("El monto total con propina es de: S/.{} soles".format(f"{cuenta_total:.2f}"))
        else:
            print("Los valores de la cuenta y la propina deben ser decimales, ingrese un nuevo número")

        if type(personas) == int:
            print("Cada persona debe pagar: S/.{} soles".format(f"{cuenta_total / personas:.2f}"))
        if cuenta_total / personas > 100:
            print("¡Advertencia! El monto por persona supera los S/. 100")
        break

    except ValueError:
        print("Por favor, ingrese valores númericos")
