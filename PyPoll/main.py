#PyPoll

#Read the csv file; import correct modules
import os
import csv
import collections
votes = collections.Counter()
csvpath = os.path.join("..", "PyPoll", "election_data.csv")

#Read the csv file per line
with open(csvpath, 'r') as csvfile:
    electiondataCSV = csv.reader(csvfile)
    #Skip the header
    next(electiondataCSV)

    #Count the total number of votes(rows) in the data set
    # noVotes = sum(1 for row in electiondataCSV)
    # print("Total Votes: " + str(noVotes))

    #Create a list with candidate names and votes
    candidateNames = []
    candidateVotes = ["1"]
    for row in electiondataCSV:
        if row[2] not in candidateNames:
            candidateNames.append(row[2])
    print(candidateNames)

    for row in electiondataCSV:
        if(row[2] == candidateNames[0]):
            candidateVotes = ["1"]
    print(candidateVotes)

    # #Loop through column to count up votes
    # #d = {k:None for k in l}
    # count = 0
    # for row in electiondataCSV:
    #     if (row[2] == "Correy"):
    #         count += 1
    # print(count)
    # print(candidateNames[0])