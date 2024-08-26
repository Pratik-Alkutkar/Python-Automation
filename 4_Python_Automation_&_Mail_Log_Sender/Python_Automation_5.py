"""
Date:- 02-06-2024 
Code No:- 5
Code:- Create Log File and display its time of creation and display information of all running processes in it.
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

    Arr = GetProcessInfo()

    for data in Arr:
        fd.write("%s \n" %data)  # '%s' is for string and '\n' is to print on next line.

    fd.write(seperator + "\n")
    
    fd.close()

def GetProcessInfo():
    listprocess = []
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        listprocess.append(proc.info)

    return listprocess

def main():
    CreateLog()

if __name__ == "__main__":
    main()