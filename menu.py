"""
Function to load menu item and price into a dictionary
Input: (str)file_path
Output: (dictionary)menu
"""
def get_menu_dictionary(file_name:str) -> dict:
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
    
def main():
    menu_items = get_menu_dictionary("file.txt")

    total = 0
    while True:
        item_requested = input("Item: ")
        if item_requested.lower() == "end":
            break
        #get item price
        try:
            item_price = menu_items[item_requested]
        except:
            continue
        total = item_price + total
        print(f"Total: ${total:.2f}")

    
    
main()