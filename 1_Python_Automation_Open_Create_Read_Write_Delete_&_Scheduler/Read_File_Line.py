"""
Date:- 12-05-2024
Code No:- 14
Code:- File IO - Read file. This program enables us to specify how much Lines we want to read. So here 4 lines are printed.
"""

import os

def main():
    print("Enter the name of file that you want to Open for reading purpose: ")
    Fname = input()
    
    if os.path.exists(Fname):
        fobj = open(Fname, "r")
        print("File Succcessfully opened in Read mode!")

        str1 = fobj.readline()
        str2 = fobj.readline()
        str3 = fobj.readline()
        str4 = fobj.readline()

        print(str1)
        print(str2)
        print(str3)
        print(str4)

        fobj.close()
    
    else:
        print("Unable to Open the file as file is not present in Current Directory!")

if __name__ == "__main__":
    main()