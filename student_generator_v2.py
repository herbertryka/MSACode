from student import Student
import datetime

"""
Function to write an error message to a log file
Input: error message(str)
Output: none
"""
def write_to_error_log(message:str)->None:
    #open the log file: errorlog.txt
    #write error message to the file in the format
    #date: message -> 6/24/2025: Error in data file on line 5
    data_file = open("error_log.txt", "a")
    the_date = datetime.datetime.now()
    data_file.write(f"{the_date}: {message}")
    return

"""
Function to return a list of student objects
Input: none
Output: list of student objects
"""

def load_students()->list[Student]:
        student_list:Student = []
        data_file = open("student.csv", "r")
        line_number = 0
        for line_of_data in data_file:
            line_number += 1
            if line_number == 1:
                continue

            student_info = line_of_data.split(",")
            if len(student_info) != 6:
                    message = f"Error on line {line_number}: Incorrect data format\n"
                    write_to_error_log(message)
                    #write an error message to an error log
                    continue
            first_name = (student_info[0])
            last_name = (student_info[1])
            major = (student_info[2])
            try:
                credit_hours = int(student_info[3])
                gpa = float(student_info[4])
            except:
                message = f"Error on line {line_number}: Incorrect characters used\n"
                write_to_error_log(message)
                #write an error message to an error log
                continue
            student_id = (student_info[5])
                
            #create student object
            the_student = Student(first_name, last_name, major, credit_hours, gpa, student_id)
            #append the student to student list
            student_list.append(the_student)
        
        data_file.close()
        return student_list
"""
Function to convert student objects to student dictionaries
Input: list of student objects
Ouput: list of student dictionaries
"""
def student_to_dictionary(list_of_students: list[Student])->list[dict]:
    #create a list to store the dictionaries in
    student_dictionary_list = []

    #loop through the student list and write each student's data to a dictionary
    for student in list_of_students:
        #create an empty dictionary for each student
        student_dictionary = {}

        #set the keys and values for the dictionary
        student_dictionary['first_name'] = student.get_first_name()
        student_dictionary['last_name'] = student.get_last_name()
        student_dictionary['major'] = student.get_major()
        student_dictionary['gpa'] = student.get_gpa()
        student_dictionary['class'] = student.get_class_level()
        student_dictionary['id'] = student.get_id()
        #append the dictionary to the list of dictionaries
        student_dictionary_list.append(student_dictionary)
    #return the list of dictionaries
    return student_dictionary_list
"""
Function to get a list of student dictionaries
Input: None
Output: list of student dictionaries
"""
def get_student_dictionaries():
    #get a list of students
    student_list = load_students()

    #get a list of student dictionaries
    student_dictionaries = student_to_dictionary(student_list)

    for student_dict in student_dictionaries:
       print(student_dict)
    return student_dictionaries

get_student_dictionaries()      