"""
Date:- 26-05-2024
Code No:- 2
Code:- --h and --u is for third party reader to understand the Script.
"""

import sys

def Addition(A,B):
    return A + B

def main():
    print("_____________________________________________________")
    print("-----------Automation to perform Addition-----------")
    print("_____________________________________________________")

    if (sys.argv[1]== "--h" or sys.argv[1]=="--H"):
        print("This Script is used to perform Addition of 2 integral values")
        exit()

    if (sys.argv[1]== "--u" or sys.argv[1]=="--U"):
        print("Usage of the Script: ")
        print("Name_Of_File First_Argument Second_Argument")
        print("Note:- Both the arguments must be in integral format.")
        exit()

    ret = Addition(int(sys.argv[1]), int(sys.argv[2]))
    print("Addition is: ", ret)

if __name__ == "__main__":
    main()