"""
Date:- 12-05-2024
Code No:- 11
Code:- File IO - Closes the file.
"""

import os

def main():
    print("Enter the name of file that you want to Open for writing purpose: ")
    Fname = input()
    
    if os.path.exists(Fname):
        fobj = open(Fname, "a")
        print("File Succcessfully opened in Write mode!")

        print("Enter the Data that you want to Write in the file")
        Data = input()

        fobj.write(Data)

        fobj.close()
    
    else:
        print("Unable to Open the file as file is not present in Current Directory!")

if __name__ == "__main__":
    main()