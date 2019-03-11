# -*- coding: utf-8 -*-

import os
import copy

def menu():
    print('''
	1- Añadir nombre del alumno
	2- Buscar alumno
	3- Eliminar alumno
	4- Mostrar alumnos
	5- Mostrar alumnos alfabéticamente
	9- Salir
	''')

def existeAlumno(alumnos, alumno):
	for al in alumnos:
		if al==alumno:
			return True
	return False
	
def aniadirAlumno(alumnos, alumnosMaximos):
    limpiarConsola()
    print('-- [AÑADIENDO ALUMNO] --')
    if len(alumnos)<alumnosMaximos:
        nombreAlumno=input('Introduce un nombre de alumno: ')
        if not existeAlumno(alumnos, nombreAlumno):
            alumnos.append(nombreAlumno)
            print('Añadido correctamente')
        else:
            print('[ERROR AÑADIENDO ALUMNO] El alumno ya existe!')
    else:
        print('[ERROR AÑADIENDO ALUMNO] La agenda está llena. No podemos añadir mas alumnos')

def buscarAlumno(alumnos, alumnosMaximos):
    limpiarConsola()
    print('-- [BUSCANDO ALUMNO] --')
    existe=False
    if len(alumnos)>0:
        nombreAlumno=input('Introduce un nombre de alumno: ')
        if nombreAlumno in alumnos:
            print('El alumno si existe!')
            existe=True
        if not existe:
            print('[ERROR BUSCANDO ALUMNO] El alumno {} NO existe'.format(nombreAlumno))
    else:
        print('[ERROR BUSCANDO ALUMNO] La lista está vacía')

def eliminarAlumno(alumnos, alumnosMaximos):
    limpiarConsola()
    print('-- [ELIMINANDO ALUMNO] --')
    eliminado=False
    if len(alumnos)>0:
        nombreAlumno=input('Introduce un nombre de alumno: ')
        if nombreAlumno in alumnos:
            alumnos.remove(nombreAlumno)
            print('El alumno ha sido eliminado!')
            eliminado=True
        alumnos=filter(None, alumnos)
        if not eliminado:
            print('[ERROR ELIMINANDO ALUMNO] El alumno no existe en la agenda')
    else:
        print('[ERROR ELIMINANDO ALUMNO] La lista está vacía')

def mostrarAlumnos(alumnos, alumnosMaximosm, onlyFirstPrint):
    limpiarConsola()
    if not onlyFirstPrint:
        print('-- [MOSTRANDO ALUMNOS] --')
    if len(alumnos)>0:
        for alumno in alumnos:
            if alumno:
                print('- {} - '.format(alumno))
    else:
        print('[ERROR MOSTRANDO ALUMNOS] La lista está vacía')

def mostrarAlumnosOrdenados(alumnos, alumnosMaximos):
	limpiarConsola()
	print('-- [MOSTRANDO ALUMNOS ORDENADOS] --')
	if len(alumnos)>0:
		clonAlumnos = copy.copy(alumnos)
		clonAlumnos.sort()
		mostrarAlumnos(clonAlumnos, alumnosMaximos, True)
	else:
		print('[ERROR MOSTRANDO ALUMNOS] La lista está vacía')

def limpiarConsola():
	try:
		os.system('cls' if os.name=='nt' else 'clear')
	except ValueError:
		pass

alumnosMaximos=5
opcionSeleccionada=0

alumnos=[]
limpiarConsola()

while opcionSeleccionada!=9:
	menu()
	opcionSeleccionada = input('Selecciona un elemento del menú:')
	try:
		if opcionSeleccionada == "1":
			aniadirAlumno(alumnos, alumnosMaximos)
		elif opcionSeleccionada == "2":
			buscarAlumno(alumnos, alumnosMaximos)
		elif opcionSeleccionada == "3":
			eliminarAlumno(alumnos, alumnosMaximos)
		elif opcionSeleccionada == "4":
			mostrarAlumnos(alumnos, alumnosMaximos, False)
		elif opcionSeleccionada == "5":
			mostrarAlumnosOrdenados(alumnos, alumnosMaximos)
		elif opcionSeleccionada == "9":
			break
		else:
			limpiarConsola()
			print('No has elegido una opción correcta')
	except ValueError:
		print('Not a number')