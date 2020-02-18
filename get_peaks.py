# will just get the averages from the sine curve.
# going to try to not be too extra about it....

# ******************* VARIABLES *******************
numSteps = 80   # number of steps in the circle
pointsPer = 30  # number of data points per step
spacing = 10    # how many steps I want to go
degrees = 4.5   # number degrees per step

root = "C:\\Users\\alyss\\Documents\\arduino-compass\\five_degree_data\\"
filename = "starting_north-2400"

# **************** FUNCTIONS *****************

def getData(filename):
    infile = open(filename).read().split("\n")
    xaccel = []
    yaccel = []
    for line in infile:
        columns = line.split("\t")
        xaccel.append(float(columns[0]))
        yaccel.append(float(columns[1]))
    print(xaccel)
    print(infile)

def printAverage():
    print("not yet implemented")

def average():
    print("not yet implemented")

# ******************* MAIN ******************

def main():
    getData(root + filename)

if __name__ == "__main__":
    main()