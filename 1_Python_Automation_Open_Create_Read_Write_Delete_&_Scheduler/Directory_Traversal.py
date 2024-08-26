"""
Date:- 12-05-2024
Code No:- 17
Code:- File IO - Check files present in particular folder.
"""
import os

def main():
    print("Enter the name of Directory that you want to scan: ")
    Dname = input()

    for foldername, subfoldername, filenames in os.walk(Dname):
        for fname in filenames:
            print(fname)

if __name__ == "__main__":
    main()