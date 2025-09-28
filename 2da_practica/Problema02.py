"""
- Crear una función normalizar_nombres(nombres)
- El parámetro recibe una lista de string de nombres (6 como mínimo)
- Este quitará el espacio antes y después si lo hubiera
- Convierte en tipo título
- Si hubiera más nombre los debe separar (si debe haber el caso en el input de
datos)
- Devuelve también eliminando duplicados manteniendo el orden de la primera
- No mutará la lista original
"""

nombres = []
nombre_1 = input("Introduce un nombre: ")
nombre_2 = input("Introduce un nombre: ")
nombre_3 = input("Introduce un nombre: ")
nombre_4 = input("Introduce un nombre: ")
nombre_5 = input("Introduce un nombre: ")
nombre_6 = input("Introduce un nombre: ")

nombres.extend([nombre_1, nombre_2, nombre_3, nombre_4, nombre_5, nombre_6])


nombres_finales = []
def normalizar_nombres(nombres):
    for nombre in nombres:
        nombre_strip = nombre.strip()
        nombre_titulo = nombre_strip.title()
        nombres_finales.append(nombre_titulo)

    nombre_sin_repetir = []
    for nombre in nombres_finales:
        if nombre not in nombre_sin_repetir:
            nombre_sin_repetir.append(nombre)
    return nombre_sin_repetir

resultado = normalizar_nombres(nombres)

print(f"La lista inicial, sin modificar, es {nombres}")
print(f"La lista final es {resultado}")

