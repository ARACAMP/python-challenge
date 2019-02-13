####
# PyBank 
####

# Import dependencies
import os
import csv

# specify path of text file and specify path of analysis file for output 
csvpybank = os.path.join('..', 'Resources', 'budget_data.csv')
output_path = os.path.join("analysis", "bank_analysis.txt")

# read text file
with open(csvpybank, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

months=0
total=0
average_change=0
Geatest_increase=0
Greates_decrease=0

profitandloss=[]
all_csv=[]
totals = []
with open(csvpybank, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        months+=1
        total+=int(row[1])
        profitandloss.append(int(row[1]))
        all_csv.append([row[0], int(row[1])])
        totals.append(total)

sum=0
changes=[]

length = len(profitandloss)-1
for i in range(0,length):
    changes.append(profitandloss[i+1]- profitandloss[i])
    sum = sum + changes[i]

ave_change=sum/(i+1) 
gre_inc=max(changes)
gre_inc_ind=changes.index(max(changes))+1
gre_dec=min(changes)
gre_dec_ind=changes.index(min(changes))+1

output = (
f"\nFinancial Analysis\n"
f"----------------------------------------\n"
f"Total months: {months}\n"
f"Total: ${total}\n"
f"Average  Change: ${round(average_change, 2)}\n"
f"Greatest Increase: {all_csv[gre_inc_ind][0]}, ${gre_inc}\n"
f"Greatest Decrease: {all_csv[gre_dec_ind][0]}, ${gre_dec}\n"
)

print(output)

with open(output_path, "w") as txt_file:
    txt_file.write(output)