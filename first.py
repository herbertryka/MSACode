# Print hello world to console
print("Hello World!")

#create a variable to store my name
first_name = "Ryka"

# Print "My name is Ryka"
print("My name is", first_name)

#create a variable to store my last name
last_name = "Herbert"

#write a statement to display "My full name is Ryka Herbert"
print("My full name is", first_name, last_name, sep="---")

#create variables to store your age, height, and weight, and assign them values
age = 15
height = 66
weight = 110.3

#print a sentence with age, weight, and height
print(f"My name is {first_name} {last_name}\nI am {age} years old and I weigh {weight}lbs")

#get and print the data type for age, weight, and height
print(type(age))
print(type(weight))
print(type(height))

#write 3 print statements using string interpolation (fstring) to print descriptive sentences for the data types
#Variable age in an int
print(f"Variable age is a {type(age)}")
#Variable weight is a float
print(f"Variable weight is a {type(weight)}")
#variable height is an int
print(f"Variable height is a {type(height)}")

number_1 = 5
number_2 = 7
total = number_1 + number_2
print(f"total: {total}")

number_1 = "5"
number_2 = "7"
total = number_1 + number_2
print(f"total: {total}")