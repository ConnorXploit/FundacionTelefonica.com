#!/usr/bin/python
import nmap
try:
    nma = nmap.PortScannerAsync()
    def callback_result(host, scan_result):
        print('------------------')
        print('{}: {}'.format(host, scan_result))

    try:
        nma.scan('192.168.1.9', '20-25', arguments='-sT -sV -Pn -A -T5', callback=callback_result)
        while nma.still_scanning():
            print("Waiting >>>")
            nma.wait(2)
    except:
        print('ERROR')
except:
    print('Error... Fin del programa')