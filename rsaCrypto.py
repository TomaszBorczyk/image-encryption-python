from keysModels import RSAPublicKey, RSAPrivateKey

def toHex(msg):
    return ''.join(format(ord(c), 'x') for c in msg)

def asciiToText(msg):
    length, size = len(msg), 3
    symbols = [ msg[i:i+size] for i in range(0, length, size)]
    return ''.join(chr(int(s[0].strip('0') + s[1:])) for s in symbols)

def encrypt(msg, publicKey):
    hex = toHex(msg)
    # for c in msg:
    #     print(str(ord(c)).zfill(3)) 
    m = int(''.join(str(ord(c)).zfill(3) for c in msg))
    # m = int(''.join(str(ord(c, 'x')) for c in msg))
    # m = 3
    print('message to ascii', m)
    return pow(m, publicKey.e, publicKey.n)

def decrypt(cipher, privateKey):
    decryptedVal = str(pow(cipher, privateKey.d, privateKey.n))
    if (len(decryptedVal) % 3 != 0):
        decryptedVal = '0' + decryptedVal
    return decryptedVal