import os
import csv

pollFile = os.path.join(".", "Resources", "election_data.csv")

# create empty list of candidate names
candidate_list = []
# create dict for candidates and votes
candidate_votes = {}

# define variables
voters = 0
percent_votes = 0

# read in file 
with open(pollFile, 'r') as poll_csv:
    poll_reader = csv.reader(poll_csv, delimiter=',')
    # extract header 
    header = next(poll_reader)
    
    for row in poll_reader:
        # find total count of voter
        voters = voters + 1
        
        # append list and populate dict
        if row[2] not in candidate_list:
            # populate list with candidates
            candidate_list.append(row[2])
            candidate_votes[row[2]] = 0
        # total up votes by candidate
        candidate_votes[row[2]] = candidate_votes[row[2]] + 1

# print results - total votes casted
print("Election Results\n-------------------------")
print("Total Votes: " + str(voters) + "\n-------------------------")

# extract votes from dict by candidate
for candidate in candidate_votes:
    votes = candidate_votes[candidate]
    
    # calc vote % - (candidate votes / total votes)
    percentVotes = votes / voters
    # format as percent - three decimals 
    percent_votes = "{:.3%}".format(percentVotes)
    
    # print voting results
    print(candidate + ": " + str(percent_votes) + " (" + str(votes) + ")")

# find candidate with most votes 
winner = max(candidate_votes, key=candidate_votes.get)

# print winner 
print("-------------------------" + "\nWinner: " + str(winner)+ "\n-------------------------")

