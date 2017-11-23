import json
from keysModels import RSAPublicKey, RSAPrivateKey

def getPrivate(filename=None):
    if filename is None:
        filename = 'keys/priv.rsa.json'
    private = json.load(open(filename))
    return RSAPrivateKey(private["n"], private["d"])

def getPublic(filename=None):
    if filename is None:
        filename = 'keys/pub.rsa.json'
    public = json.load(open(filename))
    return RSAPublicKey(public['n'], public['e'])

