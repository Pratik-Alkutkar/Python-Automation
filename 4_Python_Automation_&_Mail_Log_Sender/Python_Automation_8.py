"""
Date:- 02-06-2024 
Code No:- 8
Code:- Create Log File and display its time of creation and display information of all running processes in it. Schedule this activity after every 1 minutes. Create Folder and create log File in it.
# Not Working
"""
import psutil
import time
import schedule
import os

def CreateLog(FolderName = "Marvellous"):

    if not os.path.exists(FolderName):
        os.mkdir(FolderName)

    FileName= os.path.join(FolderName, "Marvellous%s.log" %(time.ctime()))

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
    schedule.every(1).minutes.do(CreateLog)
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()