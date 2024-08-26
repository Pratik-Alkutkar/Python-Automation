"""
Date:- 12-05-2024
Code No:- 9
Code:- File IO - Opens file for writing pupose from the current directory. Opens the file in which we want to write and input Data in that file. But here data gets overwritten. 
"""

import os

def main():
    print("Enter the name of file that you want to Open for writing purpose: ")
    Fname = input()
    
    if os.path.exists(Fname):
        fobj = open(Fname, "w")
        print("File Succcessfully opened in Write mode!")

        print("Enter the Data that you want to Write in the file: ")
        Data = input()

        fobj.write(Data)
    
    else:
        print("Unable to Open the file as file is not present in Current Directory!")

if __name__ == "__main__":
    main()