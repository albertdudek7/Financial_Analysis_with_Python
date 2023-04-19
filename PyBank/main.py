#file that will be used to run the main script for each analysis
#load csv libraries
import os
import csv

#file path to budget data

#csvpath = os.path.join("python-challenge-main","Pybank","Resources","budget_data.csv")

csvpath =r"C:\Users\Albert Dudek\Workspace\python-challenge-main\PyBank\Resources\budget_data.csv"




#define variables to store results

totalmonths = []
totalrevenue = 0
prev_profit_loss = 1088983
profit_loss_change = 0
changes_profit_loss = []
greatestprofit_increase = ["",0]
greatestprofit_decrease = ["",9999999999999999999999]

#set variable to contain current revenue and previous revenue
current_revenue = []
previous_revenue = 0
numberofmonths = 0
revenue_change = 0 
revenue_change_list = []
revenue_average = 0



#opening the data file:budget data and using reader

with open(csvpath) as csv_file:

    csvreader = csv.reader(csv_file, delimiter=',')

    header = next(csvreader)

    for row in csvreader:

        #calculate total number of months
        totalmonths.append(row[0])

        numberofmonths = len(totalmonths)

        #Calculate Total Revenue

        totalrevenue += int(row[1])


        #Calculate change in profit/losses since last month

        profit_loss_change = (int(row[1])) - prev_profit_loss
        prev_profit_loss = (int(row[1]))
        changes_profit_loss.append(profit_loss_change)


        #track greatest increase in profits/loss

        if(profit_loss_change > greatestprofit_increase[1]):
            greatestprofit_increase[0] = row[0]
            greatestprofit_increase[1] = profit_loss_change


        #track greatest decrease in profits/loss

        if(profit_loss_change < greatestprofit_decrease[1]):
            greatestprofit_decrease[0] = row[0]
            greatestprofit_decrease[1] = profit_loss_change


#Calculate the average change in Profit/Loss

    profit_loss_avg = sum(changes_profit_loss) / (len(changes_profit_loss)-1)

    

#print results

print("Financial Analysis")
print("---------------------------")
print(f"Total Months: {numberofmonths}")
print(f"Total: ${totalrevenue}")
print(f"Average Change: ${round(profit_loss_avg,2)}")
print(f"Greatest Increase in Profits: {greatestprofit_increase[0]} (${greatestprofit_increase[1]})")
print(f"Greatest Decrease in Profits: {greatestprofit_decrease[0]} (${greatestprofit_decrease[1]})")






