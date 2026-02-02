import os
from datetime import date, time , timedelta, datetime
import time
import files
def get_os_name():
    print("Operating System Name:", os.name)

def if_item_exists(filename):
    print(f"Item Exists: {os.path.exists(filename)}")
    print(f"This is a file : {os.path.isfile(filename)}")
    print(f"This is a directory : {os.path.isdir(filename)}")

def get_real_path(filename):
    print(f"Path of file : {"/".join(os.path.realpath(filename).split("\\")[:-1])}  File :  {os.path.realpath(filename).split("\\")[-1]}")

def get_mofified_time(filename):
    t = time.ctime(os.path.getmtime(filename))
    print(t)
    print(datetime.fromtimestamp(os.path.getmtime(filename)))
    td = datetime.now() - datetime.fromtimestamp(os.path.getmtime(filename))
    print(f"Modified {td.total_seconds()} seconds ago")

def main():
    # Setup Here 
    files.read_write_file()
    get_os_name()
    if_item_exists("sample.txt")
    get_real_path("sample.txt")
    get_mofified_time("sample.txt")

if __name__ == "__main__":
    main()