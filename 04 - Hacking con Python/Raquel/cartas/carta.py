#!/usr/bin/env python
# -*- coding: utf8 -*-

class Carta(object):

    PALOS = ["Oros", "Espadas", "Copas", "Bastos"]

    def __init__(self, valor, palo):
        self.__valor = valor
        self.__palo = palo

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, value):
        self.__valor = value

    @property
    def palo(self):
        if self.__palo not in self.PALOS:
            print("Error! No es un palo valido")
        return self.__palo

    @palo.setter
    def palo(self, value):
        self.__palo = value

    def metodo1(self):
        print("Metodo1")

    def __str__(self):
        return "{v} de {p}".format(v = self.valor, p = self.palo)


