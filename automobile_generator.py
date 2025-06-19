from Automobile import Automobile
#python will automatically recognize file
#from file import class
def main():
    #create instances of Automobile
    auto1 = Automobile("Honda", "Accord", "23456", 2.2, "Alice", 2017, "Blue")
    auto2 = Automobile("Ferrari", "F-50", "12345", 4.8, "Bob", 2022, "Black")
    #change auto2's year
    #both of these will not work without get and set methods because they were encapsulated
    #cant change year, no set method for year
    auto2.__year = 2000
    #change auto1's owner
    auto1.set_owner("Enzo")

    auto2.set_color("Red")

    #you can add these to a list
    #you also could just add auto1 and auto2 to the square brackets instead of using the append function
    auto_list = []
    auto_list.append(auto1)
    auto_list.append(auto2)
    
    #print each automobile's information
    for auto in auto_list:
        auto.print_data()

    print(f"Auto 1 is {auto1.get_age()} years old")

#Three principles of object oriented programming
#polymorphism
#inheritance
#encapsulation
    #makes properties private/protects/only makes properties that can be changed, be changed. helps protect personal info
main()