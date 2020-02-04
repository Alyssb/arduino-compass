'''
Alyssa Slayton 01/29/2020
My first python module
'''
'''
A python script which:
    Cleans data
        takes a file
        calculates and removes outliers
'''
class Outliers:
    def __init__(self, infile):
        self.infile = infile

        # sorts infile in ascending order
        self.sorted = infile.copy()
        self.sorted.sort()
        # corrects if the file had both positive and negative numbers
        print(self.sorted[-1][0])
        if(self.sorted[-1][0] == '-'):
            self.sorted.sort(reverse=True)
        
        # calculates Q1, Q3, and IQR for a given file
        self.q1 = float(self.sorted[int(0.25 * len(self.sorted))])
        self.q3 = float(self.sorted[int(0.75 * len(self.sorted))])
        self.iqr = (float(self.q3) - float(self.q1))
        self.outlierlines = []

    def findOutliers(self):
        # calculates valid range (Q1 - (1.5 * IQR) to Q3 + (1.5 * IQR))
        maxval = self.q3 + 1.5*self.iqr
        print("MAXVAL: ",maxval)
        minval = self.q1 - 1.5*self.iqr
        print("MINVAL: ",minval)

        # creates an array of line #s for outliers
        for i in range(1, len(self.infile)):
            if(float(self.infile[i]) > maxval) or (float(self.infile[i]) < minval):
                # print("CURRENT VAL: ",self.infile[i])
                self.outlierlines.append(i)
        print("Number of Outliers: ",len(self.outlierlines))
    
    def removeOutliersFn(self):
        self.outlierlines.sort(reverse=True) # sort in descending order so removals do not affect line numbers
        for val in self.outlierlines:
            del self.infile[val]
        return(self.infile)

    def replaceFile(self, filename):
        with open(filename, "w") as outfile:
            for line in self.infile:
                outfile.write(line + "\n")

    def concat(self, infile, finalFilename):
        # stitch files back together in original format
        with open(finalFilename, "a") as outfile:
            for line in infile:
                outfile.write(line + "\n")
        print(open(finalFilename, "r").read())


def main():
    print("main function of removeOutliers.py")

if __name__ == "__main__":
    main()