# -*- coding: utf-8 -*-
"""
ALGORITMO 6
Indica el valor al que habrá que inicializar P para que al finalizar
el proceso el valor que se imprima de X sea 10:
Inicio:
Datos:
X, P entero
Código:
X=0
P=?
Mientras(P<=7) hacer
X=X+1
P=P+1
Fin Mientras
Mostrar “El valor de X es “, X
Fin
"""
#Declaración de variables globales
X = 0
P = -3
#Declaración de funciones
#Cuerpo principal del programa
while (P != 7) and (X != 10):
        X = X + 1
        P = P + 1
        # prints out X
print ("El valor de X es ",X)


