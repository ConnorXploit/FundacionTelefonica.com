import argparse
import requests

def doRequest(url, method, data = None):
    if method.upper() not in ['GET', 'POST']:
        raise Exception("Metodo no permitido")
    
    if method.lower() == 'get':
        return requests.get(url)
    elif method.lower() == 'post':
        return requests.post(url, data=data)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url")
    parser.add_argument("-m", "--method")
    parser.add_argument("-d", "--data")
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args()


    r = doRequest(args.url, args.method, data = args.data)
    if r.status_code == 200:
        f = open('wiki.html', 'w')
        f.write(r.text)
        f.close()
    else:
        print("ERROR: {s}".format(s = r.status_code))
   


    
