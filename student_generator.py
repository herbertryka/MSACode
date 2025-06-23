from student import Student
def main():
        student_list:Student = []
        data_file = open("student.csv", "r")
        for line_of_data in data_file:
            student_info = line_of_data.split(",")
            if len(student_info) != 6:
                continue
            first_name = (student_info[0])
            last_name = (student_info[1])
            major = (student_info[2])
            try:
                credit_hours = int(student_info[3])
                gpa = float(student_info[4])
            except:
                 continue
            student_id = (student_info[5])
            
            #create student object
            the_student = Student(first_name, last_name, major, credit_hours, gpa, student_id)
            #append the student to student list
            student_list.append(the_student)
        
        data_file.close()


        #loop through student list and print student data
        for student in student_list:
             student.print_student_data()
main()          