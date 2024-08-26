"""
Date:- 12-05-2024
Code No:- 7
Code:- File IO - Creates a new file of desired name in the current directory and also handles file's same name error.
"""

import os

def main():
    print("Enter the name of file that you want to create: ")
    Fname = input()
    
    if os.path.exists(Fname):
        print("Unable to create file as file is already existing!")
    else:
        open(Fname, "x")
        print("File successfully created!")

if __name__ == "__main__":
    main()

# Absolute path: D:\Marvellous Infosystems\Python\Automation\Session_12/Marvellous.txt
# Relative path: Automations/Session_12/Marvellous.txt