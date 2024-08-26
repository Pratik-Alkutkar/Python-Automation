"""
Date:- 12-05-2024
Code No:- 8
Code:- File IO - Opens file from the current directory. Handles File not found error.
"""

#Here file gets logically opened for the PVM and its not like how file opens when we double click.

import os

def main():
    print("Enter the name of file that you want to Open: ")
    Fname = input()
    
    if os.path.exists(Fname):
        fobj = open(Fname, "r")
        print("File Succcessfully opened!")
        print(fobj)
    
    else:
        print("Unable to Open the file as file is not present in Current Directory!")

if __name__ == "__main__":
    main()