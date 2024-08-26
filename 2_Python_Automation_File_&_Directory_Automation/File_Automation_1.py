"""
Date:- 26-05-2024
Code No:- 1
Code:- 
"""

import sys

def Addition(A,B):
    return A + B

def main():
    ret = Addition(int(sys.argv[1]), int(sys.argv[2]))
    print("Addition is: ", ret)

if __name__ == "__main__":
    main()