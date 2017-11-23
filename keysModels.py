class RSAPublicKey:
        def __init__(self, n, e):
            self.n = n
            self.e = e

class RSAPrivateKey:
        def __init__(self, n, e, d, p, q, exponent1, exponent2, coefficient):
            self.n = n
            self.e = e
            self.d = d
            self.p = p
            self.q = q
            self.exponent1 = exponent1
            self.exponent2 = exponent2
            self.coefficient = coefficient
