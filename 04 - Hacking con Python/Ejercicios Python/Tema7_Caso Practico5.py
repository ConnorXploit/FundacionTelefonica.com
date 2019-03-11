# -*- coding: utf-8 -*-
"""
ALGORITMO 5
Indica el valor de la variable Z al finalizar el proceso siguiente:
Inicio
Datos:
A, B, X, Y, Z entero
Código:
A=60
B=0
X=100
Y=100
Z=100
Mientras(A<>B) hacer
A=A+10
Mientras(X==Y) hacer
X=X+Z
Fin Mientras
B=B+20
A=A-10
Y=X
Fin Mientras
Fin
"""
#Declaración de variables globales
A = 60
B = 0
X = 100
Y = 100
Z = 100
#Declaración de funciones
#Cuerpo principal del programa
while (A != B):
        A = A + 10
        if (X == Y):
            X = X + Z
        else:
            B = B + 20
            A = A - 10
            Y = X
# prints out Z
print ("El valor de Z es ",Z)