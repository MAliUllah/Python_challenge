import csv
import os

file1=os.path.join("Resources","election_data.csv")

with open(file1, newline="") as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    csvheader=next(csvreader)
    candidate_roster=[candidate[2] for candidate in csvreader]


vote_total=len(candidate_roster)

candidate_votes=[[candidate,candidate_roster.count(candidate)] for candidate in set(candidate_roster)]

candidates_sorted=sorted(candidate_votes, key=lambda x:x[1], reverse=True)

for candidate in candidates_sorted:
    percentage=(candidate[1]/vote_total)*100
    print(f'{candidate[0]}:{percentage:6.3f}%({candidate[1]})') #!

print("--------------------------------------------")
print("The total of votes are "+ str(vote_total))
print(candidates_sorted)
print("Above are the candidates who recieved votes")
for candidate in candidates_sorted:
    percentage=(candidate[1]/vote_total)*100
    print(f'{candidate[0]}: {percentage:6.3f}% ({candidate[1]}) Candidate info')
print(f'{candidates_sorted[0][0]} is the winner')

analysis_file=os.path.join("Analysis", "PyPoll_analysis.txt")

with open(analysis_file, "w") as txtfile:
    print("--------------------------------------------", file=txtfile)
    print("The total of votes are "+ str(vote_total), file=txtfile)
    print(candidates_sorted, file=txtfile)
    print("Above are the candidates who recieved votes", file=txtfile)
    for candidate in candidates_sorted:
        percentage=(candidate[1]/vote_total)*100
        print(f'{candidate[0]}: {percentage:6.3f}% ({candidate[1]}) Candidate info', file=txtfile)
    print(f'{candidates_sorted[0][0]} is the winner', file=txtfile)
