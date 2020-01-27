'''
Alyssa Slayton 01/22/2020
My first real python script
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
    WILL:
        Calculate average of each direction
        tell me those averages
I will be using this data to calculate which direction random data is facing.
'''
# allows me to run system commands or delete files
from os import system, remove

#################################################### FILE SPEARATION ####################################################

class directionalize:
    # creates a file for each direction
    # for x acceleration, y acceleration, and z acceleration
    def __init__(self, infile, numsections, linesPerSection, root, names, columnnames):
        self.infile = infile
        self.numsections = numsections
        self.linesPerSection = linesPerSection
        self.root = root
        self.names = names
        self.columnnames = columnnames

    def splitByD(self):
        # creates separate files for each direction in original
        currentSection = 0
        for i in range(0,self.numsections):
            currentSection = i
            with open(self.root + self.names[currentSection], "w+") as outfile:
                for j in range(currentSection * self.linesPerSection, (currentSection*self.linesPerSection) + self.linesPerSection):
                    outfile.write(self.infile[j] + "\n")
                
    def splitByAccel(self, name):
        # creates separate files for each acceleration
        # takes a direction file

        column = 0
        filename = open(self.root + name).read().split("\n")

        for i in self.columnnames:
            with open(self.root + name + i, "w+") as outfile:
                for line in filename:
                    if(len(line) >= column):
                        outfile.write(line.split("\t")[column] + "\n")
            column += 1

######################################## REMOVING OUTLIERS ###############################################################

class Outliers:
    def __init__(self, infile):
        self.infile = infile

        # sorts infile in ascending order
        self.sorted = infile.copy()
        self.sorted.sort()
        # corrects if the file had both positive and negative numbers
        if(self.sorted[len(self.sorted)-1][0] == '-'):
            self.sorted.sort(reverse=True)
        
        # calculates Q1, Q3, and IQR for a given file
        self.q1 = float(self.sorted[int(0.25 * len(self.sorted))])
        self.q3 = float(self.sorted[int(0.75 * len(self.sorted))])
        self.iqr = (float(self.q3) - float(self.q1))
        self.outlierlines = []

    def findOutliers(self):
        # calculates valid range (Q1 - (1.5 * IQR) to Q3 + (1.5 * IQR))
        maxval = self.q3 + 1.5*self.iqr
        minval = self.q1 - 1.5*self.iqr

        # creates an array of line #s for outliers
        for i in range(1, len(self.infile)):
            if(float(self.infile[i]) > maxval) or (float(self.infile[i]) < minval):
                self.outlierlines.append(i)
        print("Number of Outliers: ",len(self.outlierlines))
    
    def removeOutliers(self):
        self.outlierlines.sort(reverse=True) # sort in descending order so removals do not affect line numbers
        for val in self.outlierlines:
            del self.infile[val]
        return(self.infile)

    def concat(self, infile, finalFilename):
        # stitch files back together in original format
        with open(finalFilename, "a") as outfile:
            for line in infile:
                outfile.write(line + "\n")
        print(open(finalFilename, "r").read())

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

############################################################## MAIN ##############################################################

def main():
    # definitely could be cleaner
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
            outliers = Outliers(infile) # Create a new instance of Outliers class
            outliers.findOutliers()
            cleaned = outliers.removeOutliers()

            # create a file called something like 'xaccelclean', append to the end
            with open(root+j+"clean", "a") as outfile:
                for val in cleaned:
                    outfile.write(val.strip()+"\n")

            # remove(root+i+j) # remove some files to reduce clutter
        # remove(root + i)

    # calculating the averages
    for i in names:
        infile = open(root + i + 'xaccel').read().split("\n")
        del infile [-1]
        del infile [-1]
        xaverages.append(avgfn(infile))
        print(xaverages)
        # done with this today I think

    print("cleaning...")

    # create a gnuplot script in the active folder
    # probably a better way to do this, 
    # but I couldn't get a gnuplot script to run from another folder
    with open(root+"plot_accel.gp", "w") as outfile:
        outfile.write("set term png\n")                      # output is png
        outfile.write("set output 'accel_clean.png'\n")       # name output
        outfile.write("plot '" + root + "xaccelclean' w lines title " +  # plot xaccel and y accel
        "'X Accel', (" + str(xaverages[0]) +"), (" + str(xaverages[-1]) + "), '"+ root + "yaccelclean' w lines title 'Y Accel'\n")
        outfile.write("unset output")
    system('gnuplot ' + root + 'plot_accel.p')               # run the gnuplot script created
    print("plot created.")

####################################################################################################################################

if __name__ == '__main__':
    main()