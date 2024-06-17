import os
import csv
import numpy as np

#find the csv file
budget_csv = os.path.join("Resources","budget_data.csv")
                          
#create empty lists for months, profit and change in profit
months = []
profit = []
changeinprofit = []

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #skip first row (the column headers)
    header = next(csvreader)


    for row in csvreader:
        #add to list of months and profit
        months.append(row[0])
        profit.append(int(row[1]))
    for i in range(len(profit)-1): # change in profit list is one row less than the profit list
        changeinprofit.append(profit[i+1] - profit[i])

num_months = len(months) #total months
total_profit = sum(profit) #total profit
averageprofit_change = round(np.mean(changeinprofit),2) #average change in profit, rounded to 2 decimals

max_changeinprofit = max(changeinprofit) #max change in profit
min_changeinprofit = min(changeinprofit) #min change in profit

#for finding the dates below, the index needs to be +1 bc the change in profit list has one fewer row than the profit list
date_max = months[changeinprofit.index(max_changeinprofit) + 1] #date of the greatest increase
date_min = months[changeinprofit.index(min_changeinprofit) + 1] #date of lowest increase

print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {num_months}')
print(f'Total: ${total_profit}')
print(f'Average Change: ${averageprofit_change}')
print(f'Greatest Increase in Profits: {date_max} (${max_changeinprofit})')
print(f'Greatest Decrease in Profits: {date_min} (${min_changeinprofit})')

results = os.path.join('analysis','results.txt') #create txt file
        
with open(os.path.join('analysis','results.txt'), 'w') as file:
#write all the info in using new lines and change all variables to string date types
    file.write('Financial Analysis'+'\n')
    file.write('----------------------------' + '\n')
    file.write('Total Months: ' + str(num_months) + '\n')
    file.write('Total: $' + str(total_profit) + '\n')
    file.write('Average Change: $' + str(averageprofit_change) + '\n')
    file.write('Greatest Increase in Profits: ' + str(date_max) + ' $' + str(max_changeinprofit) + '\n')
    file.write('Greatest Decrease in Profits: ' + str(date_min) + ' $' + str(min_changeinprofit))




