
ruta = "ejemplo.txt"

# datos = [
#     {"nombre": "pepe", "edad": 30}, {"nombre": "maria", "edad":31}
# ]

# fw = open(ruta, 'w')

# for persona in datos:
#     fw.write("nombre = {n}\n".format(n = persona['nombre']))
#     fw.write("edad = {e}\n".format(e = persona['edad']))
#     fw.write('###\n')

# fw.close()

####

personas = []
f = open(ruta, 'r')
p = {}
for line in f.readlines():
    if "###" in line.strip():
        personas.append(p)
        p = {}
    else:
        label = line.split("=")[0].strip()
        valor = line.split("=")[1].strip()
        p[label] = valor
    

print(personas)
