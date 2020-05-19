# will just get the averages from the sine curve.
# going to try to not be too extra about it....

# ******************* VARIABLES *******************
numLines = 2400 # at end of filename probably
numSteps = 80   # number of steps in the circle
pointsPer = 30  # number of data points per step
spacing = 1    # how many steps I want to go
degrees = 4.5   # number degrees per step

root = "C:\\Users\\alyss\\Documents\\arduino-compass\\five_degree_data\\"
filename = "starting_north-2400"

# **************** FUNCTIONS *****************

def getPeaks(filename):
    xaccel, yaccel = getData(filename)
    xavgs = []
    yavgs = []

    # travels through and just hits the directions you want.
    for i in range(0, numSteps, spacing):    
        xavg = 0
        yavg = 0

        for j in range(0,pointsPer):
            # print(j+i*pointsPer)
            xavg = (xavg + xaccel[i*pointsPer+j])/2
            yavg = (yavg + yaccel[i*pointsPer+j])/2
        
        xavgs.append(round(xavg, 3))
        yavgs.append(round(yavg, 3))
    print("MAXIMUM X: ", max(xavgs))
    print("MINIMUM X: ", min(xavgs))
    print("MAXIMUM Y: ", max(yavgs))
    print("MINIMUM Y: ", min(yavgs))
    writeAverages(xavgs, yavgs, filename + "-avgs.txt")

def writeAverages(xavgs, yavgs, outfilename):
    with open(outfilename, "w") as outfile:
        i = 360

        while i > 0:
            outfile.write(str(i)+",")
            i -= 4.5

        outfile.write("\n")

        for i in xavgs:
            outfile.write(str(i)+",")
        outfile.write("\n")

        for i in yavgs:
            outfile.write(str(i)+",")
    print("avgs file created")
            

def getData(filename):
    infile = open(filename).read().split("\n")
    xaccel = []
    yaccel = []
    for line in infile:
        columns = line.split("\t")
        xaccel.append(float(columns[0]))
        yaccel.append(float(columns[1]))
    return(xaccel, yaccel)

def printAverage():
    print("not yet implemented")

def average():
    print("not yet implemented")

# ******************* MAIN ******************

def main():
    getPeaks(root + filename)

if __name__ == "__main__":
    main()