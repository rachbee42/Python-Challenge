# Modules
import os
import csv

# Check path
os.chdir("/Users/rsbri/python-challenge/PyBank/")
print(os.getcwd())

# Set import path
csvpath_import = os.path.abspath('Resources/budget.csv')

# Set output path
output_path = os.path.abspath('Analysis/analysis.txt')

# Set financial parameters
total_months = 0
total_net = 0
list_months = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999]

# Open and read csv
with open(csvpath_import) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first
    csv_header = next(csvreader)
    print(f"Header: {csv_header}")
    
    #len(list_months) = list_months
    #for row in csvreader:
        #if row:
            #print("Total Months: " + list_months)
    
    # Loop through file to obtain data
    # The total number of months included in the dataset
    #for row in csvreader:
        #if row[0, 1]:
            #print("Total months: " + len(total_months))

    #for row in csvreader:
        #sum_totalmonths = len(row)  
        #if row[0]:
        #print("Total Months: " + str())


    # The net total amount of "Profit/Losses" over the entire period


    # The changes in "Profit/Losses" over the entire period, and then the average of those changes


    # The greatest increase in profits (date and amount) over the entire period


    # The greatest decrease in profits (date and amount) over the entire period




# Open output file using "write mode"
#with open(output_path, 'w') as textfile:
    #writer = csv.writer(textfile)

# write the header row
#print("""Financial Analysis
#------------------
#""")

# write
#writer.writerow()