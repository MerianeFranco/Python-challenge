import os
import csv

print("Financial Analysis")
print("------------------")

budgetdata_csv = os.path.join('Resources', 'budget_data.csv')

with open(budgetdata_csv) as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Inform that data has header
    header = next(csvreader)

    # Variables
    Total = 0   #total profit/losses
    TotalA =0   #total of the difference between monthly result for average
    Months =[]  # list to hold the month column (first column)
    MonthlyResult = []  # list to hold the monthly result column (second column)
    MonthlyResultDiff =[]   # list to hold the difference between monthly result for average)
    AverageChange = 0   #number for average change
    Greatest=0  #number for greatest increase in profit
    GreatestMonth = " "     #month for greatest increase in profit
    Lowest=0    #number for greatest decrease in profit
    LowestMonth = " "   #month for greatest decrease in profit

    # Loop through the data
    for row in csvreader:
            #lenght of the data is the number of months
            Months.append(row[0])
            MonthlyResult.append (int(row[1]))
            #add the totat of each row index 1
            Total += int (row[1])
            # count the months
            
    print (f"Total Months: " + str(len(Months)))
    print (f"Total: $" + str(Total))
    
    MonthlyResultDiff = [(MonthlyResult[n]) - (MonthlyResult[n-1]) for n in range (1,len(MonthlyResult))]
    
    for n in range (0,len(MonthlyResultDiff)):
        TotalA = (MonthlyResultDiff[n]) + TotalA
    
    AverageChange = round(TotalA/len(MonthlyResultDiff),2)

    print (f"Average  Change: $" + str(AverageChange))

    for n in range (0,len(MonthlyResultDiff)):
        if (MonthlyResultDiff[n]) > Greatest:
            Greatest=(MonthlyResultDiff[n])
            GreatestMonth = (Months[n+1])

    print (f"Greatest Increase in profits: {GreatestMonth} (${str(Greatest)})")
    
    for n in range (0,len(MonthlyResultDiff)):
        if (MonthlyResultDiff[n]) < Lowest:
            Lowest=(MonthlyResultDiff[n])
            LowestMonth = (Months[n+1])
        
    print (f"Greatest Decrease in profits: {LowestMonth} (${str(Lowest)})")
 


 # Specify the file to write to
output_path = os.path.join("Analysis", "Financial_Analysis.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile)#,delimiter =',')

    # Write the results on the teh Financial Analysis file located at Analysis folder

    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['Results'])
    csvwriter.writerow(['Total Months:' + str(len(Months))])
    csvwriter.writerow(['Total: $' + str(Total)])
    csvwriter.writerow(['Average  Change: $' + str(AverageChange)])
    csvwriter.writerow(['Greatest Increase in profits: '+ str(GreatestMonth)+ ' $' + str(Greatest)])
    csvwriter.writerow(['Greatest Decrease in profits: '+ str(LowestMonth)+ ' $' + str(Lowest)])
