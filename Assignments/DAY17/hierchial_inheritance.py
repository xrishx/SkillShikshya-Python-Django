class Person:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_details(self):
        return f"Name: {self.name}, ID: {self.id}"

class Student(Person):
    def __init__(self, name, id, grade):
        super().__init__(name, id)
        self.grade = grade

    def get_details(self):
        return f"Name: {self.name}, ID: {self.id}, Grade: {self.grade}"

class Teacher(Person):
    def __init__(self, name, id, subject):
        super().__init__(name, id)
        self.subject = subject

    def get_details(self):
        return f"Name: {self.name}, ID: {self.id}, Subject: {self.subject}"

# Example usage
student = Student("Rishav", 6679, "A+")
teacher = Teacher("Dr. Smith", 1234, "Computer")
print(student.get_details())  
print(teacher.get_details())