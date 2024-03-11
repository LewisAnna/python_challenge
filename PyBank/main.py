import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')


months = []
change = []
total = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    first_row = next(csvreader)
    prev_net = int(first_row[1])
    total.append(int(first_row[1]))
    months.append(first_row[0])    
    for row in csvreader:
        net_total = int(row[1])
        changes = net_total - prev_net
        prev_net = net_total
        change.append(changes)
        month = str(row[0])
        months.append(month) 
        total.append(net_total)
    min_change = (min(change))
    max_change = (max(change))
    Average_Change = sum(change)/len(change)
    rounded_average = round(Average_Change, 2)
    min_index = change.index(min_change)
    max_index = change.index(max_change)
    row_index_max = months[max_index+1]
    row_index_min = months[min_index+1]
    print("Financial Analysis")
    print("------------------------")
    print(f"Total Months: { len(months)}")
    print(f"Total: ${sum(total)}")
    print(f"Averag Change: ${rounded_average}")
    print(f"Greatest Increase in Profits: { row_index_max} (${max_change})")
    print(f"Greatest Decrease in Profits: { row_index_min} (${min_change})")   