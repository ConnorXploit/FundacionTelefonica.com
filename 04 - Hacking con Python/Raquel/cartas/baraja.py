#!/usr/bin/env python
# -*- coding: utf8 -*-

from .carta import Carta
import random

class Baraja:

    def __init__(self):
        self.cartas = self.initialize()
        self.barajar()

    def initialize(self):
        cartas = []
        for i in range(1,11):
            for p in Carta.PALOS:
                c = Carta(valor = i, palo = p)
                cartas.append(c)
        return cartas

    def barajar(self):
        random.shuffle(self.cartas)

    def __str__(self):
        st = ""
        for c in self.cartas:
            st += str(c)
            st += "\n"
        return st


if __name__ == "__main__":

    b = Baraja()

    print(b)