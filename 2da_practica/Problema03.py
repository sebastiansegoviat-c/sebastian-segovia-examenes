"""
Crea un programa en Python que implemente una función llamada
convertir_precio(texto: str) -> float que (4 ptos):
1. Reciba un string que representa un precio en soles (ejemplo: "123.50",
"45", "20.99").
2. Intente convertirlo a un número decimal (float).
3. Tenga las siguientes excepciones:
o Si el texto está vacío, debe lanzar un ValueError("El precio no
puede estar vacío").
o Si el texto contiene caracteres inválidos (ejemplo: "abc",
"12a3"), debe lanzar un ValueError("Formato de precio inválido").
o Si el número es negativo, debe lanzar un ValueError("El precio no
puede ser negativo"). - El programa debe pedir tres precios al usuario, usar la función
convertir_precio y almacenarlos en una lista. - Finalmente, mostrar:
o La lista con los precios convertidos.
o El precio promedio de los tres valores ingresados.
"""


def convertir_precio(lista_precios):
    lista_precios_convertidos = []
    for precio in lista_precios:
        if precio.strip() == "":
            float("")

        precio_float = float(precio)
        if precio_float < 0:
            float("valor incorrecto")
        lista_precios_convertidos.append(precio_float)
    return lista_precios_convertidos

lista_precios = []
while True:
    try:
        precio_1 = input("Ingresa una precio: ")
        precio_2 = input("Ingresa una precio: ")
        precio_3 = input("Ingresa una precio: ")
        lista_precios.extend([precio_1, precio_2, precio_3])
        resultado_verificar = convertir_precio(lista_precios)
        break
    except ValueError as e:
        if "could not convert string to float" in str(e):
            print("El valor no es numérico")
        elif "''" in str(e):
            print("El valor no puede estar vacio")
        elif "'valor incorrecto'" in str(e):
            print("El valor no puede ser negativo")

        lista_precios = []
resultado_final = convertir_precio(lista_precios)
print(f"Los precios finales son: {resultado_final}")
