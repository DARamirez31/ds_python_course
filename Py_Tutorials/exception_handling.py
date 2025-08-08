class insufficientfunds(Exception): #inheriting from Exception class
    pass


from sys import exception

# #x= input("Enter a number: ")
# #y= input("Enter another number: ")
# try:
#     d = int(x)/int(y)
# except:
#     print("Exception occurred")
#
# # Handling specific exception for division by zero
# try:
#     d = int(x)/int(y)
#     a = "abc" + 410
# # except ZeroDivisionError as e:
# #     print("Division by zero is not allowed:", e)
# #     d = 5
# # except TypeError as te:
# #     print("Test error occurred:", te)
# except Exception as ge:
#     print("Test error occurred:", ge)

#not file found error
file = None
try:
    file = open("test.txt", "r") # Open file in read mode
    content = file.read()
    print("File Content:", content)
except FileNotFoundError as fnf:
    print("File not found error:", fnf)
finally:
    if file:
        file.close()
    print("File Closed.")

balance = 0
def deposit(amount):
    global balance # Variable is available throughout the module
    if amount <= 0:
        raise ValueError("Deposit amount must be positive.") # Raising a ValueError for invalid deposit amount
    balance += amount

def withdraw(amount):
    global balance
    if amount > balance:
        raise insufficientfunds(f"Not enough funds. Current balance {balance}") # Raising a generic exception for insufficient funds
    balance -= amount

deposit(100)
#deposit(-10)
withdraw(500)

print(balance)
