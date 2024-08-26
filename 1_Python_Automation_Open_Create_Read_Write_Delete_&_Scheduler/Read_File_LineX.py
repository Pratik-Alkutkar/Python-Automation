"""
Date:- 12-05-2024
Code No:- 15
Code:- File IO - Read file. This program enables us to read whole file. All File is read. (Simply print whole file line by line.)
"""

import os

def main():
    print("Enter the name of file that you want to Open for reading purpose: ")
    Fname = input()
    
    if os.path.exists(Fname):
        fobj = open(Fname, "r")
        print("File Succcessfully opened in Read mode!")

        for line in fobj:
            print(line)

        fobj.close()
    
    else:
        print("Unable to Open the file as file is not present in Current Directory!")

if __name__ == "__main__":
    main()