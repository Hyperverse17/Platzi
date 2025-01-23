
class LivingBeing:
    def __init__(self, type):
        self.type = type

class Person(LivingBeing):
    def __init__(self, type, name, age):
        super().__init__(type)
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, type, name, age, student_id):
        super().__init__(type, name, age)
        self.student_id = student_id

    def introduce(self):
        print(f"Hi, I'm a {self.type}. My name is {self.name}, I have {self.age} years old and my student ID is {self.student_id}")

print()
print("--- student ---")
student = Student("Human","Otelo", 21, "1707")
student.introduce() 


