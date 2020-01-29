'''
Alyssa Slayton 01/28/2020
'''
'''
A python script which:
    WILL:
        get a list of all files in a folder
        calculate averages for xaccel, yaccel, zaccel
        return those averages in a list
        put the averages in a file
I will be using this data to calculate which direction random data is facing
'''
'''
Design notes for myself:
    Get a list of all filenames in a folder
    separate as filename_$accel_clean
    gonna be a lot of files but that's chill ig
'''
from os import system, remove

def getFiles(root, name):
    system("dir /b /a-d " + root + name + " > " + root + name + "filenames.txt")
    return(open(root + name + "filenames.txt").read().split())

def splitByAccel():
    print("not yet implemented")

def main():
    root = 'C:\\Users\\alyss\\Documents\\arduino-compass\\'
    names = ["data_north\\", "data_south\\", "data_east\\", "data_west\\"]
    for name in names:
        filenames = getFiles(root, name)
        print(filenames)
    print("hello world.")

if __name__ == '__main__':
    main()