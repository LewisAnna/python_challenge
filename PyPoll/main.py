import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

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
    print("Election Results")
    print("--------------------------")
    total_votes = len(candidate_list)
    print(f"Total Votes: {total_votes}")
    print("--------------------------")
    for key, value in candidate_count.items():
        print(f"{key}: {round((100/total_votes)*value,3)}% ({value})")
    print("--------------------------")
    print(f"Winner: {max_key}")
    print("--------------------------")