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

    remove outliers
    produce clean files
    delete dirty ones

    calculate averages
    create a file with them
    remove all extra files
'''
import removeOutliers
from os import system, remove

# creates a file that is a list of filenames and then returns it as a listb
def getFiles(root, folder):
    system("dir /b /a-d " + root + folder + " > " + root + folder + "filenames.txt")
    return(open(root + folder + "filenames.txt").read().split())

# splits by accel, makes a bajillion files
def splitByAccel(root, folder, filename, columnames):
    # this is just regurgitated code from cleaning.py
    column = 0
    print(filename)
    for i in columnames:
        with open(root + folder + filename + i, "w+") as outfile:
            for line in open(root + folder + filename, "r").read().split("\n"):
                if(len(line) >= column):
                    outfile.write(line.split("\t")[column] + "\n")
        column += 1
    
# why do I put so much garbage in my main
def main():
    root = 'C:\\Users\\alyss\\Documents\\arduino-compass\\'
    folders = ["data_north\\", "data_south\\", "data_east\\", "data_west\\"]
    extensions = ["xaccel", "yaccel", "zaccel"]
    
    # code-spaghet
    for folder in folders:
        filenames = getFiles(root, folder)

        for name in filenames:
            if name == 'filenames.txt':
                filenames.remove(name)
        
        for name in filenames:
            # print(name)
            # print(filenames)
            splitByAccel(root, folder, name, extensions)
            
            # more reused code
            for j in extensions:
                infile = open(root + folder + name + j).read().split("\n")

                del infile[-1]
                outliers = removeOutliers.Outliers(infile)
                outliers.findOutliers()
                cleaned = outliers.removeOutliersFn()

                # create clean file
                with open(root + name + j + "clean", "a") as outfile:
                    for val in cleaned:
                        outfile.write(val.strip()+"\n")
        remove (root + folder + name)    # reduces clutter
        # throwback to when this wasn't garbage
    print("cleaning....")

if __name__ == '__main__':
    main()