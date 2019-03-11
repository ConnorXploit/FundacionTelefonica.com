import dns
import dns.resolver
import argparse
import sys


def resolveDNS(domain, reg = 'A'):
    print("resolveDNS({domain}, {reg})".format(**locals()))
    ans = dns.resolver.query(domain, reg)
    targets = set()
    for rdata in ans:
        try:
            targets.add(rdata.address)
        except:
            pass
    return targets

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--domain", help="Dominio a buscar")
    parser.add_argument("-r", "--reg")
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args()

    print(args.verbose)

    if not args.domain:
        print("Por favor, introduce un dominio")
        sys.exit(-2)

    print(resolveDNS(args.domain, args.reg))


    
