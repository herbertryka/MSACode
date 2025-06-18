"""
Function to load menu item and price into a dictionary
Input: (str)file_path
Output: (dictionary)menu
"""
def get_menu_dictionary(file_name:str)->dict:
    #open file.txt: create a file handler in read mode
    data_file = open("file.txt", "r")

    #create an empty dictionary to store item: price entries
    #lists enclose things in [], dictionaries in {}
    menu_items = {}
    #use a loop to read the contents of the file line by line
    for line_of_data in data_file:
        #split the data at the comma
        item_name_and_price = line_of_data.split(",")
        #get the menu item and price from the list 
        item_name = item_name_and_price[0]
        item_price = float(item_name_and_price[1])
        #create an entry in the dictionary for the item and price
        menu_items[item_name] = item_price
    return menu_items  

def display_cart(cart:dict, menu_items:dict)->None:
    print("Cart\n")
    #loop through the cart to print the output
    total = 0
    for item, quantity in cart.items():
        total = total + (quantity * menu_items[item])
        print(f"{quantity} {item} @{menu_items[item]:.2f}: {quantity * menu_items[item]:.2f}")
    print(f"\nTotal: {total}")

def main():
    total = 0
    menu_items = get_menu_dictionary("file.txt")
    #create a cart dictionary
    item_cart = {}

    while True:
        item_requested = input("\nItem: ")

        #determine if we need to end the program
        if item_requested.lower() == "end":
            break

        if item_requested not in menu_items():
            print(f"ERROR: {item_requested} is not on the menu")
            continue

        #prompt user for quantity
        try:
            quantity = int(input("Quantity: "))
        except:
            print("\nERROR: Enter number for quantity")
            continue
        
        #add item to cart. if item in cart already, add quantity 
        #if not in cart, add item and quantity to  cart 
        if item_requested not in item_cart:
            #create a new entry in the item cart dictionary
            item_cart[item_requested] = quantity
        else:
            #adds quantity to the value of the item's current quantity
            item_cart[item_requested] += quantity
        
        #display total by calling the display cart function
        display_cart(item_cart, menu_items)

        """
        2 Taco @ 3.00: 6.00
        3 Bowl @ 8.50: 25.50

        Total: 31.50
        """
main()
