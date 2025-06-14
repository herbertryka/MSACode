def main():
    #the need for dictionaries
    scores = [55, 75, 87, 82, 91]
    student = ["Alice", "Bob", "Jerry", "Jane", "Bill"]
    
    #print the student name and score together
    for index in range(len(scores)):
        print(f"{student[index]}: {scores[index]}")

    #create a dictionary of names and scores
    student_scores = {
        "Alice": 55,
        "Bob": 75,
        "Jerry": 87,
        "Jane": 82,
        "Bill": 91,
    }

    #print Bob and Alice's scores
    print(student_scores["Bob"])
    print(student_scores["Alice"])

    #print all student's data in the student scores dictionary
    print("\nGet all student data")
    for student in student_scores: 
        print(f"{student}: {student_scores[student]}")

    #create a car dictionary to store make, model, year, value, engine size
    car_1 = {"make": "Ferrari", "model":"f-50", "year":2021, "value": 500000, "engine": 4.8}

    #get all my car information
    print("\nGet the car information")

    for key, value in car_1.items():
        print(f"{key}: {value}")

    car_2 = {"make": "Honda", "model": "Accord", "Year": 2015, "Value": 15000}

    #create a list of dictionaries
    dictionary_list = [car_1, car_2]

    print("\nDisplay all car's information")
    for car in dictionary_list:
        print("\nCar Information")
        for feature, value in car.items():
            print(f"{feature}: {value}")
    #if data that youre storing comes in pairs, use dictionary. place list in dictionary, puts all key - value pairs in order/displayed
    #create a dictionary of dictionaries
    car_dictionary = {"Ferrari": car_1,"Honda":car_2}
    #write a for loop to display the car information
    print("\nGet car info from dictionaries")
    for car_type in car_dictionary:
        print(car_type)
        for feature, value in car.items():
            print(f"{feature}: {value}")
#loop over to get key - value pairs




main()