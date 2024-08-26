"""
Date:- 12-05-2024
Code No:- 13
Code:- File IO - Read file. This program enables us to specify how much we want to read.
"""

import os

def main():
    print("Enter the name of file that you want to Open for reading purpose: ")
    Fname = input()
    
    if os.path.exists(Fname):
        fobj = open(Fname, "r")
        print("File Succcessfully opened in Read mode!")

        Data = fobj.read(10) # <-- Bytes mentioned here

        print(Data)

        fobj.close()
    
    else:
        print("Unable to Open the file as file is not present in Current Directory!")

if __name__ == "__main__":
    main()