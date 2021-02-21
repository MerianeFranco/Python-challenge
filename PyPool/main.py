
import os
import csv

print("Election Results")
print("-----------------------")

electiondata_csv = os.path.join('Resources', 'election_data.csv')

with open(electiondata_csv) as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Inform that data has header
    header = next(csvreader)

    # Variables
    total = 0   #total number of votes (rows on the file)
    candidates = [] #list of candidates (names on column 3 row[2])
    winner = " " #winner of election
    names = []
    maxvotes = 0 #store the higher number of votes
    
    # Loop through the data
    
    for row in csvreader:
        # Count the number of rows
        total = total + 1
        candidates.append(row[2])

        if row[2] not in names:
            names.append(row[2])
    
    print(f'Total votes: '+ str(total))
    print("-----------------------")
    
 # Specify the file to write to
output_path = os.path.join("Analysis", "Election_Results.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile)  

    # Write the results on the Election Results file located at Analysis folder
    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['-----------------------'])

    for n in range (0, len(names)):    
        
        results = f'{names[n]}: {float((candidates.count(names[n])*100/total)):.3f}% ({candidates.count(names[n])})'
        print(results)
        csvwriter.writerow([results])    
    
        x= candidates.count(names[n])
        if x > maxvotes:
            maxvotes = x
            winner= names[n]
    print("Winner: " + winner)

    csvwriter.writerow([winner])


    print("-----------------------")


