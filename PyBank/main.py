# import pandas as pd

# filepath = "Resources/budget_data.csv"

# budget_df = pd.read_csv(filepath)

# print(budget_df.head())
# print("Total Months: " + str(len(budget_df)))
# print("Total: " + str(budget_df["Profit/Losses"].sum()))
# print("Average Change: " + str(budget_df["Profit/Losses"].mean()))
# print("Greatest Increase in Profits: " + str(budget_df["Profit/Losses"].max()))
# print("Greatest Decrease in Profits" + str(budget_df["Profit/Losses"].min()))

import os
import csv

#number of months
months = 0
#sum
sum = 0
#summing the change
sum_change = 0
#greatest change (increase), month and value

#greatest (decrease), month and value
bankpath = os.path.join(".", "Resources", "budget_data.csv")

with open(bankpath) as bankfile:
    csv_reader = csv.reader(bankfile, delimiter = ",")
    #read past first row

    csv_header = next(csv_reader)

    max_change_increase = float('-inf')
    max_change_decrease = float('inf')

    for row in csv_reader:
            
        months += 1

        curr_value = int(row[1])

        sum += curr_value

        if months == 1:
            prev_value = curr_value
        else:
            
            curr_change = curr_value - prev_value
            sum_change += curr_change
            #print("printing " + str(curr_value) + " - " + str(prev_value) + " = " + str(curr_change) + " between months " + str(months) + " and " + str(months-1) + "Total change = " + str(sum_change) )


            if(curr_change > max_change_increase):
                max_change_increase = curr_change
                max_change_increase_date = row[0]
            
            if(curr_change < max_change_decrease):
                max_change_decrease = curr_change
                max_change_decrease_date = row[0]



        prev_value = curr_value

print("Months: " + str(months))
print("Total: " + str(sum))
print("Average change: " + str(sum_change/(months-1)))
print("Greatest Increase in Profits: " + max_change_increase_date +  "($"+str(max_change_increase)+")")
print("Greatest Decrease in Profits: " + max_change_decrease_date + "($"+str(max_change_decrease)+")")

finalpath = os.path.join(".", "analysis", "financial_results.txt")

file_writer = open(finalpath, "w+")

file_writer.write("Months: " + str(months) + "\n")
file_writer.write("Total: " + str(sum) + "\n")
file_writer.write("Average change: " + str(sum_change/(months-1))+ "\n")
file_writer.write("Greatest Increase in Profits: " + max_change_increase_date +  "($"+str(max_change_increase)+")\n")
file_writer.write("Greatest Decrease in Profits: " + max_change_decrease_date + "($"+str(max_change_decrease)+")" + "\n")

file_writer.close()
