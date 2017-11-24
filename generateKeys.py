import json
import sys
from fractions import gcd
from Crypto.Util import number
from keysModels import RSAPublicKey, RSAPrivateKey
from keysBase64 import encodeAndSavePrivate, encodeAndSavePublic

sys.setrecursionlimit(1000000)  # long type,32bit OS 4B,64bit OS 8B(1bit for sign)
BITS = 2048
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
    # while(gcd(prime-1, E) != 1):
    while(egcd(prime-1, E)[0] != 1):
        prime = number.getPrime(bits)
    return prime

def generateKeys():
    print('Generating primes...')
    p = generatePrime(BITS+1)
    q = generatePrime(BITS-1)
    print('Calculating modulus...')
    n = p * q
    print('Calculating phi...')
    phi = lcm(p-1, q-1)
    print('Calculating private exponent...')
    d = mulinv(E, phi)
    print('Calculating exponent1...')
    exponent1 = d % (p-1)
    print('Calculating exponent2...')
    exponent2 = d % (q-1)
    print('Calculating coefficient...')
    # coefficient = (1/q) % p
    # coefficient = pow(1/q, 1, p)
    coefficient = mulinv(q, p)
    return (RSAPrivateKey(n, E, d, p, q, exponent1, exponent2, coefficient), RSAPublicKey(n, E))
