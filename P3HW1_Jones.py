# CTI-110
# P3HW1 - Debugging
# Marc-Anthony Jones 
# 10-18-22
# Debugging th code to become operatinal.

# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules



mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5,mod_6]
# TO DO: determine lowest, highest , sum and average for grades

low = min(grades)
high = max(grades)
Sum_of_Grades = sum(grades)
avg = sum(grades) / len(grades)

print("----------Results""----------")

print(f'Lowest Grade:    {low:.2f}')
print(f'Highest Grade:   {high:.2f}')
print(f'Sum of Grades:   {Sum_of_Grades:.2f}')
print(f'Average:         {avg:.2f}')
print("---------------------------")

# determine letter grade for average


if avg >= 90 and avg <= 100:
    print('Your grade is: A')
    
elif avg >= 80 and avg <= 89:
    print('Your grade is: B')
        
elif avg >= 70 and avg <= 79:
    print('Your grade is: c')

elif avg >= 60 and avg <= 69:
    print('Your grade is: d')
        
elif avg <=59:
    print('Your grade is: F') # TO DO: finish this





