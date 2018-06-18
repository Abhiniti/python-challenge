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
    candidateVotes = []
    for row in electiondataCSV:
        if row[2] not in candidateNames:
            candidateNames.append(row[2])
            candidateVotes.append(0)

    #Point back to the top of the csv file
    csvfile.seek(0)
    #Skip the heade
    next(electiondataCSV)

    for row in electiondataCSV:
        if row[2] in candidateNames:
            #Check index of candidateNames
            indexNo = candidateNames.index(row[2])
            #Increment same index in candidateVotes
            candidateVotes[indexNo] += 1

    #Calculate percentageWon of each candidate
    percentWon = []
    totalVotes = sum(candidateVotes)
    for number in candidateVotes:
        percent = round(number/totalVotes*100)
        percentWon.append(percent)

    #Determine winner
    maxVotes = max(candidateVotes)
    maxIndex = candidateVotes.index(maxVotes)
    winner = candidateNames[maxIndex]

    print("Election Results")
    print("-------------------------")
    print("Total Votes: " + str(totalVotes))
    print("-------------------------")
    finalArray = []
    for name in candidateNames:
        indexNo = candidateNames.index(name)
        finalArray.append(str(candidateNames[indexNo]) + ": " + str(percentWon[indexNo]) + "% (" + str(candidateVotes[indexNo]) + ")")
    print(*finalArray, sep='\n')
    print("-------------------------")
    print("Winner: " + str(winner))
    print("-------------------------")
