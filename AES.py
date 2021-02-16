import pyAesCrypt
print("Input your password")
password = input()

print("")
print("Input your buffer (KB) size (encrypting or decrypting)")
bufferSize = int(input())
# encrypt
print("")
print("Input your document name you are decrypting / encrypting")
name = input()
print("type in de if you are decrypting and en if you are encrypting")
status = input()

if status == "en":
    pyAesCrypt.encryptFile(name, "output.aes", password, bufferSize)
elif status == "de":
    print("Input file extension")
    ext = input()
    pyAesCrypt.decryptFile(name, "output"+ext, password, bufferSize)
