#T20 - TASK 1 - STUDENT REGISTER

# Prompts user to enter the number of students to register
number_of_reg_students = int(input("How many students will be registering for the exam venue?\n"))

# Repeatedly prompts user to enter a student ID and appends the entry to "regform.txt" along with a dotted signature line below
i = 0
while i < number_of_reg_students:
    # Student ID entry prompt
    student_ID_no = input("Please enter your student ID number:\n")
    # With-as block used to write to file
    with open("regform.txt", "a") as regform:
        regform.write(f"{student_ID_no}:\n________________\n\n")
    i += 1 # Increment to next student
