# Modules
import os
import csv
from statistics import mean

# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Variable that stores number of months(rows)
    monthcount=0

    # Variable that stores total Profit/Losses
    total=0

    # Dictionary that will store the monthly changes
    monthchange={}

    # Jumps the header of the dataset
    next(csvreader)

    # Loop through the file
    for row in csvreader:

        # Sums one to the month counter
        monthcount= monthcount + 1

        # Sums the profit/loss of each month
        total=total+int(row[1])

        # The program only calculates the monthly change on the second month and onwards 
        # to make sure that there is a value associated with a previews month
        if monthcount >= 2:

            # Adds the monthly change and date to the dictionary
            monthchange.update({row[0]:int(row[1])-int(monthPL)})

        # Stores the value of Profit/Loss for the operation in the next month
        monthPL=row[1]

    # Calculates the average of the monthly changes in Profit/Losses
    average=mean(int(monthchange[k]) for k in monthchange)

    # Finds the max value in the monthly changes dictionary
    max_key = max(monthchange, key=monthchange.get)

    # Finds the min value in the monthly changes dictionary
    min_key = min(monthchange, key=monthchange.get)

# Creates a txt file for writing
file = open('FinancialAnalysis.txt','w')

# Prints the results
print("\nFinancial Analysis")
file.write("Financial Analysis")
print("---------------------------------------")
file.write("\n---------------------------------------")
print(f'Total Months: {monthcount}')
file.write(f'\nTotal Months: {monthcount}')
print(f'Total: ${total}')
file.write(f'\nTotal: ${total}')
print(f'Average Change: {"{0:.2f}".format(average)}')
file.write(f'\nAverage Change: {"{0:.2f}".format(average)}')
print(f'Greatest Increase in Profits: {max_key} (${monthchange[max_key]})')
file.write(f'\nGreatest Increase in Profits: {max_key} (${monthchange[max_key]})')
print(f'Greatest Decrease in Profits: {min_key} (${monthchange[min_key]})\n')
file.write(f'\nGreatest Decrease in Profits: {min_key} (${monthchange[min_key]})')