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

# creates a file that is a list of filenames and then returns it as a listb
def getFiles(root, folder):
    system("dir /b /a-d " + root + folder + " > " + root + folder + "filenames.txt")
    return(open(root + folder + "filenames.txt").read().split())

# splits by accel, makes a bajillion files
def splitByAccel(root, filename, columnames):
    # this is just regurgitated code from cleaning.py
    # will eventually modularize this code
    column = 0
    for i in columnames:
        with open(root + filename + i, "w+") as outfile:
            for line in filename:
                if(len(line) >= column):
                    outfile.write(line.split("\t")[column] + "\n")
        column += 1
    

def main():
    root = 'C:\\Users\\alyss\\Documents\\arduino-compass\\'
    folders = ["data_north\\", "data_south\\", "data_east\\", "data_west\\"]
    columnames = ["xaccel", "yaccel", "zaccel"]
    for folder in folders:
        filenames = getFiles(root, folder)
        print(filenames)
        for name in filenames:
            if name == 'filenames.txt':
                pass
            else:
                splitByAccel(root, name, columnames)


if __name__ == '__main__':
    main()