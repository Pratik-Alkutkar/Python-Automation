"""
Date:- 01-06-2024
Code No:- 2
Code:- 
"""

from sys import *
import os
import hashlib

def hashfile(path, blocksize = 1024):    # 1024 bytes = 1 kB
    fd = open(path, 'rb')  #Open file Binary mode
    hasher = hashlib.md5()   #From hashlib module we are using MD5 Algorithm 

    buf = fd.read(blocksize)

    while len(buf) > 0:
        hasher.update(buf)
        buf = fd.read(blocksize)

    fd.close()

    return hasher.hexdigest()  #Actual Hash code is generated here

def FindDuplicate(path):
    flag = os.path.isabs(path)

    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    dups = {}
    if exists:
        for dirName, subdirs, fileList in os.walk(path):
            for filen in fileList:
                path = os.path.join(dirName, filen)
                file_hash = hashfile(path)
                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash] = [path]

        return dups
    else:
        print("Invalid Path")

def PrintDuplicate(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))

    if len(results) > 0:
        print("Duplicates Found: ")

        print("The following Files are identical.")

        icnt = 0
        for result in results:
            for subresult in result:
                icnt += 1
                if icnt >= 2:
                    print('\t\t%s'% subresult)

    else:
        print("No Duplicate Files Found")

def main():
    print("--------SVG by Pratik Alkutkar--------")

    print("Application name: "+argv[0])

    if (len(argv) !=2):
        print("Error : Invalid number of arguments")
        exit()

    if (argv[1] == "--h") or (argv[1] == "--H"):   #-->Help
        print("This Script is used to traverse specific directory and display sizes of files")
        exit()

    if (argv[1] == "--u") or (argv[1] == "--U"):   #-->Usage
        print("Usage: ApplicationName AbsolutePath_Of_Directory Extension")
        exit()

    try:
        arr = {}
        arr = FindDuplicate(argv[1])
        PrintDuplicate(arr)

    except ValueError:
        print("Error: Invalid Datatype of Input")

if __name__ == "__main__":
    main()