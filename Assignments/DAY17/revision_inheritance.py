class Person:
    """Represents a general person with basic details."""
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_details(self):
        return f"Name: {self.name}, ID: {self.id}"

class Student(Person):
    """Represents a student, extending the Person class to include academic details."""
    def __init__(self, name, id, grade, courses):
        super().__init__(name, id)
        self.grade = grade
        self.courses = courses

    def get_details(self):
        return f"Name: {self.name}, ID: {self.id}, Grade: {self.grade}, Courses: {', '.join(self.courses)}"

# Example usage in a school system
student = Student("Rishav", 6679, "A+", ["Math", "Physics", "Computer Science"])
print(student.get_details())