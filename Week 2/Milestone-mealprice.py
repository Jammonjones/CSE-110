"""
Purpose: Compute price of meals
Key tasks needing to be accomplished: 
    -Get price of meal including child and adult variables as well as sales tax
    -Get payment amount
    -Compute amount of change to return
"""

#Get needed info from user.
print('Please enter the following: ')
child_price = float(input("Child meal price: "))
adult_price = float(input('Adult meal price: '))
num_children = int(input('Number of children: '))
num_adults = int(input('Number of adults: '))
taxrate = float(input('Sales tax percentage rate: '))

#Determine the meals subtotal (pretax)
child_total = child_price * num_children
adult_total = adult_price * num_adults
pretax_total = child_total + adult_total

#Tell the user the subtotal
print() #blank line...
print(f'Subtotal: ${pretax_total:.2f}')

#Calculate sales tax and display it to the user
total_tax = taxrate / 100 * pretax_total
print(f'Sales Tax: ${total_tax:.2f}')

# Calculate and display total charge for customer
total = total_tax + pretax_total
print(f'Total: ${total:.2f}')

#Ask the user if they would like to use a discount
print()
discount = input('Do you want to apply your discount code? Type y or n: ')
if discount == 'y':
    total = total * .9
    print(f'Your new total is: ${total:.2f}')
else:
    print("Okay but don't forget to use it next time!")

# Get payment amount from customer and dsiplay the change that they will get back
print()
payment_amount = float(input('What is the payment amount? '))
change = payment_amount - total
print(f'Change: ${change:.2f}')


