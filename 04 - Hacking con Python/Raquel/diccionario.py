
persona = {
    "nombre": "Maria",
    "edad": 29,
    "altura": 1.70,
}

def get_data():
    return "pepe", 30, 1.80









data = get_data()
keys = list(persona.keys())

for i in range(0, len(data)):
    k = keys[i]
    persona[k] = data[i]

print(persona)







print(persona)
# nombre, edad, altura = get_data()
# persona["nombre"] = nombre
# persona["altura"] = altura
# persona["edad"] = edad
# print(persona)


for k in persona.keys():
    print("{k} = {v}".format(k = k, v = persona[k]))


# print(persona["nombre"])
# print(persona["edad"])
# print(persona["altura"])
# print(persona["dni"])

# persona["dni"] = "123456789"
