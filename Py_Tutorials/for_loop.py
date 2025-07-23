expenses=[100, 200, 300, 400, 500]
total_expenses = 0
for i in expenses:
    total_expenses = total_expenses + i
print(total_expenses)

for i in range(len(expenses)):
    expense = expenses[i]
    print(f"Expense {i + 1}: {expense}")
    total_expenses = total_expenses + expense
    print(f"Total Expenses: {total_expenses}")

# Using enumerate to get index and value
for i, expense in enumerate(expenses):
    print(f"Expense {i + 1}: {expense}")
    total_expenses += expense
    print(f"Total Expenses: {total_expenses}")

#Break in for loop
monthly_sales = [1000, 1500, 2000, 2500, 3000]
months = ["January", "February", "March", "April", "May"]
threshold = 2000
for sales_amount in monthly_sales:
    if sales_amount < threshold:
        print(f"Sales amount {sales_amount} doesn't exceed threshold {threshold}.")
    else:
        print(f"Sales amount {sales_amount} exceeds threshold {threshold}. Stopping the loop")
        break

#Using zip
for month, sales in zip(months, monthly_sales):
    print(f"Sales for {month}: {sales}")
    if sales < threshold:
        print(f"Sales for {month} is below the threshold of {threshold}.")
    else:
        print(f"Sales for {month} exceeds the threshold of {threshold}.")
        break

#using continue
for month, sales in zip(months, monthly_sales):
    if sales < threshold:
        print(f"Sales for {month} exceeds the threshold of {threshold}. Continuing to next month.")
        continue
    print(f"Sales for {month} is below the threshold of {threshold}.")
#Using while
n = 0
while n < 10:
    print(n)
    n += 1
#Nested for loop
products = ["Laptop", "Phone", "Tablet"]
regions = ["North", "South", "East"]
revenue = [200, 150, 100, 250, 300, 400, 200, 150, 100]
i=0
for product in products:
    for region in regions:
        rev = revenue[i]
        i+=1
        print(f"Sales of {product} in {region} region have a revenue of {rev}.")

#using else in for loop
for i in range(5):
    print(f"Iteration {i}")
else:
    print("Loop completed without interruption.")

