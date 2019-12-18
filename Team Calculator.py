

# who is in the meeting this list gets updated via the buttons
Team = ['CEO', 'Director', 'Manager', 'Coordinator', 'Team']

# minute rate for each level
Rate = {'CEO': 100, 'Director': 50, 'Manager': 35, 'Supervisor': 25, 'Coordinator': 15, 'Team': 9}

# sum up the current cost
cost = sum([Rate[x] for x in Team])
