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

    print("Financial Analysis")
    print("----------------------------")
    #Count the total number of months in the data set
    noMonths = sum(1 for row in budgetdataCSV)
    print("Total Months: " + str(noMonths))

    #Point back to the top of the csv file
    csvfile.seek(0)
    #Skip the header
    next(budgetdataCSV)

    #Sum up the Revenues; make sure to convert to int
    #Initialize total variable
    totalRev = 0
    #Initialize list containing monthly revenue
    monthlyRevs = []
    #For loop through all rows
    for row in budgetdataCSV:
        totalRev += int(row[1])
        monthlyRevs.append(row[1])
    print("Total Revenue: $" + str(totalRev))

    #Point back to the top of the csv file
    csvfile.seek(0)
    #Skip the header
    next(budgetdataCSV)

    #Average change between monthly revenue
    #Initialize list containing monthly revenue change
    monthlyRevChange = []
    #For loop through rows
    previous = None
    for row in budgetdataCSV:
        current = int(row[1])
        #Next row - current row change between months
        monthlyRevChange.append(0 if previous == None else current - previous)
        previous = current
        
    
    #Average change in monthly revenue change list
    def averageChange(monthlyRevChange):
        avgChange = sum(monthlyRevChange)/len(monthlyRevChange)
        return round(avgChange,2)
    roundChange = averageChange(monthlyRevChange)
    print("Average change: $" + str(roundChange))

    #Point back to the top of the csv file
    csvfile.seek(0)
    #Skip the header
    next(budgetdataCSV)

    #Determine greatest number in change list
    highest = max(monthlyRevChange)
    highestMonth = ""
    #Find out index of greatest change
    highestIndex = monthlyRevChange.index(int(highest))
    #For loop comparing monthly rev list to row
    for row in budgetdataCSV:
        if (row[1] == monthlyRevs[highestIndex]):
            highestMonth = row[0]
        elif (row[1] != monthlyRevs[highestIndex]):
            pass
    print("Greatest Increase in Profits: " + str(highestMonth) + " ($" + str(highest) + ")")

    #Point back to the top of the csv file
    csvfile.seek(0)
    #Skip the header
    next(budgetdataCSV)

    #Determine smallest number in change list
    smallest = min(monthlyRevChange)
    smallestMonth = ""
    #Find out index of smallest change
    smallestIndex = monthlyRevChange.index(int(smallest))
    #For loop compairng monthly rev list to row
    for row in budgetdataCSV:
        if(row[1] == monthlyRevs[smallestIndex]):
            smallestMonth = row[0]
        elif (row[1] != monthlyRevs[smallestIndex]):
            pass
    print("Greatest Decrease in Profits: " + str(smallestMonth) + " ($" + str(smallest) + ")")