# CTI-110
# P4HW2 - Salary Calculator
# Marc-Anthony Jones
# 11-15-22
# Tells me one or multiple Employee Salary Totals


total = 0

overtimeRate = 0.5 

# List
overtimePay = []

RegularPay = []

grossPay = []

while True:
    
    EmployeeName = input("\nEnter employee's name or \"None\" to terminate: ")
    
    if EmployeeName == "None":
        
        break
    
    hours = int(input("How many hours did {} worked? ".format(EmployeeName)))
    
    payRate = float(input("What is {}\'s pay rate? ".format(EmployeeName)))
    
    x = 0
    
    OP = RP = GP = 0.0
    
    if hours > 40:
        
        x = hours - 40
        
        OP = x * overtimeRate
        
        RP = 40 * payRate
        
        GP = OP + RP
        
    else:
        OP = 0.0
        
        RP = hours * payRate
        
        GP = RP
        
    overtimePay.append(float(OP))
    
    RegularPay.append(float(RP))
    
    grossPay.append(float(GP))
    
    total = total + 1

    # Print Statement
    
    print("Employee Name: ", EmployeeName)
    
    print(f'Hours Worked    Pay Rate      Overtime      Overtime Pay       Regular Pay            Gross Pay')
    
    print("---------------------------------------------------------------------------------------------------")
    
    print(f'{hours:.2f}           {payRate:.2f}        {x:.2f}           {OP:.2f}              {RP:.2f}                     {GP:.2f}') 


# Printing Total

print("Total number of employees entered: ",total)

print("Total amount payed for overtime: ", sum(overtimePay))

print("Total amount payed for regular hours: ", sum(RegularPay))

print("Total amount payed in gross: ", sum(grossPay))
