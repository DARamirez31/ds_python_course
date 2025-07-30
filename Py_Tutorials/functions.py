expenses_deisy = [100, 200, 300, 400, 500]
expenses_victor = [150, 250, 350, 450, 550]

def calculate_total_expenses(expenses):
    '''
     
    :param expenses:
    :return:
    '''
    """Calculate the total expenses from a list of expenses."""
    total = 0
    for expense in expenses:
        total += expense
    return total

total_expenses_deisy = calculate_total_expenses(expenses_deisy)
total_expenses_victor = calculate_total_expenses(expenses_victor)
print(f"Total expenses for Deisy: {total_expenses_deisy}")
print(f"Total expenses for Victor: {total_expenses_victor}")
