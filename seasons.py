#function: get season name from month number function
#input: month number
#ouput: season name
def get_season_name(season):
    if ((season == 12)) or ((season == 1)) or ((season == 2)):
        return "winter"
    elif ((season <= 5)) and ((season > 2)):
        return "spring"
        
    elif ((season <= 8)) and ((season > 3)):
        return "summer"
        
    elif ((season <= 11)) and ((season > 8)):
        return "fall"

#function: get month number from user input
#input: user input
#output: (int) of month
def get_month_number():
    #validate numer is 1 -12
    #reprompt user if input not valid
    while True:
        try:
            season = int(input("Enter the month in number format: "))
            if season <=0:
                print("ERROR: Please enter a valid number")
                continue
            elif ((season >=13)):
                print("ERROR: Please enter a valid number")
                continue
            else:
                break
        except:
            print("ERROR: Please enter a number")
            continue
    return season
    
def main():
    while True:
         #call the get_month_number function and get the month number from the user
        month_number = get_month_number()
        #call the get_season_name function to get the name of the season
        season_name = get_season_name(month_number)
         #print the output
        print(f"it is {season_name}")
        #ask the user of they want to run the program again
        #if y or Y, rerun the program, otherwise end the program
        do_again = input("Would you like to run the program again? press y to continue: ")
        if do_again == "Y" or do_again == "y":
            continue
        else:
            break
main()
