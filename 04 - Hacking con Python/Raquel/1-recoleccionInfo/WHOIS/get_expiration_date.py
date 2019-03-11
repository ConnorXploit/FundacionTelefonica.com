import argparse
import whois


def getDate(domain):
    x = whois.whois(domain)
    dates = x.expiration_date
    if dates is not None:
        return dates[0]
    else:
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--domain", help="Dominio a buscar")
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args()


    print(getDate(args.domain))
   


    
