import csv
import os

#csvpath
csvpath = os.path.join("Resources", "election_data.csv")

#variables
total_votes = 0
candidate_votes = {}
candidates = []

#read csv
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #skip header
    header = next(csvreader)

    #loop through rows
    for row in csvreader:
        total_votes += 1
        candidate = row[2]

        #count votes for each candidate
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1
            candidates.append(candidate)

#determine winner
winner = max(candidate_votes, key=candidate_votes.get)

#calculate percentage of votes for each candidate and format the output
results = []
results.append("Election Results")
results.append("-------------------------")
results.append(f"Total Votes: {total_votes}")
results.append("-------------------------")
for candidate in candidates:
    vote_count = candidate_votes[candidate]
    percentage = (vote_count / total_votes) * 100
    results.append(f"{candidate}: {percentage:.3f}% ({vote_count})")
results.append("-------------------------")
results.append(f"Winner: {winner}")
results.append("-------------------------")

#print results to terminal
print(results)

#export results to a text file
output_file = os.path.join("analysis", "election_results.txt")
with open(output_file, "w") as txtfile:
    txtfile.write("\n".join(results) + "\n")

print(f"\nResults have been exported to: {output_file}")