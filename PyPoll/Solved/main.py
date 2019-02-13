import os
import csv

voters=0
votes={}

csvpypoll = os.path.join('..', 'Resources', 'election_data.csv')
poll_output = os.path.join("analysis", "poll_results.txt")

with open(csvpypoll, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    for row in csvreader:
        voters+=1
        votes.update({row[2]: 0})


with open(csvpypoll, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    for x in votes:
        for row in csvreader:
            if row[2] in votes:
                votes[row[2]]=votes[row[2]]+1

candidates_votes=[]
temp=[]
for key, value in votes.items():
    temp = [key,value]

candidates_votes.append(temp)
candidates_votes.sort(key=lambda x: x[1], reverse=True)

winner_name_get = []
winner_percent_get = []
winner_votes_get = []
winner_get = []

for i in range(0,len(candidates_votes)):

    winner_name = candidates_votes[i][0]
    winner_percent = round(candidates_votes[i][1]*100/voters,3)
    winner_votes = candidates_votes[i][1]
    winner = candidates_votes[0][0]

    winner_name_get.append(winner_name)
    winner_percent_get.append(winner_percent)
    winner_votes_get.append(winner_votes)
    winner_get.append(winner)

   

output = (
"\nElection Results\n"
"-------------------------\n"
f"Total Votes: {voters}\n"
"-------------------------\n"
f"\n{winner_name_get[0]}: {winner_percent_get[0]}% ({winner_votes_get[0]})\n"
"-------------------------\n"
f"Winner: {winner_get[0]}\n"
"-------------------------\n" )


print(output)

with open(poll_output, "w") as text_file:
    text_file.write(output)
