import shodan
import argparse


SHODAN_API_KEY = "XXX" # Hay que registrarse y coger una licencia

api = shodan.Shodan(SHODAN_API_KEY)

def buscar(palabra):
    return api.search(palabra)



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--search", help="Termino a buscar")
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args()


    r = buscar(args.search)
    print("Resultados: {total}".format(total = r['total']))
    data = r['matches']
    print("Resultados obtenidos: {data}".format(data = len(data)))

    for item in data:
        print("{i}:{p}".format(i = item['ip_str'], p = item['port']))
        
