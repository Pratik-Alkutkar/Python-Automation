"""
Date:- 12-05-2024
Code No:- 6
Code:- File IO - Creates a new file of desired name in the current directory.
"""

import os

def main():
    print("Enter the name of file that you want to create: ")
    Fname = input()

    open(Fname, "x")

if __name__ == "__main__":
    main()