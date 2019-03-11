import socket

IP_RANGE = "192.168.1"
ports = [21, 22, 25, 53, 79, 80, 110, 443, 8080, 9050]
for host in range(204, 206):
    for port in ports:
        try:
            ip = IP_RANGE + "." + str(host)

            print("Creando socket a {ip}:{p}".format(ip = ip, p = port))

            # Crear un objeto socket
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1) # Tiempo maximo de espera
            s.connect((ip, port)) # Conexion. Recibe tupla!!
            
            banner = s.recv(1024) # Recibe datos

            print("Banner encontrado en {ip}:{p}".format(ip = ip, p = port))
            print("Banner = {b}".format(b = str(banner)))
        except Exception as e:
            #print("ERROR: {e}".format(e = str(e)))
            pass
