import json

def getPrivate(filename=None):
    if filename is None:
        filename = 'keys/priv.rsa.json'
    private = json.load(open(filename))
    return (private["n"], private["d"])

def getPublic(filename=None):
    if filename is None:
        filename = 'keys/pub.rsa.json'
    public = json.load(open(filename))
    return (public['n'], public['e'])
