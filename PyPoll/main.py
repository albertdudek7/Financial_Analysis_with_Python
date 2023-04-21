#file that will run the main script for each analysis
#load csv libraries

import csv
import os 

#file path to budget data

csvpath = r"C:\Users\Albert Dudek\Workspace\python-challenge-main\PyPoll\Resources\election_data.csv"

output_path = os.path.join("analysis","election_results.txt")


#define variables to be used in code
#totalvotes as an int
#candidate votes as a dictionary
totalvotes = 0
candidates_votes = {}
totalvotesforcandidate = 0
maxvotes = 0

#winner defined by string value
winner=""

#csv file format: (0)Ballot ID, (1)County, (2)Candidate


#opening the data file:budget data and using reader

with open(csvpath, mode='r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    #Loop through each row in the CSV File
    for row in csvreader:
        
        #adding number of total votes cast
        totalvotes += 1

        #gather Candidate names from row 2
        candidatename = row[2]


        #compiling total votes for each candidate

        if candidatename not in candidates_votes:
            candidates_votes[candidatename] = 1

        else:
            candidates_votes[candidatename] += 1

    print("Election Results")
    print("---------------------------")
    print(f"Total Votes: {totalvotes}") 
    print("---------------------------")  

    for candidatename,votes in candidates_votes.items():

       
        percentage_of_votes = round((votes / totalvotes) * 100, 3)

        
    # probably the hardest part of the script for me was to print and display the candidates in order
    #after much trial and error I was able to get the appropriate text display, I realized I needed to index [candidatename] after candidate votes. Sigh of a relief
        
        print(f"{candidatename}: {percentage_of_votes}% ({candidates_votes[candidatename]})")

        



    winnervotes = max(candidates_votes.values())

    #indexing list to print out Winning Candidate below
    #used powerpoint presentation to get the right code below

    winner = list(candidates_votes.keys())[list(candidates_votes.values()).index(winnervotes)]
            #sorted_candidatename = sorted(candidatename)

















# print results from election_date

             

print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")



# output results to textfile

#analysis\results.txt


with open("analysis\election_results.txt","w") as f:
    f.write("Election Results")
    f.write("\n")
    f.write("----------------------------")
    f.write("\n")
    f.write(f"Total Months: {totalvotes}")
    f.write("\n")
    f.write("---------------------------")
    f.write("\n")
    for candidatename,votes in candidates_votes.items():

       
        percentage_of_votes = round((votes / totalvotes) * 100, 3)

        f.write(f"{candidatename}: {percentage_of_votes}% ({candidates_votes[candidatename]})\n")
    f.write("\n")
    f.write("----------------------------")
    f.write("\n")
    f.write(f"Winner: {winner}")
    f.write("\n")
    f.write("----------------------------")
    
    



 