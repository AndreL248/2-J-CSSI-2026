"""
Nombre :
Grupo  :
Fecha  :
"""
#-------------------------------------------------------------------------#
#Escribir un metodo que acepte el porcentaje de un alumno y evalue el grado de acuerdo al siguiente criterio
#Calificacion	Grado
#   >90				A
#   >80 y <= 90		B
#   >=60 y <=80		C
#   menor a 60		D
print("Porcentajes de calificacion")
porcentaje = int(input("Ingresa tu calificacion: "))

if porcentaje > 90:
    grado = "A"
elif porcentaje > 80 and porcentaje <= 90:
    grado = "B"
elif porcentaje >= 60 and porcentaje <= 80:
    grado = "C"
else:
    grado = "D"

print("Grado:", grado)


#-------------------------------------------------------------------------#
#Escribir un metodo que capture el precio de una bicicleta y muestre los impuestos que debe pagar siguiendo los criterios siguientes:
# Costo					Impuesto
# >100000				15%
# >50000 y <= 100000	10% 
#<=50000				 5%
print("Precio de bicicleta")
precio = int(input("Ingresa el precio: "))
if precio > 100000:
        impuesto = precio * 0.15
elif precio > 50000 and precio <= 100000:
    impuesto = precio * 0.10
else:
    impuesto = precio * 0.05

print("Impuesto a pagar:", impuesto)

#-------------------------------------------------------------------------#
#Escribir un metodo que verifique si un año es bisiesto o no
año = int(input("Ingresa el año actual "))
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")

#-------------------------------------------------------------------------#
#Escribir un metodo que capture un numero del 1 al 7 y muestre el nombre del dia de la semana
#Por ejemplo el 1 seria Domingo y el 2 Lunes
numero = int(input("Ingresa el numero: "))
dias = {
    1: "Domingo",
    2: "Lunes",
    3: "Martes",
    4: "Miercoles",
    5: "Jueves",
    6: "Viernes",
    7: "Sabado"}

if numero in dias:
    print(dias[numero])
else:
    print("Numero invalido")

#-------------------------------------------------------------------------#
#Escribir un metodo que acepte un numero del 1 al 12 y muestre el nombre del mes asi como los dias que contiene
#Ejemplo 1 seria Enero tiene 31 dias
print("Numero de meses")
meses = int(input("Ingresa el mes actual: "))
meses = {
    1: ("Enero", 31),
    2: ("Febrero", 28),
    3: ("Marzo", 31),
    4: ("Abril", 30),
    5: ("Mayo", 31),
    6: ("Junio", 30),
    7: ("Julio", 31),
    8: ("Agosto", 31),
    9: ("Septiembre", 30),
    10: ("Octubre", 31),
    11: ("Noviembre", 30),
    12: ("Diciembre", 31)
}

if numero in meses:
    nombre, dias = meses[numero]
    print(nombre, "tiene", dias, "dias")
else:
    print("Numero invalido")

#-------------------------------------------------------------------------#
#Escribir un programa que imprima los primeros 10 numeros naturales
print("Numeros nturales")
for i in range(1, 11):
    print(i)

#-------------------------------------------------------------------------#
#Escibir un programa que imprima los primeros 10 numeros impares
print("Numeros impares")
for i in range(1, 20, 2):
        print(i)

#-------------------------------------------------------------------------#
#Escribir un programa que imprima los primeros 10 numeros naturales en orden descendente
print("Numeros descendentes")
for i in range(10, 0, -1):
        print(i)
#-------------------------------------------------------------------------#
#Escribir un programa que escriba la tabla de multiplicar de un numero especificado por el usuario
print("Numeros multiplos")
numero = int(input("Ingresa el numero: "))
for i in range(1, 11):
    print(numero, "x", i, "=", numero * i)
#-------------------------------------------------------------------------#
#Escribir un programa que escriba el producto de los digitos de un numero especificado por el usuario
producto = 1

while numero > 0:
        digito = numero % 10
        producto *= digito
        numero //= 10

print("Producto de los digitos:", producto)