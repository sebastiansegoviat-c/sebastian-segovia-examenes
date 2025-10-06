"""
Utilizar el concepto de módulo necesariamente. Y escribir un programa para el
manejo de listas el cuál cumplirá los siguientes requerimientos (2 ptos):
"""
import random

def almacenar_numeros():
    while True:
        try:
            valor = int(input("índica los numeros aleatorios que quieres generar: "))
            lista = [random.randint(1, 50) for _ in range(valor)]
            print(f"Tu lista es: {lista}")
            return lista
        except ValueError:
            print("Valor no valido")

def no_repetidos(lista_1):
    no_repetidos = list(set(lista_1))
    print(f"La lista sin rrepetir es: {no_repetidos}")
    return no_repetidos

def orden_listas(lista):
    mayor_menor = sorted(lista, reverse=True)
    menor_mayor = sorted(lista)
    print(f"Numeros de mayor a menor: {mayor_menor}")
    print(f"Numeros de menor a mayor: {menor_mayor}")
    return mayor_menor, menor_mayor

def mayor_par(lista):
    num_par = [num for num in lista if num % 2 == 0]
    if num_par:
        mayor = max(num_par)
        print(f"El mayor numero par es: {mayor}")
        return mayor
    else:
        print("No hay números pares")
        return None