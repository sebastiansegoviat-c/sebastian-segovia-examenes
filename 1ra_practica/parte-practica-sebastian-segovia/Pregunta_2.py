#Caso 2: Reporte de calificaciones

matematicas = 17
ciencias = 14
historia = 15

prom_mat = (matematicas * 40)/100
prom_cie = (ciencias * 30)/100
prom_his = (historia * 30)/100

nota_final = prom_mat + prom_cie + prom_his
print("La nota final es: {}".format(f"{nota_final:.1f}"))

print("_____________________________________________________________________________________________")
Aprobado = True
Desaprobado = False

if nota_final >= 13:
    print("¿Aprobado?: {}".format(Aprobado))
if nota_final < 13:
    print("¿Aprobado?: {}".format(Desaprobado))

print("_____________________________________________________________________________________________")
print("El resumen es el siguiente:")
print("El estudiante obtuvo una nota final de {} y su estado final es: Aprobado".format(nota_final))

