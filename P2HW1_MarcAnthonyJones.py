# Travel Expense Code Module 4
# 10-06-22
# CTI-110 P2HW1 - Travel
# Marc-Anthony Jones

#The Input is user input for Location, Budget, and other expenses. Then it will be processed with the calculations I have defined, then print output based off the input.


print("This program calculates and displays travel expenses")

## User Enters Budget.

Budget = float(input('Enter Budget: \n'))


## User Enters Travel Destination

Location = input('Enter your travel destination: ')


## How much Gas Spent ?

GasExpense = float(input('How much do you think you will spend on gas?: '))


## Acommadation / Hotel Cost

HotelCost = float(input('Approximately, how much will you need for accomdations / hotels?: '))


## How much do you need for food?

FoodCost = float(input('Last, how much do you need for food?: '))

## Receipt


print("----------Travel Expenses""----------")

print(f' Location:           {Location} ')
print(f' Initial Budget:    ${Budget}')
print(f' Fuel:              ${GasExpense}')
print(f' Accomdation:       ${HotelCost}')
print(f' Food:              ${FoodCost}')

## Remaining Balance equation us as follows >>> Remaining_Balance = Budget - GasExpense - HotelCost - FoodCost

Remaining_Balance = Budget - GasExpense - HotelCost - FoodCost

print("-----------------------------------")
print(f' Remaining Balance: ${Remaining_Balance}')
