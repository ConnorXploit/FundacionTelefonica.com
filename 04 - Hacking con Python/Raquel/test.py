
lista = ["hola", 3, True, "8"]



while True:
    nb = input("introduce un valor: ")
    
    try:
        nb = int(nb)
        nb = int(nb)
        nb = int(nb)
        nb = int(nb)
        nb = int(nb)
        nb = int(nb)

    except ValueError:
        # No es un entero
        print("No es un entero, prueba otra vez")
    except Exception as e:
        print(e)


    if nb in lista:
        print("El valor {v} está en la lista: {l}".format(v = nb, l = lista))
    else:
        pass

print("Esto no se ejecutará nunca")