
#This program will calculate and display travel expenses
#9/27/2023
#CTI-110 P1HW2 - Travel Expense
#Hector Hughes

#Ask the user to enter the reqired information

budget= float(input("Please enter your budget: $ "))

travel_d= input("Please enter your desired destination: ")

gas= float(input("Please enter the amount you are planning to spend on gas: $ "))

sleep_place= float(input("Please enter the amount you are planning to spend on accomodation: $ "))

food= float(input("Please enter the ammount you are planning to spend on food: $ "))

#Add together the expenses

total_expense= (budget + gas + sleep_place + food)

#Subtract the total from the budget

left_over= (total_expense - budget)

#Print results

print('\n')

print("----------Travel Expenses----------")

print("Location:", travel_d)

print("Initial Budget: $", budget)

print('\n')

print("Fuel: $", gas)

print("Accomodation: $ ", sleep_place)

print("Food: $ ", food)

print('\n')

print("Remaining balance: $ ", left_over)
