# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("resources", "budget_data.csv")

greatest_increase =0
greatest_decrease =0
months =[]
profit =[]
monthly_diff =[]
changes_totaled =0
total_changes =0
average_change =0
months_total =0

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    #list values for months and profit
    total_profit=0
    for row in csvreader:
        total_profit += int(row[1])
        months.append(row[0])
        profit.append(row[1])

    # iterate through and calculate change in profit month-to-month
    profit = [int (i) for i in profit]
    months_total = len(months)
    for i in range(0, months_total-1):
        monthly_diff.append(int(profit[i+1]-profit[i]))

    #Calculate Max, Min, Average and totals.  then capture month of greates increase and decrease.
    greatest_increase = max(profit)
    greatest_decrease = min(profit)
    changes_totaled = sum(monthly_diff)
    total_changes = len(monthly_diff)
    MaxDateSpot=profit.index(greatest_increase)
    MinDateSpot=profit.index(greatest_decrease)
    increase_month=months[MaxDateSpot]
    decrease_month=months[MinDateSpot]
    average_change = (changes_totaled/total_changes)

    # print results
    print (f'Financial Analysis: \
    \n  Total Months: {months_total} \
    \n  Total Profit: ${total_profit} \
    \n  Average Change: ${average_change} \
    \n  Greatest Increase in Profits: {increase_month} (${greatest_increase}) \
    \n  Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})')

# set output path and file name.
output = os.path.join("analysis", "budget_analysis.csv")
with open(output, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    # create lists
    lables=['Label', 'total months', 'total profit', 'average change', 'greatest increase month', 'greatest increase', 'greatest decrease month', 'greatest decrease', ]
    data=['Data', months_total, total_profit, average_change, increase_month, greatest_increase, decrease_month, greatest_decrease]
    # convert list to rows and write to .csv
    rows=zip(lables, data)
    for row in rows:
        csvwriter.writerow(row)

    # # print (res)
    # # print (profit)
    # # print (total_changes)
    # # calculate average change
    # # average_change = sum(int(monthly_diff))
    # print (greatest_increase)
    # print (greatest_decrease)
    # print (average_change)
    # print (increase_month)
    # print (decrease_month)
    # # print (monthly_diff[i])
    # print (total_profit)
    # # print (months_total)
    # # print (greatest_increase)
    # # print (greatest_decrease)



    
