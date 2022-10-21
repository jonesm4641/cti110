# CTI-110
# P2HW2 - List
# Marc-Anthony Jones 
# 10-13-22
# The user will input grades, which will be added to a list and be processed with calculations, and the multiple print statements will display output.


# Define Variables
# Module Grade User Input


Module1 = float(input("Enter grade for Module 1: "))

Module2 = float(input("Enter grade for Module 2: "))

Module3 = float(input("Enter grade for Module 3: "))

Module4 = float(input("Enter grade for Module 4: "))

Module5 = float(input("Enter grade for Module 5: "))

Module6 = float(input("Enter grade for Module 6: "))

Grades = [Module1, Module2, Module3, Module4, Module5, Module6]

# Define New Variables for after Results

LowestGrade = min(Grades)

HighestGrade = max(Grades)

Sum_of_Grades = sum(Grades)

Average = sum(Grades) /len(Grades)



# Print Results


print("----------Results""----------")

print(f'Lowest Grade:    {LowestGrade:.2f}')
print(f'Highest Grade:   {HighestGrade:.2f}')
print(f'Sum of Grades:   {Sum_of_Grades:.2f}')
print(f'Average:         {Average:.2f}')
print("---------------------------")

