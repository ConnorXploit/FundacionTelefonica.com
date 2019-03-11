# -*- coding: utf-8-*-
"""
ALGORITMO 2
Indica los valores de las variables X, Y y Z al finalizar el siguiente
proceso.
Inicio
Datos:
X entero
Y entero
Z entero
Seguimiento de algoritmos
Caso práctico
Código:
X=0
Y=7
Z=-4
Mientras (X > Z) hacer
Si (Y<15) entonces
Y=Y+4
Sino
Si(Z<0) entonces
Z=Z+2
Sino
Z=Z+1
X=X-1
Fin si
Y=Y+3
Fin si
Fin mientras
Fin
"""
X = 0
Y = 7
Z = -4
#Declaración de funciones
#Cuerpo principal del programa
while (X > Z):
    if (Y < 15):
        Y = Y + 4
        if (Z < 0):
            Z = Z +2
    else:
       Z = Z + 1
       X = X + 1 
Y = Y + 3
# prints out X,Y,Z
print ("El valor de X es",X)
print ("el valor de Y es",Y)
print ("el valor de Z es",Z)
