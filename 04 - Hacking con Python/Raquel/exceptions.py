lista = [1,2]
try:
    
   pass



except ValueError:
    print("Zoquete! introduce un numero!")
except Exception as e:
    print("ERROR!!! ----> "+str(e))
finally:
    # Limpieza
    # Destruir variables
    # Cerrar ficheros/conexiones
    print("Finally")



print("Sigo ejecutandome")