#! /usr/bin/python3

# Permitir que se ingresen las 3 notas
n1 = int(input("Ingrese la primera nota"))
n2 = int(input("Ingrese la segunda nota"))
n3 = int(input("Ingrese la tercera nota"))
# Calcular el promedio
promedio = (n1 + n2 + n3) / 3
# Mostrar el promedio
print("Promedio:", promedio)
# Determinar si aprobó
if promedio < 6 or n3 < 6:
    situacion = "Reprobado"
else:
    situacion = "Aprobado"

# Mostrar si aprobó
print("La situación del estudiante es:",situacion)
