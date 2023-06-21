# Modules
import os
import csv

# Check path
os.chdir("/Users/rsbri/python-challenge/PyPoll")
print(os.getcwd())

# Set import path
csv_import = os.path.join('Resources', 'election_data_pypoll.csv')

# Set output path
output_path = os.path.join('Analysis', 'analysis.txt')

# Define variables
count_votes = 0
candidate_list = []
candidate_dict = {}
to_add = 0

# Open and read csv file
with open(csv_import) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
   
    # Read the header row first
    csv_header = next(csvreader)
    print(f"Headers: {csv_header}") 
    
    #Read each row thereafter and return: 
    for row in csvreader:
                
        # The total number of votes
        count_votes = count_votes + 1
        
        # A complete list of candidates who received votes
        #candidate = row[2]
        #print(row)
        #break
        
        if candidate not in candidate_list:

            # Add it to the list of candidates in the running
            candidate_list.append(candidate)

            # And begin tracking that candidate's voter count
            candidate_dict[candidate] = 0
            
        # Then add a vote to that candidate's count
        candidate_dict[candidate] = candidate_dict[candidate] + 1

        # The percentage of votes each candidate won
        #percentage = []
        
        
        # The total number of votes each candidate won
        # The winner of the election based on popular vote

output=f"""
Election Results
--------------------
Total Votes: {count_votes}
--------------------
Charles Casper Stockham: {candidate}
Diana Degette: {candidate}
Raymon Anthony Doane: {candidate}
--------------------
Winner: {to_add}
--------------------
"""
print(output)

# Write analysis to a text file
with open(output_path, 'w') as textfile:
    textfile.write(output)

