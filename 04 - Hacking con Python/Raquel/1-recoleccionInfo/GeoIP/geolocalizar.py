
import pygeoip
import argparse

class Geolocalizador(object):

    def __init__(self, filename = 'Geo.db'):
        self.gip = pygeoip.GeoIP(filename)

    
    def getCountryCodeByName(self, domain):
        return self.gip.country_code_by_name(domain)
    
    def getCountryNameByName(self, domain):
         return self.gip.country_name_by_name(domain)

    def getCountryCodeByIp(self, ip):
        return self.gip.country_code_by_addr(ip)
    
    def getCountryNameByIp(self, ip):
        return self.gip.country_name_by_addr(ip)



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--domain", help="Dominio a buscar")
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args()


    geo = Geolocalizador(filename= 'Geo.dat')
    print(geo.getCountryNameByName(args.domain))
