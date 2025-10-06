from modulo import almacenar_numeros, no_repetidos, orden_listas, mayor_par

lista1 = almacenar_numeros()
no_repetidos1 = no_repetidos(lista1)
orden1_mayor, orden1_menor = orden_listas(no_repetidos1)
mayor_par1 = mayor_par(no_repetidos1)

print("\n--------------------------------------------------------------_-")

lista2 = almacenar_numeros()
no_repetidos2 = no_repetidos(lista2)
orden2_mayor, orden2_menor = orden_listas(no_repetidos2)
mayor_par2 = mayor_par(no_repetidos2)