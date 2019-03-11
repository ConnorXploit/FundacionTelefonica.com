import nmap
from socket import inet_aton
import struct

nm = nmap.PortScanner()

nm.scan(hosts='192.168.1.205')
#nm.scan(hosts='192.168.1.205', ports='10-100')
hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
hosts_ord = []

for host, status in hosts_list:
    if status in 'up':
        hosts_ord.append(host)

hosts_ord = sorted(hosts_ord, key=lambda ip: struct.unpack("!L", inet_aton(ip))[0])
for h in hosts_ord:
    host_msg = '{}: '.format(h)
    protocolos = ['tcp','udp']
    for proto in protocolos:
        try:
            if nm[h][proto]:
                host_msg = '{}[{}] - '.format(host_msg, proto.upper())
                port_listed = ''
                cont_ports = 0
                for port in nm[h][proto]:
                    if nm[h][proto][port]['state'] == "open":
                        cont_ports = cont_ports + 1
                        port_listed = '{}{},'.format(port_listed, port)
                host_msg = '{}Se han encontrado {} puertos: {}'.format(host_msg, cont_ports, port_listed)
                # Quitamos la ultima coma:
                host_msg = host_msg[:-1]
                print(host_msg)
        except:
            pass
