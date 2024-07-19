import csv
import os

#file path
file_path = os.path.join("Resources","budget_data.csv")

#variables
total_months = 0
net_total = 0
previous_profit = None
changes = []
greatest_increase = float('-inf')
greatest_decrease = float('inf')
greatest_increase_date = ""
greatest_decrease_date = ""

#read csv
with open(file_path, 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip header row

    for row in reader:
        date = row[0]
        profit_loss = int(row[1])
        
        #update total months and net total
        total_months += 1
        net_total += profit_loss
        
        #calculate changes
        if previous_profit is not None:
            change = profit_loss - previous_profit
            changes.append(change)
            
            #check for greatest increase/decrease
            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_date = date
            
            if change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_date = date
        
        previous_profit = profit_loss

#calculate average change
average_change = sum(changes) / len(changes) if changes else 0

#results
financial_analysis = (
f"Financial Analysis\n"
f"-------------------\n"
f'Total Months: {total_months}\n'
f'Net Total Profit/Losses: ${net_total}\n'
f'Average Change in Profit/Losses: ${average_change:.2f}\n'
f'Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n'
f'Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n')

#print financial analysis to terminal
print(financial_analysis)

#export to txt file
output_file = os.path.join("analysis", "financial_analysis.txt")
with open(output_file, 'w') as txt_file:
    txt_file.write(financial_analysis)

print(f"Financial analysis has been exported to '{output_file}'")


