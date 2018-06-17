#PyBank

#Read the csv file; import correct modules
import os
import csv
csvpath = os.path.join("..", "PyBank", "budget_data.csv")

#Read the csv file per line
with open(csvpath, 'r') as csvfile:
    budgetdataCSV = csv.reader(csvfile)
    #Skip the header
    next(budgetdataCSV)

    #Count the total number of months in the data set
    noMonths = sum(1 for row in budgetdataCSV)
    print("Total Months: " + str(noMonths))

    #Sum up the Revenues; make sure to convert to int
    #Initialize total variable
    totalRev = 0
    #Initialize list containing monthly revenue
    monthlyRevs = []
    #For loop through all rows
    for row in budgetdataCSV:
        totalRev += int(row[1])
        monthlyRevs.append(row[1])
    print("Total Revenue: " + str(totalRev))

    #Average change between monthly revenue
    #Initialize revChange variable
    revChange = 0
    #Initialize list containing monthly revenue change
    monthlyRevChange = []
    #For loop through list
    for monthAmt in monthlyRevs:
        #Next row - current row change between months
        revChange = (monthAmt + 1) - monthAmt
        monthlyRevChange.append(revChange)
    
    #Average change in monthly revenue change list
    avgChange = sum(monthlyRevChange)/len(monthlyRevChange)
    print("Average change: " + str(avgChange))

    #Determine greatest number in change list
    highest = max(monthlyRevChange)
    #Find out index of greatest change
    highestIndex = monthlyRevChange.index(highest)
    #For loop comparing monthly rev list to row
    for row in budgetdataCSV:
        if (row[1] == str(monthlyRevs.index(highestIndex - 1))):
            highestMonth = row[0]
    print("Greatest Increase in Profits: " + str(highestMonth) + "($" + str(highest) + ")")

    #Determine smallest number in change list
    smallest = min(monthlyRevChange)
    #Find out index of smallest change
    smallestIndex = monthlyRevChange.index(smallest)
    #For loop compairng monthly rev list to orw
    for row in budgetdataCSV:
        if(row[1] == str(monthlyRevs.index(smallestIndex -1))):
            smallestMonth = row[0]
    print("Greatest Decrease in Profits: " + str(smallestMonth) + "($" + str(smallest) + ")")