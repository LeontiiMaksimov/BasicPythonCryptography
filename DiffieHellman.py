import sys
import hashlib
import secrets
import pyDH

if sys.version_info < (3, 6):
    import sha3

random1 = 16384 + secrets.randbelow(10000)


# encryption/decryption buffer size is random


# To send the information we will be using the pure python implementation of the Diffie-Hellman algorithm.
d1 = pyDH.DiffieHellman()
d1_pubkey = d1.gen_public_key()
print("Your public key is:")
print(d1_pubkey)
print("")
print("Input the public key of the other user")
d2_pubkey = int(input())
d1_sharedkey = d1.gen_shared_key(d2_pubkey)

for i in range(random1):
    d1_sharedkey = hashlib.sha3_512(d1_sharedkey.encode('utf-8')).hexdigest()

t = ""
for i in str(d1_sharedkey):
    try:
        int(i)
        t = t + str(i)
    except: continue
    if len(t) == 2:
        break

print("Your buffer size (in KB) for this session will be: " + t)
print("Your shared key for this session will be: " + d1_sharedkey)
print("")
print("Compare using these two keys, you send one, the other user sneds the other, they are the same for both of you")

for i in range(random1-1):
    d1_sharedkey = hashlib.sha3_512(d1_sharedkey.encode('utf-8')).hexdigest()
print(d1_sharedkey)
print('')

for i in range(random1+3):
    d1_sharedkey = hashlib.sha3_512(d1_sharedkey.encode('utf-8')).hexdigest()

print(d1_sharedkey)
