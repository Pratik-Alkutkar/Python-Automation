from sys import *
import os
import hashlib
import time

def DeleteFiles(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))

    icnt = 0

    if len(results) > 0:
        for result in results:
            for subresult in result:
                icnt += 1
                if icnt >= 2:
                    os.remove(subresult)
                icnt = 0
    else:
        print("No Duplicate Files Found.")

def hashfile(path, blocksize = 1024):    # 1024 bytes = 1 kB
    afile = open(path, 'rb')  #Open file Binary mode
    hasher = hashlib.md5()   #From hashlib module we are using MD5 Algorithm 
    buf = afile.read(blocksize)

    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()

    return hasher.hexdigest()  #Actual Hash code is generated here

def FindDuplicate(path):
    flag = os.path.isabs(path)

    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    dups = {}
    if exists:
        for dirName, subdirs, fileList in os.walk(path):
            print("Current Folder is: "+dirName)
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

def PrintResults(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))

    if len(results) > 0:
        print("Duplicates Found: ")
        print("The following Files are duplicate.")
        for result in results:
            for subresult in result:
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
        startTime = time.time()
        arr = FindDuplicate(argv[1])
        PrintResults(arr)
        DeleteFiles(arr)
        endTime = time.time()

        print('Took %s seconds to evaluate.' % (endTime - startTime))

    except ValueError:
        print("Error: Invalid Datatype of Input")

    except Exception as E:
        print("Error: Invalid Input",E)

if __name__ == "__main__":
    main()