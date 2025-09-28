"""
-  Crear una función llamada procesar_notas(estudiantes) la cual va a recibir
un diccionario donde las claves serán los nombres de los estudiantes y sus
valores serán listas con 3 notas.
- Calcular el promedio de cada estudiante.
- Devolver un nuevo diccionario donde la clave sea el nombre del estudiante
y el valor sea otro diccionario con:
promedio: que será el promedio de notas
estado: “aprobado” si es mayor o igual a 11, “desaprobado” si es menor - Mostrar en pantalla el estudiante con mayor promedio
"""

datos_estudiantes = {'jose': [15, 13, 17], 'amira': [13, 12, 16], 'sergio': [18, 12, 16]}
print("La lista de datos es: {}".format(datos_estudiantes))
print("_________________________________________________________________-")
lista_notas = list(datos_estudiantes.values())

def procesar_notas(datos_estudiantes):
    promedios = {}

    for estudiante, notas in datos_estudiantes.items():
        promedio = sum(notas) / len(notas)
        promedios[estudiante] = promedio
    return promedios

promedio_final = procesar_notas(datos_estudiantes)
for estudiante, promedio in promedio_final.items():
    estado = ""
    if promedio >= 11:
        estado = "aprobado"
    else:
        estado = "desaprobado"
    print(f"{estudiante} tiene un promedio de: {promedio:.2f} y su estado es: {estado}")
print("_________________________________________________________________-")
mayor_promedio = 0
mejor_estudiante = ""
for estudiante, promedio in promedio_final.items():
    if promedio > mayor_promedio:
        mayor_promedio = promedio
        mejor_estudiante = estudiante

print(f"El mayor promedio es de {mejor_estudiante} con {mayor_promedio:.2f}")

