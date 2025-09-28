#Asignar en variables los datos de tu nombre, salario, edad y compañía para un usuario e identificar
# sus tipos de variables
nombre = "Sebastian Segovia"
salario = 2100
edad = 19
compañia = "Pfizer"

print("Tu nombre es:", nombre)
print("Tu salario es: {} soles".format(salario))
print("Tu edad es: {} años".format(edad))
print("Tu compañia es: ", compañia)
print("________________________________________")
print("La clase de 'nombre' es: {}".format(type(nombre)))
print("La clase de 'salario' es: {}".format(type(salario)))
print("La clase de 'edad' es: {}".format(type(edad)))
print("La clase de 'compañia' es: {}".format(type(compañia)))

print("________________________________________")
#Identificar si la edad es mayor a 30, mostrar un mensaje ingresado “Usted
#tiene un bono de 10% en el mes de diciembre” caso contrario mostrar “Usted
#tiene un bono del 5% en el mes diciembre”

if edad > 30:
    print("Usted tiene un bono del 10% en el mes de diciembre")
else:
    print("Usted tiene un bono del 5% en el mes de diciembre")

print("________________________________________")
#Mostrar el bono final que es: potencia de 2 del salario más el 5 o 10 % de su salario, según corresponda.

bono_final = (salario ** 2) + (salario * 5)/100
print("Tu bono final es de: {} soles".format(f"{bono_final:.0f}"))


