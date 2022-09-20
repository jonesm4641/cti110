# Travel Expense Code
# 9-20-22
# CTI-110 P1HW2 - Travel Expense
# Marc-Anthony Jones


print("This program calculates and displays travel expenses")

## User Enters Budget.

Budget = int(input('Enter Budget:\n'))


## User Enters Travel Destination

Location = input('Enter your travel destination:')


## How much Gas Spent ?

GasExpense = int(input('How much do you think you will spend on gas?:'))


## Acommadation / Hotel Cost

HotelCost = int(input('Approximately, how much will you need for accomdations / hotels?:'))


## How much do you need for food?

FoodCost = int(input('Last, how much do you need for food?:'))

## Receipt


print("----------Travel Expenses""----------")

print("Location:",Location)
print("Initial Budget:",Budget)
print("Fuel:",GasExpense)
print("Accomdation:",HotelCost)
print("Food:",FoodCost)

## Remaining Balance equation us as follows >>> Remaining_Balance = Budget - GasExpense - HotelCost - FoodCost

Remaining_Balance = Budget - GasExpense - HotelCost - FoodCost

print("Remaining Balance:", Budget - GasExpense - HotelCost - FoodCost)
