import csv
import os

file1=os.path.join("Resources","budget_data.csv")

budget_data=[]

with open(file1) as csvfile:
    reader=csv.DictReader(csvfile)

    for row in reader:
        budget_data.append({"month": row["Date"], "amount": int(row["Profit/Losses"]),"change": 0})

total_months=len(budget_data)

prev_amount=budget_data[0]["amount"]
for i in range(total_months):
    budget_data[i]["change"]=budget_data[i]["amount"] - prev_amount
    prev_amount=budget_data[i]["amount"]

total_amount=sum(row["amount"] for row in budget_data)

total_row_change=sum(row["change"] for row in budget_data)
average=round(total_row_change/(total_months-1),2)

great_increase=max(budget_data, key=lambda x:x["change"])

great_decrease=min(budget_data,key=lambda x:x["change"])

Final_Report=[("PyBank Analysis"),
(f'Total Months: {total_months}'),
(f'Total: {total_amount}'),
(f'Average Change: {average}'),
(f'Greatest Increase in Profits: {great_increase["month"]} ${great_increase["change"]}'),
(f'Greatest Decrease in Profits: {great_decrease["month"]} ${great_decrease["change"]}')]
print(Final_Report)


file2=os.path.join("Analysis","PyBank_analysis.txt")

with open(file2,"w") as textfile:
    print("PyBank Analysis",file=textfile)
    print("----------------------", file=textfile)
    print(f'Total Months: {total_months}',file=textfile)
    print(f'Total: {total_amount}',file=textfile)
    print(f'Average Change: {average}',file=textfile)
    print(f'Greatest Increase in Profits: {great_increase["month"]} ${great_increase["change"]}', file=textfile)
    print(f'Greatest Decrease in Profits: {great_decrease["month"]} ${great_decrease["change"]}', file=textfile)
