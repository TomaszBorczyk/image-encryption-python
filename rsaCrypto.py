from keysModels import RSAPublicKey, RSAPrivateKey
import math
import sys

def getMaxBitsDataSize(key):
    return len(str(key.n)) - 3

def asciiToText(msg):
    length, size = len(msg), 3
    symbols = [ msg[i:i+size] for i in range(0, length, size)]
    return ''.join(chr(int(s[0].strip('0') + s[1:])) for s in symbols).rstrip('\0')

def encrypt(msg, publicKey):
    # hex = toHex(msg)
    # for c in msg:
    #     print(str(ord(c)).zfill(3)) 
    m = int(''.join(str(ord(c)).zfill(3) for c in msg))
    # m = int(''.join(str(ord(c, 'x')) for c in msg))
    # m = 3
    print('message to ascii', m)
    value = pow(m, publicKey.e, publicKey.n)
    print('ENCRYPTED VALUE', value)
    print('BIT LENGTH OF ENCRYPTED VALUE', int.bit_length(value))
    return value

def decrypt(cipher, privateKey):
    decryptedVal = str(pow(cipher, privateKey.d, privateKey.n))
    if (len(decryptedVal) % 3 != 0):
        decryptedVal = '0' + decryptedVal
    print('DECRYPTED VALUE', decryptedVal)
    return decryptedVal




def msgToAsciiValue(msg):
    return ''.join(str(ord(c)).zfill(3) for c in msg)

def splitToBlocks(asciiMsg, size):
    length = len(asciiMsg)
    blocks = [ asciiMsg[i:i+size].ljust(size, '0') for i in range(0, length, size)]
    return blocks

def encryptBlock(block, publicKey):
    val = pow(block, publicKey.e, publicKey.n)
    return val

def encryptBlockMessage(blocks, publicKey):
    return ''.join(str(encryptBlock(int(block), publicKey)) + '\n' for block in blocks).rstrip('\n')

def encryptLargeFile(msg, publicKey):
    bits = getMaxBitsDataSize(publicKey)
    asciiMsg = msgToAsciiValue(msg)
    blocks = splitToBlocks(asciiMsg, bits)
    encryptedMsg = encryptBlockMessage(blocks, publicKey)
    return encryptedMsg




def decryptBlock(block, privateKey):
    bits = getMaxBitsDataSize(privateKey)
    decryptedVal = str(pow(block, privateKey.d, privateKey.n))
    return decryptedVal.zfill(bits)

def decryptBlockMessage(blocks, privateKey):
    decrypted, blocksAmount = '', len(blocks)
    print('\r0%', end='')
    for i, block in enumerate(blocks):
        decrypted = decrypted + str(decryptBlock(int(block), privateKey))
        progress = str(math.floor((i/blocksAmount)*100))
        print('\r' + progress + '%', end='')
    print('\r100%', end='')
    return decrypted
    # return ''.join(str(decryptBlock(int(block), privateKey)) for block in blocks)

def decryptLargeFile(msg, privateKey):
    length = len(msg)
    blocks = msg.split('\n')
    decryptedMsg = decryptBlockMessage(blocks, privateKey)
    text =  asciiToText(decryptedMsg)
    return text
    



