# CTI-110
# P4HW1 - Score List
# Marc-Anthony Jones 
# 11-3-22
# The user will input grades, which will be added to a list and be processed with calculations, and the multiple print statements will display output.



# How many scored entered


ScoresEntered = int(input("How many scores do you want to enter? "))

MyList = []



# Loop

for i in range (ScoresEntered):
    Grade = int(input("Enter score #:"  +str(i)))



    if Grade >= 0 and Grade <= 100:

        MyList.append(Grade)



    else:
        print("INVALID Score entered !!!!")
        print("Score should be between 0 and 100")

        while Grade < 0 or Grade > 100:
            Grade = int(input("Enter score again #:"  +str(i)))






        
        

    


#ModifiedList = # print every score except the lowest value

ModifiedList = (Grade)





# Results

    
LowestScore = min(MyList)

ScoreAverage = sum(MyList) /len(MyList)

if ScoreAverage <= 59:
    LetterGrade = ("F")
elif ScoreAverage < 70 or Grade >= 60:
    LetterGrade =("D")
elif ScoreAverage < 80 or Grade>=70:
    LetterGrade = ("C")
elif ScoreAverage < 90 or Grade >=80:
    LetterGrade = ("B")
elif ScoreAverage< 101 or Grade >=90:
    LetterGrade = ("A")



print("----------------Results-----------")
    
print(f'Lowest Score:    {LowestScore:.2f}')
print(f'Modified List:   {ModifiedList:.2f}')
print(f'Score Average:   {ScoreAverage:.2f}')
print(f'Grade:         {LetterGrade:}')
print("---------------------------")





