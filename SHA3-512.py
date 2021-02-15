import sys
import hashlib
if sys.version_info < (3, 6):
    import sha3
    
print("Input")
text = input()
print("Input how many times the input should be hashed")
n = int(input())

for i in range(n):
    text = hashlib.sha3_512(text.encode('utf-8')).hexdigest()
