import os
import csv

# file path to collect data within the resource folder
budgetFile = os.path.join('.','Resources','budget_data.csv')

# create lists - months and profit/loss - and dict
list_net_changes = []
list_months = []
date_profit = {}

# define variables
previous_change = 0
total_change = 0
months = 0

# open and read csv file
with open(budgetFile) as budget_csv:
    budget_reader = csv.reader(budget_csv, delimiter=',')
    
    # extract header
    header = next(budget_reader)
    first_row = next(budget_reader)
    
    # set variables
    net_change = int(first_row[1])
    previous_change = net_change
    total_change = net_change
    months = 1
    
    for row in budget_reader:
        # find total count of months
        months = months + 1
        # find the net profit/loss - changes in profit/loss over the period
        total_change = total_change + int(row[1])
        net_change = int(row[1]) - previous_change
        previous_change = int(row[1])
        list_net_changes.append(net_change)
        
        # populate list with all months
        if row[0] not in list_months:
                list_months.append(row[0])
      
# find avg change over the given period  
avg = sum(list_net_changes) / len(list_net_changes)

# find greatest profit/loss amounts
max_change = max(list_net_changes)
min_change = min(list_net_changes)

# formatting
total_change = "${:.0f}".format(total_change)
avg_change = "${:.2f}".format(avg)
max_change = "${:.0f}".format(max_change)
min_change = "${:.0f}".format(min_change)


# combine lists into dict
date_profit = dict(zip(list_months, list_net_changes))

# find month in which greatest profits and losses occurred
greatest_profit = max(date_profit, key=date_profit.get)
greatest_loss = min(date_profit, key=date_profit.get)


# print results
print('Financial Analysis\n-------------------------')
print('Total Months: ' + str(months))
print('Total: ' + str(total_change))
print('Average Change: ' + str(avg_change))
print('Greatest Increase in Profits: ' + greatest_profit + ' ' + '(' + str(max_change) + ')')
print('Greatest Decrease in Profits: ' + greatest_loss + ' ' + '(' + str(min_change) + ')')