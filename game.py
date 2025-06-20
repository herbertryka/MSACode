#import random number generator function module thing
import random

#get questions
"""
Function to create appropriate questions based on game level and number of questions specified
Input: game_level, number_of_questions
Output: Equation??
"""
def get_level():
    while True:
        #ask user for input
        try:
            game_level = int(input("What level would you like? (1-3): "))
        #validate input
            if game_level not in [1, 2, 3]:
                continue
            break
        except:
            print("ERROR: Please enter a valid number")
        
    return game_level

#get number of questions
"""
Function to get number of questions asked
Input: user
Output: number of questions 1-3
"""
def get_number_of_questions():
    while True:
        #ask user for input
        number_of_questions = int(input("\nHow many questions would you like (3-10): "))
        #use try except block to validate input
        try:
            if number_of_questions <3:
                print("ERROR: Enter valid input")
                continue
            elif number_of_questions > 10:
                print("ERROR: Enter valid input")
                continue
            break
        except: 
            print("ERROR: Enter valid input")
            continue
    return number_of_questions

def main():
    random_generator = random.Random()
    #call game level function
    game_level = get_level()

    #call number of questions function
    number_of_questions = get_number_of_questions()
    correct_answers = 0

    #create a for loop to ask number_of _questions questions
    for _ in range(number_of_questions):
        #generate x and y randomly
        #game level 1, ask appropriate question (int 0-9) using if statement
        if game_level == 1:
            x = random_generator.randint(0, 9)
            y = random_generator.randint(0, 9) 
        #game level 2, ask appropriate question (int 10-99) using if statement
        elif game_level == 2:
            x = random_generator.randint(10, 99)
            y = random_generator.randint(10, 99) 
        #game level 3, ask appropriate question (int 10-99) using if statement
        elif game_level == 3:
            x = random_generator.randint(100, 999)
            y = random_generator.randint(100, 999)
          

        #prompt the user for the answer up to three times
        max_tries = 0
        for _ in range(3):
            #make equation?
            user_answer = int(input(f"\n{x} + {y} = "))
            if user_answer != (x + y):
                print("\nIncorrect")
                max_tries += 1
                continue
            elif user_answer == (x + y):
                print("\nCorrect!")
                correct_answers += 1
                break
            else:
                break
        
        #determine if the user did not get the answer correct in 3 tries
        if max_tries == 3:
            print(f"{x} + {y} = {x + y}")
    print(f"\nYou got {correct_answers / number_of_questions * 100:.2f}% right")
main()