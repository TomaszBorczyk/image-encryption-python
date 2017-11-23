import json
from fractions import gcd
from Crypto.Util import number

BITS = 1024
# E = 65537
E = 3

def lcm(_a, _b):
    return (_a *_b) // gcd(_a, _b)

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

def mulinv(b, n):
    g, x, _ = egcd(b, n)
    if g == 1:
        return x % n

def generatePrime(bits):
    prime = number.getPrime(bits)
    while(gcd(prime-1, E) != 1):
        prime = number.getPrime(bits)
    return prime

def generateKeys():
    p = generatePrime(BITS)
    q = generatePrime(BITS-1)
    n = p * q
    phi = lcm(p-1, q-1)
    d = mulinv(E, phi)
    return ((n, d), (n, E))

def saveKeysToFiles(private, public):
    n, d, = private
    _, e = public
    privateJson = {'n': n, 'd': d}
    publicJson = {'n': n, 'e': e}
    
    with open('keys/pub.rsa.json', 'w') as outfile:
        json.dump(publicJson, outfile)

    with open('keys/priv.rsa.json', 'w') as outfile:
        json.dump(privateJson, outfile)


def main():
    private, public = generateKeys()
    # print(private, public)
    saveKeysToFiles(private, public)
