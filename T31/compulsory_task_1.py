#T31 - COMPULSORY TASK 1

class Course:
    name = "Fundamentals of Computer Science"
    contact_website = "www.hyperiondev.com"
    head_office_location = "Cape Town"

    def contact_details(self):
        print("Please contact us by visiting", self.contact_website)

    # 1. Method that prints the head office location "Cape Town"
    def print_head_office_location(self):
        print(f"The head office is located in {self.head_office_location}")

# 2. Creates a subclass of the Course class named OOPCourse
class OOPCourse(Course):
    # 3. Constructor that initialises "description", "trainer" and assigns values
    def __init__(self):
        self.description = "OOP Fundamentals"
        self.trainer = "Mr Anon A. Mouse"
        self.course_id = "#12345"
    # 4. Method that prints what the course is about and name of trainer by using description and trainer attributes
    def trainer_details(self):
        print(f"\nCourse Description:\t\t{self.description}")
        print(f"Course Trainer:\t\t\t{self.trainer}")
    # 5. Prints the ID number of the course: #12345
    def show_course_id(self):
        print(f"Course ID:\t\t\t\t{self.course_id}")

# 6. Creates an object of subclass called 'course_1' and calls contact_details(), trainer_details() and show_course_id()
course_1 = OOPCourse()
course_1.contact_details()
course_1.trainer_details()
course_1.show_course_id()
