class Milestone:

    def __init__(self, vertical, row):
        #['Vertical', 'Goal', 'Workstreams', 'Workstream Status', 'Completion Target', 'Highlight', 'Gap', 'People', '']
        #print '*****************************start Milestone init*****************************'
        self.vertical = vertical
        self.content = row
        self.milestonename = row[2]
        self.milestone_status = row[3]    # row 3 = Workstream Status
        self.completion_target_data = row[4]    # row 4 = Completion Target
        #self.completetion_eta
        self.highlight = row[5] # row 5 = Highlight
        self.risk = row[6]    # row 6 = Gap
        self.poc = row[7]    # row 7 = People
        # self.status = status
        # other items to include in future
        # self.impact = impact
        # self.notes = notes
        #print '*****************************end Milestone init*****************************'

    def __repr__(self):
        return '__repr__'
