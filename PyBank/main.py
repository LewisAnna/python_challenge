import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')
file_to_output = os.path.join('Analysis', 'pybank.txt' )


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
    print_out =("Financial Analysis\n"
                "------------------------\n"
                 f"Total Months: { len(months)}\n"
                 f"Total: ${sum(total)}\n"
                 f"Average Change: ${rounded_average}\n"
                 f"Greatest Increase in Profits: { row_index_max} (${max_change})\n"
                 f"Greatest Decrease in Profits: { row_index_min} (${min_change})\n") 
    print(print_out)
with open(file_to_output, "w") as writefile:
   writefile.write(print_out)

                  