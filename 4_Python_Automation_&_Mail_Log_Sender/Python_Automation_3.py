"""
Date:- 02-06-2024 
Code No:- 3
Code:- Create a Log File.
"""
import psutil

def CreateLog(FileName = "Marvellous.log"):
    fd = open(FileName, "w")
    seperator = "-"*70

    fd.write(seperator + "\n")
    fd.write("Marvellous Process Log"+ "\n")
    fd.write(seperator + "\n")

    fd.write("CONTENTS OF LOG FILE"+ "\n")
    fd.write(seperator + "\n")

    fd.close()

def main():
    CreateLog()

if __name__ == "__main__":
    main()