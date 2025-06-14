
#prompt user to insert coin
#only excepts 1, 5, 10, 25

def main():
    #print vending machine and amount owed (50)
    #get user input using input function
    #validate user inputs (input can only be 1, 5, 10, 25)
    #assign variable and set variable equal to those amounts in while loop
    #any other answer will be ignored (else function?)
    #use variable math to get amount left from user (50 - user input = amount)
    #make variable only positive? 
    #give user change if answer was orginally negative, display amount owed if orginal answer was postive
    amount_owed = 50
    print(f"Vending Machine\n--------")
    while True:
        print(f"Amount Owed: {amount_owed}")
        try:
            change_inserted = int(input("Enter coin here: "))
           
            if change_inserted not in [1, 5, 10, 25]:
                continue
        except:
            print("Please enter a valid number")
            continue
        
        amount_owed = amount_owed - change_inserted
        if amount_owed == 0:
            print(f"Amount Owed: {amount_owed}")
            break
        if amount_owed < 0:
            print(f"Change back: {amount_owed * -1}. Please take your change :)")
            break

main()