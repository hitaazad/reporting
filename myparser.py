import csv     # imports the csv module
import sys      # imports the sys module
from milestone import Milestone
class Myparser:

    def __init__(self, instring):
        print "start Myparser init"
        global filename
        filename = instring
        print "end Myparser init filename: %s" % filename

    def start(self):
        print "start Myparser.start "
        allmilestones =[]
        f = open(filename, 'r') # opens the csv file
        reader = csv.reader(f, delimiter=',')  # creates the reader object with delimer comma
        for row in reader:   # iterates the rows of the file in orders
            if row[0] is not None:
                vertical = row[0]
            milestone = Milestone(vertical,row) #create a milestone with current vertical
            allmilestones.append(milestone)  #append the current milestone to the array of milestones

        f.close()      # closing
        # print allmilestones[0].vertical
        # print allmilestones[2].vertical
        #print [milestone.vertical for milestone in allmilestones]#print [class.variable for class in list]
        print "end Myparser.start"
        return allmilestones
