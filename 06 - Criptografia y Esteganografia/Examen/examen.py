import argparse

def separarPor(contenido, separador):
    return contenido.split(separador)

def unirPor(piezas, separador):
    return separador.join(piezas)

def readBinaryFiles(path):
    f = open(path, 'rb')
    contenido = f.read()
    f.close()
    return contenido

def writeBinaryFile(path, contenidoBinario):
    f = open(path, 'wb')
    f.write(contenidoBinario)
    f.close

def definirExtension(cabecera):
    if b"\xFF\xD8" in cabecera: return "JPG"
    elif b"\x89\x50\x4E\x47\x0D\x0A\x1A\x0A" in cabecera: return "PNG"
    elif b"\xEC\xA5\xC1\x00" in cabecera: return "DOC"
    elif b"\x25\x50\x44\x46" in cabecera: return "PDF"
    elif b"\x49\x44\x33" in cabecera: return "MP3"
    elif b"\x52\x49\x46\x46" in cabecera: return "WAV"
    elif b"\x90\x00" or b"\x4D\x5A\x50\x00" in cabecera: return "EXE"
    elif b"\x30\x26\xB2\x75" in cabecera: return "WMV"
    elif b"\x47\x49\x46\x38\x39\x61" or b"\x37\x61" in cabecera: return "GIF"
    elif b"\x50\x4B\x03\x04" in cabecera: return "ZIP"
    else: return None

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--ocultar", help = "Indique el archivo a ocultar")
    parser.add_argument("-e", "--extraer", help = "Indique el archivo del que se quiere sacar la información")
    parser.add_argument("-b", "--bindear", help = "Indique el archivo al que se le acoplará el otro fichero")
    parser.add_argument("-g", "--guardar", help = "Indique el nombre de archivo al extraer")
    args = parser.parse_args()

    if args.ocultar is None and args.extraer is None:
        raise Exception("Selecciona alguna opcion")

    if args.ocultar is not None:
        if args.bindear is None:
            raise Exception("Debes indicar un archivo para bindear")
        else:
            fichero1 = readBinaryFiles(args.bindear)
            fichero2 = readBinaryFiles(args.ocultar)
            piezas = [fichero1, fichero2]
            ficheroStego = unirPor(piezas, b"")
            writeBinaryFile('oculto_{fichero}'.format(fichero=args.bindear), ficheroStego)
            print("Fichero 'oculto_{fichero}' creado".format(fichero=args.bindear))

    if args.extraer is not None:
        contenido = readBinaryFiles(args.extraer)
        cabecera = contenido[0:20]
        print("Analizando tipo de fichero introducido...")
        extension = definirExtension(cabecera)
        separador = b"\xFF\xD9"
        piezas = separarPor(contenido, separador)
        contenidoOculto = unirPor(piezas[1:], separador)
        if args.guardar is not None:
            writeBinaryFile(args.guardar, contenidoOculto)
            print("Se ha generado el archivo '{nom}' con la información oculta en el fichero inicial".format(nom=args.guardar))
        else:
            writeBinaryFile('output2.{ext}'.format(ext=definirExtension(contenidoOculto[0:20])), contenidoOculto)
            print("Se ha generado el archivo 'output2.txt' con la información oculta en el fichero inicial")