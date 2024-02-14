from student import Student
from teacher import Teacher

student = Student("John", 15, 10)
teacher = Teacher("Ms. Smith", 35, "Math")

student.display_info()
student.study()

teacher.display_info()
teacher.teach()