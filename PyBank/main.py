# import library
import os
import csv
# define csv file path
bank_csv = os.path.join("/Users/shui/Desktop/BSC/UT-TOR-DATA-PT-01-2020-U-C-Master/03-Python/Instructions/python-challenge/PyBank/Resources/budget_data.csv")
# open and read the csv file line by line
with open(bank_csv,'r') as csvfile:
    csvheader = next(csvfile)
    csvreader = csv.reader(csvfile, delimiter = ",")

# create list variables
    date = []
    revenue = []
    monthly_change = []

# populate the date and revenue lists 
    for row in csvreader:
        date.append(row[0])
        revenue.append(float(row[1]))
    
        total_month = len(date)
        total_revenue = sum(revenue)

# calulate the average change in revenue and profit using the populated lists
    for i in range(1, total_month):
        monthly_change.append(revenue[i] - revenue[i-1])
        average_change = round(sum(monthly_change)/len(monthly_change),2)
        increase_profit = max(monthly_change)
        increase_profit_date = str(date[monthly_change.index(max(monthly_change))+1])
        decrease_profit = min(monthly_change)
        decrease_profit_date = str(date[monthly_change.index(min(monthly_change))+1])

# print the output on the terminal 
print(f"Financial Analysis")
print(f"---------------------------")
print(f"Total Months: {total_month}")
print(f"Total: ${total_revenue}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {increase_profit_date} (${increase_profit})")
print(f"Greatest Decrease in Profits: {decrease_profit_date} (${decrease_profit})")


# print the output as a text file
# alternatively using python main.py >> output.txt in the terminal 
txtfile_path = "/Users/shui/Desktop/BSC/UT-TOR-DATA-PT-01-2020-U-C-Master/03-Python/Instructions/python-challenge/PyBank/output.txt"
with open(txtfile_path,"w") as txt_file:
    txt_file.write(f"Financial Analysis\n")
    txt_file.write(f"---------------------------\n")
    txt_file.write(f"Total Months: {total_month}\n")
    txt_file.write(f"Total: ${total_revenue}\n")
    txt_file.write(f"Average Change: ${average_change}\n")
    txt_file.write(f"Greatest Increase in Profits: {increase_profit_date} (${increase_profit})\n")
    txt_file.write(f"Greatest Decrease in Profits: {decrease_profit_date} (${decrease_profit})\n")
    txt_file.close()