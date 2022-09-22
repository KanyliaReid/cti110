# This program asks for information about a trip the user is taking, then calculates and displays the travel expenses. 
# September 22, 2022
# CTI-110 P1HW2 - Travel Expense
# Kanylia Reid
#
#***********PSEUDOCODE***********
#
# Display "This program calculates and displays travel expenses!"
# Display "Enter Budget: "
# Input budget
# Display "Enter your travel destination: "
# Input travel destination
# Display "How much do you think you will spend on gas? "
# Input amount
# Display "Approximately, how much will you need for accomodation/hotel? "
# Input amount
# Display "Last, how much do you need for food? "
# Input amount
# Display "----------Travel Expenses----------"
# Display "Location:", destination
# Display "Initial Budget:", budget
# Display "Fuel: ", gasMon
# Display "Accomodation: ", accHot
# Display "Food: ", food
# Set expenses = gasMon + accHot + food
# Set remBal = budget - expenses
# Display "Remaming Balance:", remBal

print('This program calculates and displays travel expenses!')
budget = float(input('\nEnter Budget: '))
destination = input('Enter your travel destination: ')

gasMon = float(input('\nHow much do you think you will spend on gas? '))
accHot = float(input('Approximately, how much will you need for accomodation/hotel? '))
food = float(input('Last, how much do you need for food? '))

print('\n----------Travel Expenses----------')
print('\nLocation:', destination)
print('Initial Budget:', budget)

print('\nFuel:', gasMon)
print('Accomodation:', accHot)
print('Food:', food)

expenses = gasMon+accHot+food
remBal = budget-expenses

print('\nRemaining Balance:', remBal)



