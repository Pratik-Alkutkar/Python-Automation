"""
Date:- 26-05-2024
Code No:- 10
Code:- Return path and size of all the files present in given directory's Folder that is given in Command Line arguments.
"""
import os
import sys
import time

def DirectoryWatcher(DirName):

    flag = os.path.isabs(DirName) #isabs is used to check whether the path is an Absolute path.

    if(flag == False):
        print("Path is not an Absolute path")
        DirName = os.path.abspath(DirName)  #abspath is used to convert to Absolute path.
        print("Converted Absolute path is: ",DirName)

    exist = os.path.isdir(DirName)

    if (exist == True):
        for foldername, subfoldername, filename in os.walk(DirName):
            for name in filename:
                print("File Path is: ", os.path.join(foldername,name))
                print("File Size is: ", os.path.getsize(os.path.join(foldername, name)), "bytes")

    else:
        print("There is no such Directory")

def main():
    print("_____________________________________________________")
    print("-----------------Directory Watcher-----------------")
    print("_____________________________________________________")

    if (len(sys.argv) == 2):
        if (sys.argv[1]== "--h" or sys.argv[1]=="--H"):
            print("This Script is used to perform Directory Traversal")
            exit()

        if (sys.argv[1]== "--u" or sys.argv[1]=="--U"):
            print("Usage of the Script: ")
            print("Name_Of_File Name_Of_Directory")
            exit()

        try:
            starttime = time.time()

            DirectoryWatcher(sys.argv[1])
            
            endtime = time.time()

            print("Time required to execute the Script is: ", endtime-starttime)

        except Exception as obj2:        ##
            print("Unable to perform the task due to", obj2)

    else:
        print("Invalid Option")
        print("Use --h option to get the help and use --u option to get the usage of Application")
        exit()

    print("_____________________________________________________")
    print("-----------Thank You for using our Script------------")
    print("______________Pratik Pramod Alkutkar_________________")

if __name__ == "__main__":
    main()