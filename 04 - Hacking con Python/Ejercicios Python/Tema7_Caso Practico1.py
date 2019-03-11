# -*- coding: utf-8-*-
"""
Práctica 1: TEMA 7,ALGORITMO 1
Indica el valor de las variables A y B al finalizar el siguiente
algoritmo:
Inicio
Datos:
A, B, C entero
Código:
A=7
B=4
C=9
Mientras (A<>C) hacer
Si (C>9) entonces
B=B+5
Sino
A=A+2
Fin Si
Fin Mientras
Fin
"""
#Declaración de variables globales
A = 7
B = 4
C = 9
#Declaración de funciones
#Cuerpo principal del programa
while (A != C):
    if (C > 9):
        B = B + 5
    else:
        A = A + 2  
# prints out 1,2,3
print (A)
print (B)
 