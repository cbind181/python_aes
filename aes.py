from Crypto import Random
from Crypto.Cipher import AES
import os
import os.path
from os import listdir
from os.path import isfile, join
import time

encryptTimes = []
decryptTimes = []

class Encryptor:
    
    def __init__(self, key):
        self.key = key

    def pad(self, s):
        return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

    def encrypt(self, message, key, key_size=256):
        start = time.time()
        message = self.pad(message)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        ret = iv + cipher.encrypt(message)
        end = time.time()
        print("encrypt time: ", end - start)
        encryptTimes.append(end - start)
        return ret

    def encrypt_file(self, file_name):
        with open(file_name, 'rb') as fo:
            plaintext = fo.read()
        enc = self.encrypt(plaintext, self.key)
        with open(file_name + ".enc", 'wb') as fo:
            fo.write(enc)
        os.remove(file_name)

    def decrypt(self, ciphertext, key):
        start = time.time()
        iv = ciphertext[:AES.block_size]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plaintext = cipher.decrypt(ciphertext[AES.block_size:])
        ret = plaintext.rstrip(b"\0")
        end = time.time()
        print("decrypt time: ", end - start)
        decryptTimes.append(end - start)
        return ret

    def decrypt_file(self, file_name):
        with open(file_name, 'rb') as fo:
            ciphertext = fo.read()
        dec = self.decrypt(ciphertext, self.key)
        with open(file_name[:-4], 'wb') as fo:
            fo.write(dec)
        os.remove(file_name)


key = b'[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e'
enc = Encryptor(key)
clear = lambda: os.system('cls')



for i in range(0,20):

    enc.encrypt_file("small.txt")
    

    enc.decrypt_file("small.txt.enc")
    

print("average encrypt time: ", sum(encryptTimes)/len(encryptTimes))
print("average decrypt time: ", sum(decryptTimes)/len(decryptTimes))

print("best encrypt time: ", min(encryptTimes))
print("best decrypt time: ", min(decryptTimes))

