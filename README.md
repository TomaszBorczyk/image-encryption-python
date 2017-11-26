PNG encryption implementing RSA and Caesar Cipher in Python
===================
Used Python version is 3.6. Only PNG format was tested.

This is a university project for a digital signature and cryptography class. The goal was to create an RSA key generation and image encryption/decryption from scratch, and also to implement Caesar Cipher to see that images can still be recognised after encryption.

----------

### RSA

Due to limited data size in RSA encryption, an image file is processed in chunks of length less than the length of the key. This is method has probably no real life use. 

For the keys generation, Extended Euclidean Algorithm and finding modular inverses implementations are from [Wikipedia page](https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm#Python).
Key bit strength is hardcoded in generateKeys.py BITS global. No more than 1024 was tested. Since decryption can take significant amount of time, especially with long key, small greyscale images are recommended with pixels expressed in single value, not RGBA (see lena-greyscale-small.png for reference).
### Caesar cipher

This algorithm uses array of values from 0 to 255 in a random order as a cipher dictionary. 
### Usage

Run the program by calling
```
python main.py
```
Use following commands to navigate the program:


| Command| Usage|
| ---------------------------- | ------------------
| r           | Choose RSA encoding |
| c           | Choose Caesar cipher |
| g | Generate keys/Caesar cipher dictionary |
| e | Encrypt file |
| d | Decrypt file |

Beware, as generating new keys or cipher dictionary overrides old ones without a warning.