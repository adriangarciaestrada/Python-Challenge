#Modules
import os
import csv
import collections, functools, operator

# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #VotecounterVariable that will store the total number of votes
    votecounter=0

    #Dictionary that stores the votes for each candidate
    votes={}

    #Jumps the header of the dataset
    next(csvreader)

    #Loop through the file
    for row in csvreader:

        # Counts the votes one by one
        votecounter = votecounter +1

        # Conditional that checks in the dictionary for a the candidate that is voted in the current row, 
        # if the candidate is not in the dictionary,
        if row[2] not in votes:
            
            # If the condition is true, adds a new candidate to de dictionary and assigns a value of 1 vote to that key
            votes.update({row[2]:1})

        # If the candidate is already in the dictionary
        else:
            
            # Just sums 1 to the value related to the current candidate key 
            # and adds it as the new value for that candidates key
            votes[row[2]]=votes.get(row[2], "")+1

# Creates a txt file for writing
file = open('PollResults.txt','w')

# Prints the general results in the terminal and in the txt
print("\nElection Results")
file.write("Election Results")
print("--------------------------------")
file.write("\n--------------------------------")
print(f'Total Votes: {votecounter}')
file.write(f'\nTotal Votes: {votecounter}')
print("--------------------------------")
file.write("\n--------------------------------")

#Loops through the number of keys in the candidates dictionary
for candidate in votes:

    #Calculates the percentage of votes for the current candidate key
    percent=(int(votes.get(candidate,""))/votecounter*100)

    # Prints the result for the current candidate key
    print(f'{candidate}: {"{0:.3f}".format(percent)}% ({votes.get(candidate,"")})')
    file.write(f'\n{candidate}: {"{0:.3f}".format(percent)}% ({votes.get(candidate,"")})')

# Finds the max value of votes per candidate in the dictionary and returns the Key(name of the winner)
max_key = max(votes, key=votes.get)

print("--------------------------------")
file.write("\n--------------------------------")
print(f'Winner: {max_key}')
file.write(f"\nWinner: {max_key}")
print("--------------------------------\n")
file.write("\n--------------------------------")