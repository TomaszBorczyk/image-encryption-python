def encrypt(msg, publicKey):
    n, e = publicKey
    m = int(''.join(str(ord(c)) for c in msg))
    # m = 3
    print('message to ascii', m)
    return pow(m, e, n)

def decrypt(cipher, privateKey):
    n, d = privateKey
    print('d', d)
    return pow(cipher, d, n)