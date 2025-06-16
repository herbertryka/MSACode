#strings are lists of characters
#you can treat strings like lists
def main():
    my_name = "ryka"

    #capitalize
    print(my_name.capitalize())

    #make a string uppercase
    print(my_name.upper())

    #make a string lowercase
    last_name = "HERBERT"
    print(f"{my_name.lower()} {last_name.lower()}")

    print("\nUsing startswith() method")
    #determine if a string starts with a set of characters
    print(my_name.startswith("r") or my_name.startswith("R"))
    #lowercase vs uppercase - different values
    #validating the truth and whether its right, NOT validating whether its wrong. True otherwise wrong, not function
    if((not my_name.startswith("ry")) and (not my_name.startswith("Ry"))):
        print(f"You spelled {my_name} incorrectly")
    else:
        print(f"You spelled {my_name} correctly!\nYayyy")
    
    print(f"\nUsing endswith() method")
    print(f"{my_name} ends with 'ka': {my_name.endswith("ka")}")
    #if your string is wrapped in double quotes, you can use single quotes inside and vice versa - will work the same

    print("\nUsing the find() method")
    print(f"The 'y' is at index {my_name.find("y")} in my name")
    #if letter not found, index will equal -1
    print(f"The 'x' is at index {my_name.find("x")} in my name")
    search_letter = "yk"
    if(my_name.find(search_letter)) == -1:
        print(f"There is no {search_letter} in {my_name}")
    else:
        print(f"The {search_letter} is at index {my_name.find(search_letter)} in {my_name}")
    #substring is any part of the string (ryka - substring could be ry)
    #substring can be the whole string

    #loop through a string
    print("\nLoop through a string")
    for letter in my_name:
        print(letter)
    
    print(f"{my_name} has {len(my_name)} letters")

    #print the letters in a string along with the index position
    for letter_index in range(len(my_name)):
        print(f"Letter {letter_index+1}: {my_name[letter_index]}")
    
    print("\n\n")
    sentence = "I have a dog. My dog is cute. Do you want a dog?"
    start_index = 0
    search_word = "dog"
    number_of_dogs = 0
    #write code that counts the number of occurences of the word dog 
    #in the sentence. Expected output: 3
    #use a while loop
    while True:
       
        #start at the beginning of the string
        #search for the first occurence of the word(dog) starting from index 0
        dog_index = sentence.find(search_word, start_index)
        #if we find a dog add one to some variable of dogs we found
        if dog_index == -1:
            break
        else:
            number_of_dogs += 1
        #continue searching the string from the next index after the dog we found
        #update the start index to dog index plus one
        start_index = dog_index + 1
        #do this until we don't find any more dogs
    print(f"There are {number_of_dogs} {search_word}(s) in the sentence")
    
    #how to use the split() method
    print("\nUsing the split method")
    car_info = "Ferrari,f-50,2021,500000,4.8"
    car_data = car_info.split(",")
    print(car_data)
    #get individual pieces of data
    make = (car_data[0])
    model = (car_data[1])
    year = int(car_data[2])
    price = float(car_data[3])
    engine_size = float(car_data[4])

    print(f"{year} {make} {model}")
    print(f"Price : ${price} - engine : {engine_size}L")


main()
