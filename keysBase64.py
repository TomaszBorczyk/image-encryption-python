from pyasn1.codec.native.encoder import encode
from pyasn1.codec.der.encoder import encode as der_encoder
from pyasn1.codec.der.decoder import decode as der_decoder
from base64 import b64decode, b64encode
from pyasn1.type.univ import Integer, Sequence
from pyasn1.type.namedtype import NamedType, NamedTypes

from keysModels import RSAPublicKey, RSAPrivateKey


class RSAPublicKeyASN1(Sequence):
    componentType = NamedTypes(
        NamedType('modulus', Integer()),
        NamedType('publicExponent', Integer()),
    )

class RSAPrivateKeyASN1(Sequence):
    componentType = NamedTypes(
        NamedType('modulus', Integer()), # n
        NamedType('publicExponent', Integer()), # e
        NamedType('privateExponent', Integer()), # d
        NamedType('prime1', Integer()), # p
        NamedType('prime2', Integer()), # q
        NamedType('exponent1', Integer()), # d % (p-1) 
        NamedType('exponent2', Integer()), # d mod(q-1)
        NamedType('coefficient', Integer()) # 1/q % p
    )


def encodeAndSavePublic(public):
    n, e = public.n, public.e

    asn1Public = RSAPublicKeyASN1()
    asn1Public['modulus'] = n
    asn1Public['publicExponent'] = e
    # print(asn1Public)
    py_public = encode(asn1Public)
    # print(py_public)
    der_serialization = der_encoder(asn1Public)
    # print(der_serialization)
    b64_serialization = '-----BEGIN RSA PUBLIC KEY-----\n'
    b64_serialization += b64encode(der_serialization).decode('utf-8')
    b64_serialization += '\n-----END RSA PUBLIC KEY-----'
    # print(b64_serialization)
    with open('keys/pub.rsa', 'w') as pub:
        pub.write(b64_serialization)

def encodeAndSavePrivate(private):
    asn1Private = RSAPrivateKeyASN1()
    asn1Private['modulus'] = private.n
    asn1Private['publicExponent'] = private.e
    asn1Private['privateExponent'] = private.d
    asn1Private['prime1'] = private.p
    asn1Private['prime2'] = private.q
    asn1Private['exponent1'] = private.exponent1
    asn1Private['exponent2'] = private.exponent2
    asn1Private['coefficient'] = private.coefficient

    # print(asn1Public)
    py_private = encode(asn1Private)
    # print(py_public)
    der_serialization = der_encoder(asn1Private)
    # print(der_serialization)
    b64_serialization = '-----BEGIN RSA PRIVATE KEY-----\n'
    b64_serialization += b64encode(der_serialization).decode('utf-8')
    b64_serialization += '\n-----END RSA PRIVATE KEY-----'
    # print(b64_serialization)
    with open('keys/id.rsa', 'w') as priv:
        priv.write(b64_serialization)


def loadPublicKey():
    with open('keys/pub.rsa', 'r') as pub:
        public64 = ''.join(pub.readlines()[1:-1])
    
    der_serialization = b64decode(public64)
    publicKey, rest_of_input = der_decoder(der_serialization, asn1Spec=RSAPublicKeyASN1())
    py_public = encode(publicKey)
    return RSAPublicKey(*tuple(list(py_public.values())))

def loadPrivateKey():
    with open('keys/id.rsa', 'r') as priv:
        private64 = ''.join(priv.readlines()[1:-1])
    
    der_serialization = b64decode(private64)
    privateKey, rest_of_input = der_decoder(der_serialization, asn1Spec=RSAPrivateKeyASN1())
    py_private = encode(privateKey)
    return RSAPrivateKey(*tuple(list(py_private.values())))
