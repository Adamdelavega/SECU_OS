import hashlib
from datetime import datetime

print("Enter the path of the file to open :")
pathOpenFile = input()

file = open(pathOpenFile,'r')
line = file.readline()

wordlist = open("dico-mini_fr", "r")
password = wordlist.readline()

def getTime():
    global time
    time = datetime.now()
    beginTime = time.strftime("%H:%M:%S")
    return

def getHash(line):
    beginHash = "$"
    endUserName = ":"
    userName = ""
    global lineWithoutUserName
    global stockHash
    stockHash = []
    while line:
        for chekLine in line:
            userName += chekLine
            if chekLine == endUserName:
                lineWithoutUserName = line.strip(userName)
                for checkBeginHash in lineWithoutUserName:
                    if checkBeginHash == beginHash:
                        stockHash.append(lineWithoutUserName[3:35])
                        break
                line = file.readline()
                break
    file.close()
    return

def compareHash(stockHash):
    print("enter the path of the file to create :")
    pathCreateFile = input()
    for checkPass in wordlist:
        for checkHash in stockHash:
            if hashlib.md5(checkPass.strip().encode('utf-8')).hexdigest() == checkHash:
                outputFile = open(pathCreateFile, "a")
                outputFile.write(checkPass)
                now = datetime.now()
                print("time to find the password is :", now - time)
                print(checkPass)
                password = wordlist.readline()          
    file.close()
    return

getTime()
getHash(line)
compareHash(stockHash)
