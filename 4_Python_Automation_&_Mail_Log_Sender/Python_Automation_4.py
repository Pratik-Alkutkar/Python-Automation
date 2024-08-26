"""
Date:- 02-06-2024 
Code No:- 4
Code:- Create Log File and display its time of creation.
"""
import psutil
import time

def CreateLog(FileName = "Marvellous.log"):
    fd = open(FileName, "w")
    seperator = "-"*70

    fd.write(seperator + "\n")
    fd.write("Marvellous Process Log"+ "\n")
    fd.write("Log File Created at: "+time.ctime() + "\n")
    fd.write(seperator + "\n")

    fd.write("CONTENTS OF LOG FILE"+ "\n")
    fd.write(seperator + "\n")
    
    fd.close()

def main():
    CreateLog()

if __name__ == "__main__":
    main()