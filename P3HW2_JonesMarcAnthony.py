# CTI-110
# P3HW2 - Salary Calculator
# Marc-Anthony Jones 
# 10-18-22
# Calculating Salaries with multiple results in different fields.

# Define Variables

EmployeeName = input("Enter employee's name: ")

HoursWorked = float(input("Enter number of hours worked: "))

PayRate = float(input("Enter employee's pay rate: "))

RegHour_Pay = HoursWorked * PayRate

# Overtime Pay Equation


if HoursWorked > 40:
    OvertimePay = (RegHour_Pay / 2)
else:
    OvertimePay = 0


    
Overtime = HoursWorked > 40
    


# RegHour Pay

RegHour_Pay = (HoursWorked * PayRate)

# Gross Pay Equation

GrossPay = (HoursWorked * PayRate + OvertimePay)

print("---------------------------")

print("Employee Name:", EmployeeName)

print(f'')

print(f'Hours Worked    PayRate    Overtime    Overtime Pay    RegHour Pay    Grosspay') ## Print f'

print("---------------------------------------------------------------------------------")

print(f'{HoursWorked:.2f}           {PayRate:.2f}        {Overtime:.2f}        {OvertimePay:.2f}         {RegHour_Pay:.2f}           {GrossPay:.2f}')



