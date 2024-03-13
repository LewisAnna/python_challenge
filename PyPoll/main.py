import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')
file_to_output = os.path.join('Analysis', 'pypoll.txt' )

candidate_list = []
candidate_count = {}


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        candidate = str(row[2])
        candidate_list.append(candidate)
    for cand in candidate_list:
        if cand in candidate_count:
            candidate_count[cand]+= 1
        else:
            candidate_count[cand] = 1
    max_key = max(candidate_count, key=candidate_count.get)

    max_value = candidate_count[max_key]
    total_votes = len(candidate_list)
    print_out = (
    "Election Results\n"
    "--------------------------\n"
    f"Total Votes: {total_votes}\n"
    "--------------------------\n")
    print_more = ("--------------------------\n"
    f"Winner: {max_key}\n"
    "--------------------------")
    
    #for key, value in candidate_count.items():
        #print(f"{key}: {round((100/total_votes)*value,3)}% ({value})\n")
    y = 0
    for key, value in candidate_count.items():
        x = (f"{key}: {round((100/total_votes)*value,3)}% ({value})\n") 
        print_out = print_out + x 
        
    print(print_out)
    print(print_more)
with open(file_to_output, "w") as writefile:
   writefile.write(print_out)
   writefile.write(print_more)