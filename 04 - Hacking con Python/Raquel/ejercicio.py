#!/usr/bin/env python
# -*- coding: utf8 -*-


def readFile(path):
    """
    Lee un fichero y devuelve una estructura con la informacion contenida
    """
    f = open(path, 'r')
    item = {}
    data = []
    for line in f.readlines():
        line = line.replace("\n", "").strip()
        if line.startswith("-----"):
            # nuevo elemnto
            data.append(item)
            item = {}
        elif line.startswith("#") or len(line) == 0:
            # Comentarios
            continue
        else:
            # Datos validos
            fields = line.split("=")
            clave = fields[0].strip()
            valor = fields[1].strip()
            item[clave] = valor 
    f.close()
    return data

def buscar(datos, valor):
    """
    Busca en `datos`, un elemento cuya clave `dni` se corresponda con valor.
    Una vez encontrado, lo devuelve. Si no lo encuentra, devuelve None
    """
    for item in datos:
        try:
            if str(item['dni']) == str(valor):
                return item 
        except KeyError:
            pass
        except ValueError:
            pass
    return None


def mostrar(item):
    """
    Muestra un elemento por pantalla
    """
    print("Informacion del elemento\n")
    for k in item.keys():
        print("{k}: {v}".format(k = k, v = item[k]))
    print("*" * 20)


if __name__ == "__main__":

    path = "personas.txt"
    data = readFile(path)
    
    dni = input("Introduce un DNI: ")

    p = buscar(data, dni)
    if p is not None:
        mostrar(p)
    else:
        print("Persona no encontrada!")

