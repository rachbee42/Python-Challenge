# Modules
import os
import csv
import operator

# Check path
os.chdir("/Users/rsbri/python-challenge/PyPoll")
print(os.getcwd())

# Set import path
csv_import = os.path.join('Resources', 'election_data_pypoll.csv')

# Set output path
output_path = os.path.join('Analysis', 'analysis.txt')

# Define variables
count_votes = 0
count_charles = 0
count_diana = 0
count_raymon = 0 
candidate_charles = "Charles Casper Stockham"
candidate_diana = "Diana DeGette"
candidate_raymon = "Raymon Anthony Doane"
pc_charles = 0
pc_diana = 0
pc_raymon = 0

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
        
        # Then loop through rows to return vote count by candidate
        # The total number of votes each candidate won
        candidate_row = row[2]
        
        if candidate_row == candidate_charles: count_charles = count_charles + 1
        elif candidate_row == candidate_diana: count_diana = count_diana + 1
        elif candidate_row == candidate_raymon: count_raymon  = count_raymon + 1
        
        # Then loop through rows to return the percentage of each candidate's votes
        # The percentages of votes each candidate won
        pc_charles = count_charles / count_votes * 100
        pc_diana = count_diana / count_votes * 100
        pc_raymon = count_raymon / count_votes * 100

        # The winner of the election based on popular vote
        pc_dict = {
            'Charles Casper Stockham':pc_charles,
            'Diana DeGette':pc_diana,
            'Raymon Anthony Doane': pc_raymon
            }
        
        winner = max(pc_dict.items(), key=operator.itemgetter(1))[0]
        
# Display analysis
output=f"""
Election Results
--------------------
Total Votes: {count_votes:,}
--------------------
Charles Casper Stockham: {pc_charles:.3f}% ({count_charles:,})
Diana Degette: {pc_diana:.3f}% ({count_diana:,})
Raymon Anthony Doane: {pc_raymon:.3f}% ({count_raymon:,})
--------------------
Winner: {winner}
--------------------
"""
print(output)

# Write analysis to a text file
with open(output_path, 'w') as textfile:
    textfile.write(output)

