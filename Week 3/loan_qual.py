"""
File Name: loan_qual.py
Creator: Ammon Jones
Purpose: Determine if a user can qualify for a loan.
"""
# Libraries needed to complete the task:

# Functions needed to complete the task:

# Constants needed to complete the task:

# Info needed from user to complete the task:
print('Please enter 1-10 to rate the following questions:')
large_loan = int(input('How large is the loan? '))
good_credit = int(input('How good is your credit history? '))
high_income = int(input('How high is your income? '))
large_down = int(input('How large is your down payment? '))
# Formulas needed to complete the task:

should_loan = True
if large_loan >= 5:
    if good_credit >= 7 and high_income >= 7:
        should_loan = True
    elif good_credit >= 7 or high_income >= 7:
        if large_down >= 5:
            should_loan = True
        else:
            should_loan = False
    else:
        should_loan = False
else:
    if good_credit < 4:
        should_loan = False
    elif high_income >= 7 or large_down >= 7:
        should_loan = True
    elif high_income >= 4 and large_down >= 4:
        should_loan = True
    else:
        should_loan = False

if should_loan:
    print('You qualify for the loan!')
else:
    print("You don't qualify for the loan!")
    print('You should learn how to manage your money better!')
    


