#args*

def sum_all(*args):
    """
    This function takes a variable number of arguments and returns their sum.
    :param args: Variable number of arguments
    :return: Sum of all arguments
    """
    total = 0
    for num in args:
        total += num
    return total

total= sum_all(1, 2, 3, 4, 5)
print(f"The total sum is: {total}")

def company_info(**kwargs):
    if 'ticker' in kwargs:
        print(f"Ticker: {kwargs['ticker']}")

    if 'ceo' in kwargs:
        print(f"CEO: {kwargs['ceo']}")
    if 'revenue' in kwargs:
        print(f"Revenue: {kwargs['revenue']}")

company_info(ticker='AAPL', ceo='Tim Cook', revenue="200 billion")

def find_square(a):
    return a*a

x = lambda a: a*a
print(x(2))

b = find_square(2)
print(b) 
