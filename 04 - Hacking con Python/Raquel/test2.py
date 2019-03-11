
def get_data_tradicional():
    return ("pepe", 30, 1.80)

def get_data():
    return "pepe", 30, 1.80


# Forma tradicional
mi_tupla = get_data_tradicional()
nombre = mi_tupla[0]
edad = mi_tupla[1]
altura = mi_tupla[2]

print(nombre)
print(edad)
print(altura)

# Forma Python
nombre, edad, altura = get_data()

print(nombre)
print(edad)
print(altura)