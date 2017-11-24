from keysModels import RSAPublicKey, RSAPrivateKey
import math
import sys
# BITS = 1233 # for 4096 RSA
BITS = 307 # for 1024 RSA

def toHex(msg):
    return ''.join(format(ord(c), 'x') for c in msg)

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

def splitToBlocks(asciiMsg):
    length, size = len(asciiMsg), BITS
    blocks = [ asciiMsg[i:i+size].ljust(size, '0') for i in range(0, length, size)]
    msg = blocks[0].encode()
    return blocks

def encryptBlock(block, publicKey):
    val = pow(block, publicKey.e, publicKey.n)
    return val

def encryptBlockMessage(blocks, publicKey):
    return ''.join(str(encryptBlock(int(block), publicKey)) + '\n' for block in blocks).rstrip('\n')

def encryptLargeFile(msg, publicKey):
    asciiMsg = msgToAsciiValue(msg)
    blocks = splitToBlocks(asciiMsg)
    encryptedMsg = encryptBlockMessage(blocks, publicKey)
    print(encryptedMsg)
    return encryptedMsg




def decryptBlock(block, privateKey):
    decryptedVal = str(pow(block, privateKey.d, privateKey.n))
    return decryptedVal.zfill(BITS)

def decryptBlockMessage(blocks, privateKey):
    decrypted, blocksAmount = '', len(blocks)
    print('0%')
    for i, block in enumerate(blocks):
        decrypted = decrypted + str(decryptBlock(int(block), privateKey))
        # print(str(math.floor((i/blocksAmount)*100))+'%')
        progres = math.floor((i/blocksAmount)*100
        sys.stdout.write("Download progress: %d%%   \r", progress)
        sys.stdout.flush()
    return decrypted
    print('100%')
  
    # return ''.join(str(decryptBlock(int(block), privateKey)) for block in blocks)

def decryptLargeFile(msg, privateKey):
    length, size = len(msg), BITS
    blocks = msg.split('\n')
    # print('encrypted blocks', blocks)
    decryptedMsg = decryptBlockMessage(blocks, privateKey)
    # print('decrypted msg', decryptedMsg)
    text =  asciiToText(decryptedMsg)
    # print(text)
    return text
    



