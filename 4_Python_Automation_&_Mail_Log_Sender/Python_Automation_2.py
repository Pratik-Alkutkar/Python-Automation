"""
Date:- 02-06-2024 
Code No:- 2
Code:- To display information of all Running Processes.
"""
import psutil

def DisplayProcess():
    print("List of Running processes are: ")

    print("________________________________________________________")

    for proc in psutil.process_iter(['pid', 'name', 'username']):
        print(proc.info)

    print("________________________________________________________")

def main():
    DisplayProcess()

if __name__ == "__main__":
    main()