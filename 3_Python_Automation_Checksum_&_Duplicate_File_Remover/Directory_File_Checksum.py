"""
Date:- 01-06-2024
Code No:- 1
Code:- Checksum - The MD5 hash function creates a checksum value, but each file won't necessarily have a unique number. 
Application:- The MD5 hash is a cryptographic checksum to verify that a file hasn't been tampered with, the MD5 hash of that file should be verified.
"""

from sys import *
import os
import hashlib

def hashfile(path, blocksize = 1024):    # 1024 bytes = 1 kB
    afile = open(path, 'rb')  #Open file Binary mode
    hasher = hashlib.md5()   #From hashlib module we are using MD5 Algorithm 

    buf = afile.read(blocksize)

    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)

    afile.close()

    return hasher.hexdigest()  #Actual Hash code is generated here

def DisplayChecksum(path):
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    if exists:
        for dirName, subdirs, fileList in os.walk(path):
            print("Current folder is: "+dirName)
            for filen in fileList:
                path = os.path.join(dirName, filen)
                file_hash = hashfile(path)
                print(path)
                print(file_hash)
                print(' ')
    else:
        print("Invalid Path")

def main():
    print("--------SVG by Pratik Alkutkar--------")

    print("Application name: "+argv[0])

    if (len(argv) !=2):
        print("Error : Invalid number of arguments")
        exit()

    if (argv[1] == "--h") or (argv[1] == "--H"):   #-->Help
        print("This Script is used to traverse specific directory and display checksum of files")
        exit()

    if (argv[1] == "--u") or (argv[1] == "--U"):   #-->Usage
        print("Usage: ApplicationName AbsolutePath_Of_Directory Extension")
        exit()

    try:
        arr = DisplayChecksum(argv[1])

    except ValueError:
        print("Error: Invalid Datatype of Input")

    except Exception as E:
        print("Error: Invalid Input",E)

if __name__ == "__main__":
    main()