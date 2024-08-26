"""
Date:- 12-05-2024
Code No:- 16
Code:- File IO - Delete file. 
"""

import os

def main():
    print("Enter the name of file that you want to Delete: ")
    Fname = input()
    
    if os.path.exists(Fname):
        os.remove(Fname)
        print("File Deleted Successfully!")
    
    else:
        print("Unable to Delete the file as file is not present in Current Directory!")

if __name__ == "__main__":
    main()