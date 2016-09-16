class Markdown:

    def __init__(self):
        print "start Markdown init"
        print "end Markdown init filename"

    def genmarkdown(self, allmilestones):
        print [milestone.vertical for milestone in allmilestones]
