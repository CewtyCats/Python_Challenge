#import library
import os
import csv

#join path
budget_data = os.path.join("Resources", "budget_data.csv")

# open csv
with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    # skip header row
    print(f"Header: {csv_header}")

    # find net amount of profit and loss
    P = []
    months = []

    # scan through each row of data
    for rows in csvreader:
        P.append(int(rows[1]))
        months.append(rows[0])

    # Change in revenue
    revenue_change = []

    for x in range(1, len(P)):
        revenue_change.append((int(P[x]) - int(P[x-1])))
    
    # Average revenue fluctuation
    revenue_average = sum(revenue_change) / len(revenue_change)
    
    # Total length of months
    from calendar import monthrange
    def monthdelta(d1, d2):
       delta = 0
       while True:
          mdays = monthrange(d1.year, d1.month)[1]
          if d1 <= d2:
             delta += 1
         else:
            break
         return delta


    # greatest increase in Profits
    greatest_increase = max(revenue_change)
    # greatest decrease in Profits
    greatest_decrease = min(revenue_change)


    # print the Results
    print("Financial Analysis")

    print("....................................................................................")

    print("Total Months: " + str(delta))

    print("Total: " + "$" + str(sum(P)))

    print("Average change: " + "$" + str(revenue_average))

    print("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(greatest_increase))

    print("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "$" + str(greatest_decrease))


    # output to a text file

    file = open("output.txt","w")

    file.write("Financial Analysis" + "\n")

    file.write("...................................................................................." + "\n")

    file.write("Total Months: " + str(Total_Months) + "\n")

    file.write("Total: " + "$" + str(sum(P)) + "\n")

    file.write("Average change: " + "$" + str(revenue_average) + "\n")

    file.write("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(greatest_increase) + "\n")

    file.write("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "$" + str(greatest_decrease) + "\n")

    file.close()