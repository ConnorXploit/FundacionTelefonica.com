# -*- coding: utf-8 -*-
"""
ALGORITMO 4
Indica el valor de la variable X al finalizar el proceso siguiente:
Inicio
Datos:
A, B, X, Y, Z entero
Código:
A=15
B=15
X=100
Y=100
Z=0
Mientras(A==B) hacer
A=A+3
Mientras(X==Y) hacer
X=X+Z
Fin Mientras
B=B+3
Fin Mientras
Fin
"""
#Declaración de variables globales
A = 15
B = 15
X = 100
Y = 100
Z = 0
#Declaración de funciones
#Cuerpo principal del programa
while (A == B):
        A = A + 3
        if (X == Y):
            X = X + Z
        else:
            B = B + 3       
# prints out X
print ("El valor de X es ",X)

 
