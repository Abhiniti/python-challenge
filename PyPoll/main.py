#PyPoll

#Read the csv file; import correct modules
import os
import csv
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
    #Loop through rows in csv file
    for row in electiondataCSV:
        #Check if candidate name is not already in list
        if row[2] not in candidateNames:
            #If not, add it to the list
            candidateNames.append(row[2])
            #Since votes will have same length as candidate list, add a generic value to votes list
            candidateVotes.append(0)

    #Point back to the top of the csv file
    csvfile.seek(0)
    #Skip the header
    next(electiondataCSV)

    #Loop through rows in csv file
    for row in electiondataCSV:
        if row[2] in candidateNames:
            #Check index of candidateNames
            indexNo = candidateNames.index(row[2])
            #Increment same index in candidateVotes
            candidateVotes[indexNo] += 1

    #Calculate percentageWon of each candidate
    percentWon = []
    #Sum up total number of votes
    totalVotes = sum(candidateVotes)
    #Loop through candidateVotes list
    for number in candidateVotes:
        #Calculate percent won for each candidate
        percent = round(number/totalVotes*100)
        #Add percentWon for each candidate into another list
        percentWon.append(percent)

    #Determine winner
    maxVotes = max(candidateVotes)
    #Detemine index for winner
    maxIndex = candidateVotes.index(maxVotes)
    #Get name for winneerr
    winner = candidateNames[maxIndex]

    print("Election Results")
    print("-------------------------")
    print("Total Votes: " + str(totalVotes))
    print("-------------------------")
    #Format final results
    finalArray = []
    #Loop through list to get index
    for name in candidateNames:
        indexNo = candidateNames.index(name)
        #Format: Name, percent won, votes
        finalArray.append(str(candidateNames[indexNo]) + ": " + str(percentWon[indexNo]) + "% (" + str(candidateVotes[indexNo]) + ")")
    #Present results in separate lines
    print(*finalArray, sep='\n')
    print("-------------------------")
    print("Winner: " + str(winner))
    print("-------------------------")
