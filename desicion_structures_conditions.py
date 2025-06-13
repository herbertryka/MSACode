#this file demonstrates decision structures and conditions 
def main():
    a = 7
    b = 4

    #exploring conditions
    print(f"a is greater than b: {a > b}")
    print(f"B is greater than A: {b > a}")
    print(f"A is equal to B: {a == b}")
    #comparision operators:
    #less than: <, greater than >, less than or equal to <=, greater than or equal to >=
    #equal to: == 
    #one equal sign is an assignment statement, two equal signs is a comparison operator

    #create a decision structure to determine if a and b are equal
    if a > b:
        print(f"{a} is greater than {b}")
    elif b > a:
        print(f"{b} is greater than {a}")
    else:
        print(f"{a} is equal to {b}")

    #create a decision structure to print a letter grade based
    #on a test score
    #A: 100-90, B: 89-80, C: 79-70, D: 69-60, F: less than 60
    print("Grade Decision: 1")
    test_score = (float(input("Enter your test score in number format: ")))
    #           A                       B
    if ((test_score > 100)) or ((test_score < 0)):
        print(f"ERROR: Please enter a valid test score")
   
    elif ((test_score <= 100) and (test_score >= 90)):
            print(f"{test_score} --> A")
    elif ((test_score <= 89) and (test_score >= 80)):
            print(f"{test_score} --> B")
    elif ((test_score <= 79) and (test_score >= 70)):
            print(f"{test_score} --> C")
    elif ((test_score <= 69) and (test_score >= 60)):
            print(f"{test_score} --> D")
    elif (test_score >= 0):
        print(f"{test_score} --> F")
    else:
        print(f"ERROR: Please enter a valid test score")
  



     #create a decision structure to determine the season: winter, spring, summer, fall
     #ask the user to enter the number of the month and based on the number, determine the season
     #winter: 12, 1, 2; Spring: 3, 4 ,5; Summer: 6, 7, 8; Fall: 9, 10, 11
     #Output / Print the season: It is season
    while True:
        try:
            season = int(input("Enter the month in number format: "))
            if ((season == 12)) or ((season == 1)) or ((season == 2)):
                print("It is winter.")
                break
            elif ((season <= 5)) and ((season > 2)):
                print("It is spring")
                break
            elif ((season <= 8)) and ((season > 3)):
                print("It is summer")
                break
            elif ((season <= 11)) and ((season > 8)):
                print("It is fall")
                break
            else:
             print("Enter a valid month")
             continue
        except:
            print("Please enter a number")
            continue
        
main()