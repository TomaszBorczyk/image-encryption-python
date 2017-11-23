import json
from fractions import gcd
from Crypto.Util import number
from keysModels import RSAPublicKey, RSAPrivateKey
from keysBase64 import encodeAndSavePrivate, encodeAndSavePublic
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
    exponent1 = d % (p-1)
    exponent2 = d % (q-1)
    coefficient = (1/q) % p
    return (RSAPrivateKey(n, E, d, p, q, exponent1, exponent2, coefficient), RSAPublicKey(n, E))
