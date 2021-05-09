import os
import csv

# file path to collect data within the resorce folder
budgetFile = os.path.join('.','Resources','budget_data.csv')


# open and read csv file
with open(budgetFile) as budget_csv:
    budget_reader = csv.reader(budget_csv, delimiter=',')
    
    
    # header = next(budget_reader) - returned count of 85 when ran
    # begRow = next(budget_reader)
    # totalMonths = str(len({row[0] for row in budget_reader}))
    # profitLoss = []
    
    for row in budget_reader:
        
        # ignore below comments
        # profitLoss.append([row[0], int(row[1])])
        # totalMonths = totalMonths + 1
        # # print(row[1])
        # print(totalMonths)
        
        # find total count of months
        months = str(len(list(budget_reader)))


print("Financial Analysis\n------------------------")
print('Total Months: ' + months)
