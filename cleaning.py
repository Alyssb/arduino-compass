'''
Alyssa Slayton 01/29/2020
My first real python script; my pride and joy
I would like to eventually separate this into modules
'''
'''
A python script which:
    Cleans sensor data
        separates by direction
        removes outliers
        concats back together
    Plots clean file using gnuplot
        writes a gnuplot script in respective directory
        plots clean x accel data versus clean y accel data
        outputs png
        Calculates and returns average of each direction
    WILL:
        put averages in same file as just_averages.py
I will be using this data to calculate which direction random data is facing.
'''
# allows me to run system commands or delete files
import removeOutliers
from os import system, remove


#################################################### FILE SPEARATION ####################################################

class directionalize:
    # creates a file for each direction and extension

    def __init__(self, infile, numsections, linesPerSection, root, names, columnnames):
        self.infile = infile
        self.numsections = numsections
        self.linesPerSection = linesPerSection
        self.root = root
        self.names = names
        self.columnnames = columnnames

    # creates a file for each direction
    def splitByD(self):
        currentSection = 0
        for i in range(0,self.numsections):
            currentSection = i
            with open(self.root + self.names[currentSection], "w+") as outfile:
                for j in range(currentSection * self.linesPerSection, 
                        (currentSection*self.linesPerSection) + self.linesPerSection):
                    outfile.write(self.infile[j] + "\n")
    
    # creates a file for each acceleration
    def splitByAccel(self, name):
        # takes a direction file
        column = 0
        filename = open(self.root + name).read().split("\n")

        # the columns are known in the data
        # this will not work if the data is in a different format
        for i in self.columnnames:
            with open(self.root + name + i, "w+") as outfile:
                for line in filename:
                    if(len(line) >= column):
                        outfile.write(line.split("\t")[column] + "\n")
            column += 1

######################################################### CALCULATING AVERAGE ##############################################

def avgfn(infile):
    # calculates average of a file
    total = 0.0
    for i in range(len(infile)):
        total+=float(infile[i])
    return total/(len(infile))

############################################### CALCULATING STANDARD DEVIATION #################################################

def stdfn(infile, avg):
    # calculates standard deviation of a file
    # NOT CURRENTLY USED
    total = 0.0
    for i in range(len(infile)):
        total+=((float(infile[i])-avg)**2)
    return total/(len(infile))       

######################################################## MISC. SPACE MANAGEMENT #########################################################

# gets the averages and puts them in a list. Deletes excess files
def getAvgs(root, name, extension, averages):
    infile = open(root + name + extension).read().split("\n")
    del infile [-1]
    del infile [-1]
    averages.append(avgfn(infile))
    remove(root + name + extension)

############################################################## MAIN ##############################################################


def main():
    # definitely could be cleaner
    print("cleaning...")

    root = 'C:\\Users\\alyss\\Documents\\arduino-compass\\20mindata\\' # change as needed
    infile = open(root + "20mindata.txt", "r").read().split("\n")
    
    # VARIABLES
    numsections = 5                                             # number of directions file has
    linesPerSection = 2400                                      # number of lines per direction
    names = ["north", "south", "east", "west", "north2"]        # name of each direction
    extensions = ["xaccel", "yaccel", "zaccel"]                 # names of sections used, must go in a specific order
    
    # produce all files used
    split = directionalize(infile, numsections, linesPerSection, root, names, extensions)
    split.splitByD()
    for i in names:
        split.splitByAccel(i)

    # clear the final files
    # there is probably a better way to do this
    for i in extensions:
        open(root + i+ 'clean', 'w').close()

    # create these for later
    xaverages = []
    yaverages = []
    zaverages = []

    # our heavy lifter
    for i in names: # for each direction,
        for j in extensions:    # for each acceleration,
            infile = open(root + i + j).read().split("\n")  # open the file

            # files made have 2 newlines at the end. Remove them
            del infile[-1]
            del infile[-1]
            outliers = removeOutliers.Outliers(infile) # Create a new instance of Outliers class
            outliers.findOutliers()
            cleaned = outliers.removeOutliersFn()

            # create a file called something like 'xaccelclean', append to the end
            with open(root+j+"clean", "a") as outfile:
                for val in cleaned:
                    outfile.write(val.strip()+"\n")

            # remove(root+i+j) # remove some files to reduce clutter
        remove(root + i)

    print('cleaned.')

    # calculating the averages
    print('calculating averages....')
    for i in names:
        getAvgs(root, i, 'xaccel', xaverages)
        getAvgs(root, i, 'yaccel', yaverages)
        getAvgs(root, i, 'zaccel', zaverages)

    print("averages calculated:\n\tXAVERAGES: ", 
    xaverages, '\n\tYAVERAGES: ', yaverages, '\n\tZAVERAGES: ', zaverages)

    # create and run a gnuplot script in the active folder
    # probably a better way to do this, 
    with open(root+"plot_accel.gp", "w") as outfile:
        outfile.write("set term png\n")                      # output is png
        outfile.write("set output '" + root + "accel_clean.png'\n")       # name output
        # I want to draw arrows on the plot but that's cosmetic and a later problem I think
        outfile.write("plot '" + root + "xaccelclean' w lines title " +  # plot xaccel and y accel
        "'X Accel', (" + str(xaverages[0]) +"), (" + str(xaverages[-1]) + "), '"+ root + "yaccelclean' w lines title 'Y Accel'\n")
    system('gnuplot ' + root + 'plot_accel.gp') # runs the created gnuplot script
    
    print("plot created.")

####################################################################################################################################

if __name__ == '__main__':
    main()