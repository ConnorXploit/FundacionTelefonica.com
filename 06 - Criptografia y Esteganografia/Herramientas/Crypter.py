import argparse
from math import sqrt
from numpy import matrix
from numpy import linalg

ALFABETO = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz 0123456789!$#"

class Crypter:
    
    def __init__(self):
        pass

    # Cifrado de desplazamiento
    def cifrar_desplazamiento(self):
        pass
    
    def descifrar_desplazamiento(self):
        pass

    # Cifrado Cesar
    def cifrar_cesar(self, mensaje, desplazamiento):
        data = []
        for letra in mensaje:
            if letra not in ALFABETO:
                raise Exception("No he podido cifrar la letra `{l}`".format(l = letra))
            i = ALFABETO.index(letra)
            j = (i + desplazamiento) % len(ALFABETO)
            letra_cifrada = ALFABETO[j]
            data.append(letra_cifrada)
        return ''.join(data)

    def descifrar_cesar(self, mensaje, desplazamiento):
        data = []
        for letra in mensaje:
            if letra not in ALFABETO:
                raise Exception("No he podido cifrar la letra `{l}`".format(l = letra))
            i = ALFABETO.index(letra)
            j = (i - desplazamiento) % len(ALFABETO)
            letra_cifrada = ALFABETO[j]
            data.append(letra_cifrada)
        return ''.join(data)

    # Cifrado afin
    def existeInversa(a, n):
        return math.gcd(a, n) == 1

    def getInv(a, n):
        # Calculo la inversa de a en modulo n
        if existeInversa(a, n):
            return euclides(a, n)
        else:
            return None

    def cifrar_afin(self, a, b):
        data = []
        for letra in m:
            if letra not in ALFABETO:
                raise Exception("No he podido cifrar la letra `{l}`".format(l = letra))
            i = ALFABETO.index(letra)
            j = ( (i * a) + b) % len(ALFABETO)
            letra_cifrada = ALFABETO[j]
            data.append(letra_cifrada)
        return ''.join(data)
    
    def descifrar_afin(self, a, b):
        data = []
        for letra in m:
            if letra not in ALFABETO:
                raise Exception("No he podido cifrar la letra `{l}`".format(l = letra))
            i = ALFABETO.index(letra)
            inv = getInv(a, len(ALFABETO))
            if inv is not None:
                j = ( (i - b) * inv ) % len(ALFABETO)
                letra_cifrada = ALFABETO[j]
                data.append(letra_cifrada)
            else:
                return "??????????"
        return ''.join(data)

    # Cifrado vigenere
    def cifrar_vigenere(self, p, k):
        c = ""
        kpos = []
        for x in k:
            kpos.append(alphabets.find(x))
        i = 0
        for x in p:
            if i == len(kpos):
                i = 0
            pos = alphabets.find(x) + kpos[i]
            if pos > 25:
                pos = pos-26
            c += alphabets[pos].capitalize()
            i +=1
        return c
    
    def descifrar_vigenere(self, c, k):
        p = ""
        kpos = []
        for x in k:
            kpos.append(ALFABETO.find(x))
        i = 0
        for x in c:
            if i == len(kpos):
                i = 0
            pos = ALFABETO.find(x.lower()) - kpos[i]
            if pos < 0:
                pos = pos + 26
            p += ALFABETO[pos].lower()
            i +=1
        return p

    # Cifrado Hill
    def cifrar_hill(self, mensaje, clave):
        n = int(sqrt(len(clave)))
        if n * n != len(clave):
            raise Exception("La longitud debe ser posible hacer una raiz cuadrada")
        numeros = dict([(ALFABETO[i], i * 1) for i in range(len(ALFABETO))])

        # Poner mensaje con espacios si es necesario
        if len(mensaje) % n > 0:
            mensaje += '|' * (n - (len(mensaje) % n))
        
        # Construimos una matriz de claves
        lista_claves = []
        for a in clave:
            lista_claves.append(numeros[a])
        
        # Cargamos la matriz
        matriz_claves = [] 
        for i in range(n):
            matriz_claves.append(lista_claves[i * n : i * n + n])

        matriz_claves = matrix(matriz_claves).round().T
        return mensaje
    
    def descifrar_hill(self):
        pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--mensaje")
    parser.add_argument("-C", "--criptografia")
    parser.add_argument("-D", "--desplazamiento")
    parser.add_argument("-c", "--cifrar", action="store_true")
    parser.add_argument("-d", "--descifrar", action="store_true")
    parser.add_argument("-a", "--decimacion")
    args = parser.parse_args()

    cr = Crypter()

    # Comprobar mensaje
    if not args.mensaje:
        raise Exception("Debes indicar un mensaje (-m)")
    else:
        if not args.criptografia:
            raise Exception("Debes indicar una criptografía (-C)")
        else:
            if not args.cifrar and not args.descifrar:
                raise Exception("Debes indicar que hacer... Descifrar o cifrar (-d / -c)")
            else:
                cripto = args.criptografia.lower()
                if cripto == 'cesar':
                    if not args.desplazamiento:
                        raise Exception("Debes indicar un desplazamiento para esta criptografia (-D)")
                    else:
                        desplazamiento = args.desplazamiento
                        try:
                            desplazamiento = int(args.desplazamiento)
                        except ValueError:
                            raise ValueError("El desplazamiento debe ser numerico")
                        if args.cifrar: # Comprobar desplazamiento a int()
                            cr.cifrar_cesar(mensaje=args.mensaje, desplazamiento=desplazamiento)
                        else:
                            cr.descifrar_cesar(mensaje=args.mensaje, desplazamiento=desplazamiento)
                elif cripto == 'afin':
                    if not args.desplazamiento:
                        raise Exception("Debes indicar un desplazamiento para esta criptografia (-D)")
                    else:
                        if args.cifrar:
                            cr.cifrar_afin(mensaje=args.mensaje, desplazamiento=args.desplazamiento)
                        else:
                            cr.descifrar_afin(mensaje=args.mensaje, desplazamiento=args.desplazamiento)
                elif cripto == 'vigenere':
                    if not args.desplazamiento:
                        raise Exception("Debes indicar un desplazamiento para esta criptografia (-D)")
                    else:
                        if args.cifrar:
                            cr.cifrar_afin(mensaje=args.mensaje, desplazamiento=args.desplazamiento)
                        else:
                            cr.descifrar_afin(mensaje=args.mensaje, desplazamiento=args.desplazamiento)
                elif cripto == 'hill':
                    pass
                else:
                    raise Exception("Criptografia incorrecta... (Validos: cesar, afin, vigenere o hill)")

    if args.cifrar:
        # Cifro
        c = cifrar(args.mensaje, decimacion, desplazamiento)
        print("{m} ({a},{b}): {c}".format(
            m = args.mensaje,
            a = decimacion,
            b = desplazamiento, 
            c = c
        ))
    else:
        if args.descifrar:
            # Descifro
            if args.fuerzabruta:
                pass
            else:
                d = descifrar(args.mensaje, decimacion, desplazamiento)
                print("{m} ({a},{b}): {d}".format(
                    m = args.mensaje,
                    a = decimacion,
                    b = desplazamiento, 
                    d = d
                ))
        else:
            raise Exception("Debes indicar cifrar o descifrar")