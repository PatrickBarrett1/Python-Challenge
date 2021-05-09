import os
import csv

pollFile = os.path.join(".", "Resources", "election_data.csv")

with open(pollFile, 'r') as poll_csv:
    poll_reader = csv.reader(poll_csv, delimiter=',')
    
    # extract header 
    header = next(poll_reader)
    
    for row in poll_reader:
        # find total count of voters
        voters = str(len(list(poll_reader)))

print("Election Results\n-----------------------")
print("Total Votes: " + voters)
            

    