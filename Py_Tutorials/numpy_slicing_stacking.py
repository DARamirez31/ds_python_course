import numpy as np
a= np.array([1, 2, 3, 4])
print(a[0:2])     # Slicing the first two elements, 0 inclusive, 2 exclusive
print(a[2:])     # Slicing from the third element to the end, 2 inclusive
print(a[-1])    # Slicing the last element, -1 refers to the last element

b = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(b[1,2])  # Accessing the element at row 1, column 2 (6)
print(b[0:2, 1:3])  # Slicing rows 0 to 1 and columns 1 to 2
#print first 2 elements on the last row
print(b[-1, 0:2])  # Slicing the first two elements of the last row
# Only print second and third column
print(b[:, 1:3])  # Slicing all rows, second column

# Customer ID, Name
c = np.array([[1, 'Alice'], [2, 'Bob'], [3, 'Charlie']])
# Customer ID, Purchase Amount, Purchase Date
d = np.array([[1, 100, '2023-01-01'], [2, 200, '2023-01-02'], [3, 300, '2023-01-03']])

# Create a new array by stacking c and d horizontally
e = np.hstack((c, d[:, 1:]))  # Exclude the first column of d to avoid duplication
print(e)  # Print the horizontally stacked array

# Add new customers id, name
new_customers = np.array([[4, 'David'], [5, 'Eve']])
f =np.vstack((new_customers, c))  # Stack new customers on top of existing data
print(f)  # Print the vertically stacked array with new customers

# Horizontally splitting the array e into two parts
e1, e2 = np.hsplit(e, 2)  # Split into two equal parts
print(e1)  # Print the first part of the split array
e3, e4 = np.hsplit(e, [3])  # Split f at the third column
print(e3)  # Print the first part of the split array f

#vertically splitting the array f into two parts
#f1, f2 = np.vsplit(f, 2)  # Split into two equal parts
#print(f1)  # Print the first part of the vertically split array
f3, f4 = np.vsplit(f, [3])  # Split f at the third row
print(f3)  # Print the first part of the vertically split array f

# Monthly sales data
monthly_sales = np.array([30, 45, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140])
result = monthly_sales < 55  # Boolean array indicating sales less than 55
print(result)  # Print sales less than 55

#indexing the monthly sales data
print(monthly_sales[result])  # Print the sales data where the condition is True

#maximum and minimum sales
print("Maximum sales:", monthly_sales.max())  # Print the maximum sales
print("Minimum sales:", monthly_sales.min())  # Print the minimum sales
# Find out the index of maximum and minimum sales, which month had the maximum and minimum sales
print("Index of maximum sales:", monthly_sales.argmax())  # Index of maximum sales
print("Index of minimum sales:", monthly_sales.argmin())  # Index of minimum sales
index = np.argmax(monthly_sales)
print ("maximum sales value:", monthly_sales[index])

# Transactions data Id, Name, Amount, Date
transactions = np.array([[1, 'Alice', 100, '2023-01-01'],
                          [2, 'Bob', 200, '2023-01-02'],
                          [3, 'Charlie', 300, '2023-01-03']])
#get the maximum transaction amount
max_transaction = transactions[transactions[:, 2].astype(int).argmax()]
print(max_transaction)
# Get the id 1 transaction
transaction_id_1 = transactions[transactions[:, 0].astype(int) == 1]
print(transaction_id_1)  # Print the transaction with id 1