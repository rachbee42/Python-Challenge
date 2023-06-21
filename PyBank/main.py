# Modules
import os
import csv

# Check path
os.chdir("/Users/rsbri/python-challenge/PyBank")
print(os.getcwd())

# Set import path
csv_import = os.path.join('Resources', 'budget.csv')

# Set output path
output_path = os.path.join('Analysis', 'analysis.txt')

# Open and read csv file
with open(csv_import) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    
    # Read the header row first
    csv_header = next(csvreader) 
    
    # Read each row thereafter and return: 
    firstrow = next(csvreader)
    total_net = 0
    total_change = 0
    total_months = 1
    total_change_month = 0
    total_net = total_net + int(firstrow[1])
    previous_profitloss = int(firstrow[1])
    greatest_increase = 0
    greatest_increase_month = ""
    greatest_decrease = 0
    greatest_decrease_month = ""
    
    for row in csvreader:
                
        # The total number of months 
        total_months = total_months + 1
        
        # The net amount of profit/losses over the entire period
        #current_profitloss = 0
        current_profitloss = int(row[1])
        total_net = total_net + current_profitloss
        
        # The changes in proft/losses over the entire period, and then the average of those changes
        profit_change = current_profitloss - previous_profitloss
        total_change = total_change + profit_change
        previous_profitloss = current_profitloss
        total_change_month = total_change_month + 1
        
        # The greatest increase in profits (date and amount) over the entire period
        if profit_change > greatest_increase: 
            greatest_increase = profit_change
            greatest_increase_month = row[0]
               
        if profit_change < greatest_decrease: 
            greatest_decrease = profit_change
            greatest_decrease_month = row[0]

# Display analysis
output = f"""
Election Results
----------------
Total months: {total_months}
Total net: ${total_net:,}
Average change: ${total_change / total_change_month:,.2f}
Greatest increase in profits: {greatest_increase_month} (${greatest_increase:,})
Greatest decrease in profits: {greatest_decrease_month} (${greatest_decrease:,}) 
"""

print(output)

# Write analysis to a text file
with open(output_path, 'w') as textfile:
    textfile.write(output)