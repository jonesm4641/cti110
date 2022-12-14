import random


def display_intro():
    title = "Welcome to Math Quiz"
    
    print(title)
    


def display_menu():
    menu_list = ["1. Adding Random Numbers", "2. Subtracting Random Numbers", "3. Exit"]
    print(menu_list[0])
    print(menu_list[1])
    print(menu_list[2])
    


def display_separator():
    print("-" * 24)


def get_user_input():
    user_input = int(input("Please choose one of the menu options: "))
    while user_input > 5 or user_input <= 0:
        print("Invalid menu option.")
        user_input = int(input("Please try again: "))
    else:
        return user_input


def get_user_solution(problem):
    print("Enter answer.")
    print(problem, end="")
    result = int(input(" = "))
    return result


def check_solution(user_solution, solution, count):

        
    if user_solution == solution:
        count = count + 1
        print("Congradulations !!!! your answer is correct...")
        return count
    elif user_solution > solution:
        user_solution = int(input("Try Again: "))
        print("Sorry, guess is too high")
        
        if user_solution == solution:
            print("Congradulations !!!! your answer is correct...")

    elif user_solution < solution:
        user_solution = int(input("Try Again: "))
        print("Sorry, guess is too high")
        if user_solution == solution:
            print("Congradulations !!!! your answer is correct...")

    else:
        while user_solution != solution:
            user_solution = int(input("Try Again: "))
    

            

         

def menu_option(index, count):
    number_one = random.randrange(1, 101)
    number_two = random.randrange(1, 101)
    if index == 1:
        problem = str(number_one) + " + " + str(number_two)
        solution = number_one + number_two
        user_solution = get_user_solution(problem)
        count = check_solution(user_solution, solution, count)
        return count
    elif index == 2:
        problem = str(number_one) + " - " + str(number_two)
        solution = number_one - number_two
        user_solution = get_user_solution(problem)
        count = check_solution(user_solution, solution, count)
        return count
   


def display_result(total, correct):
    if total > 0:
        result = correct / total
        count = round((result * 100), 2)
    if total == 0:
        count = 0
    print("Number of Guesses", total)
  


def main():
    display_intro()
    display_menu()
    display_separator()

    option = get_user_input()
    total = 0
    correct = 0
    while option != 3:
        total = total + 1
        correct = menu_option(option, correct)
        option = get_user_input()

   
    print("Thank you for playing...")
    print("Bye!!")
    display_separator()
    display_result(total, correct)

main()
