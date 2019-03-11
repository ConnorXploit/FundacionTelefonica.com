from scapy.all import *

class EscaneadorPuertos(object):

    def __init__(self, ip, puerto):
        self.ip = ip
        self.puerto = puerto

    def tcp(self):
        # Envio un paquete con SYN
        r = sr1(IP(dst= self.ip )/TCP(dport=int(self.puerto), flags="S"), verbose = 0, timeout = 5)

        if(r is None):
            # Puerto cerrado
            return False
        elif( r.haslayer(TCP) ):
            if(r.getlayer(TCP).flags == 0x12): # SYN + ACK
                r2 = sr1(IP(dst= self.ip)/TCP(dport=int(self.puerto),flags="AR"),verbose = 0, timeout = 5)
                # Puerto abierto
                return True
            elif(r.getlayer(TCP).flags == 0x14): # ACK + RST
                # Puerto cerrado
                return False
            
    def syn(self):
        # Envio un paquete con SYN
        r = sr1(IP(dst= self.ip )/TCP(dport=int(self.puerto), flags="S"), verbose = 0, timeout = 5)
        if r is None:
            # Puerto filtrado
            return False
        elif(r.haslayer(TCP)):
            if(r.getlayer(TCP).flags == 0x12): # SYN + ACK
                r2 = sr1(IP(dst= self.ip)/TCP(dport=int(self.puerto),flags="R"),verbose = 0, timeout = 5)
                # Puerto abierto
                return True
            elif(r.getlayer(TCP).flags == 0x14): # ACK + RST
                # Puerto cerrado
                return False
            elif(r.haslayer(ICMP)):
                if(int(r.getlayer(ICMP).type)==3 and int(r.getlayer(ICMP).code) in [1,2,3,9,10,13]):
                    # Puerto filtrado
                    return False
    
    def udp(self):
        # Envio un paquete UDP vacio
        r = sr1(IP(dst=self.ip)/UDP(dport=int(self.puerto)), verbose = 0, timeout = 5)
        retrans = [r]

        if r is None:
            # Si no obtengo respuesta me preparo para una retransmision
            for count in range(0,3):
                # Añadimos las retransmisiones
                retrans.append( sr1(IP(dst=self.ip)/UDP(dport=int(self.puerto) ) ) )

        for item in retrans:
            if item is not None and  item.haslayer(UDP): # Si existe una respuesta UDP
                # Puerto abierto
                return True
            else:
                # Puerto cerrado
               return False

    def fin(self):
        # Envio un paquete con el flag FIN
        r = sr1(IP(dst=self.ip)/TCP(dport=int(self.puerto),flags="F"), verbose = 0, timeout = 5) # FIN
        if r is None:
            # Puerto abierto|filtrado
            return True
        elif(r.haslayer(TCP) and r.getlayer(TCP).flags == 0x14): # ACK + RST
            # Puerto cerrado
            return False
        elif(r.haslayer(ICMP)):
            if(int(r.getlayer(ICMP).type)==3 and int(r.getlayer(ICMP).code) in [1,2,3,9,10,13]):
                # Puerto filtrado
                return False

    def ack(self):
        """
        Determina si existe un firewall o no
        """
        # Envio un paquete con el flag ACK
        r = sr1(IP(dst=self.ip)/TCP(dport=int(self.puerto),flags="A"), verbose = 0, timeout = 5) # ACK
        if r is None:
            # Puerto filtrado. Seguramente exista un firewall
            return True
        elif(r.haslayer(TCP)):
            if(r.getlayer(TCP).flags == 0x4): # RST
                # No Firewall
                return False
            elif(r.haslayer(ICMP)):
                if(int(r.getlayer(ICMP).type)==3 and int(r.getlayer(ICMP).code) in [1,2,3,9,10,13]):
                    # Hay firewall
                    return True

    def xmax(self):
        # Envio un paquete con los flags FIN PSH y URG
        r = sr1(IP(dst=self.ip)/TCP(dport=int(self.puerto),flags="FPU"), verbose = 0, timeout = 5)
        if r is None:
            # No puedo determinar el estado, lo consideraré filtrado
            # El puerto estará abierto|filtrado
            return True
        elif(r.haslayer(TCP) and r.getlayer(TCP).flags == 0x14): # ACK + RST
            # Puerto cerrado
            return False
        elif(r.haslayer(ICMP)):
            if(int(r.getlayer(ICMP).type)==3 and int(r.getlayer(ICMP).code) in [1,2,3,9,10,13]):
                # Puerto filtrado
                return False

    def hasFirewall(self):
        return self.ack()

    def scan(self):
        print("TCP Scan: {s}".format( s = self.tcp() ))
        print("SYN Scan: {s}".format( s = self.syn() ))
        print("UDP Scan: {s}".format( s = self.udp() ))
        print("FIN Scan: {s}".format( s = self.fin() ))
        print("ACK Scan: {s}".format( s = self.ack() ))
        print("XMAX Scan: {s}".format( s = self.xmax() ))


if __name__ == "__main__":

    ip = "192.168.1.205"
    puerto = 22

    e = EscaneadorPuertos(ip, puerto)

    e.scan()