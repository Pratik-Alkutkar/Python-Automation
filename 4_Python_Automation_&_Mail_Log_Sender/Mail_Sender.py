"""
Date:- 02-06-2024 
Code No:- 11
Code:- Script which accepts time interval from user and create log file in that Marvellous directory which contains information of all running processes. 
After creating the log file send that log file through mail.
"""

import os
import time
import psutil
import urllib.request
import urllib.error
import smtplib
import schedule
from sys import *
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

def is_connected():
    try:
        print("Checking internet connection...")
        urllib.request.urlopen('http://www.google.com', timeout=5)
        print("Internet connection is available.")
        return True
    except urllib.error.URLError as e:
        print(f"No internet connection: {e}")
        return False
    
def Mail_Sender(filename, time):
    try:
        fromaddr = "pratik_alkutkar@moderncoe.edu.in"
        toaddr = "pratikalkutkar.svg@gmail.com"

        msg = MIMEMultipart()

        msg['From'] = fromaddr

        msg['To'] = toaddr

        body = """
        Hello %s,
        Welcome to SVG Group.
        Please find attached document which contains Log of Running Processes.
        Log File is created at: %s

        This is Auto generated mail.

        Thanks and Regards,
        Pratik Pramod Alkutkar
        SVG Group
        """%(toaddr,time)

        Subject = """
        SVG Group Process Log generated at: %s
        """%(time)

        msg['Subject'] = Subject

        msg.attach(MIMEText(body, 'plain'))

        attachment = open(filename, "rb")

        p = MIMEBase('application', 'octet-stream')

        p.set_payload((attachment).read())

        encoders.encode_base64(p)

        p.add_header('Content-Disposition', "attachment; filename = %s" % filename)

        msg.attach(p)

        s = smtplib.SMTP('smtp.gmail.com', '587')

        s.starttls()

        s.login(fromaddr, "----")

        text = msg.as_string()

        s.sendmail(fromaddr, toaddr, text)

        s.quit()

        print("Log File Successfully sent through Mail.")

    except Exception as E:
        print("Unable to send mail.", E)

def ProcessLog(log_dir = 'Marvellous'):
    listprocess = []

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass

    timestamp = time.ctime().replace(" ", "-").replace(":", "_").replace("/", "_")
    log_path = os.path.join(log_dir, f"Marvellous_{timestamp}.txt")

    with open(log_path, 'w') as f:
        separator = "-" * 80
        f = open(log_path, 'w')
        f.write(separator + "\n")
        f.write("SVG Group's Process Logger:" +time.ctime() + "\n")
        f.write(separator + "\n")
        f.write("\n")

        for proc in psutil.process_iter():
            try:
                pinfo = proc.as_dict(attrs=['pid','name','username'])
                vms = proc.memory_info().vms / (1024 * 1024)
                pinfo['vms'] = vms
                listprocess.append(pinfo)

            except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

        for element in listprocess:
            f.write("%s\n"%element)

    print("Log File is Sucessfully generated at location %s" %(log_path))

    connected = is_connected()

    if connected:
        startTime = time.time()
        Mail_Sender(log_path, time.ctime())
        endTime = time.time()

        print('Took %s seconds to send mail' % (endTime - startTime))

    else:
        print("There is no Internet Connection")

def main():
    print("-----SVG Group by Pratik Alkutkar-----")

    print("Application name: "+argv[0])

    if(len(argv) != 2):
        print("Error: Invalid number of arguements")
        exit()

    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used to log record of Running Processes.")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage: ApplicationName AbsolutePath_Of_Directory")
        exit()

    try:
        schedule.every(int(argv[1])).minutes.do(ProcessLog)
        while True:
            schedule.run_pending()
            time.sleep(1)

    except ValueError:
        print("Error: Invalid datatype of input")

    except Exception as E:
        print("Error: Invalid Input", E)

if __name__ == "__main__":
    main()