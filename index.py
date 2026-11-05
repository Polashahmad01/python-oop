class StudentDatabase:
  student_list = []

  @classmethod
  def add_student(cls, student):
    cls.student_list.append(student)

class Student:
  def __init__(self, student_id, name, department, is_enrolled):
    self.__student_id = student_id
    self.__name = name
    self.__department = department
    self.__is_enrolled = is_enrolled
    StudentDatabase.add_student(self)

  def enroll_student(self, id):
    is_found = False

    for student in StudentDatabase.student_list:
      if student.__student_id == id:
        is_found = True

        if student.__is_enrolled:
          print(f"Student with ID: {id} is already enrolled.")
        else:
          student.__is_enrolled = True
          print(f"Student with ID: {id} successfully enrolled.")
        break

    if not is_found:
      print(f"No student found with ID: {id}")

  def drop_student(self, id):
    is_found = False

    for student in StudentDatabase.student_list:
      if student.__student_id == id:
        is_found = True

        if not student.__is_enrolled:
          print(f"Student with ID: {id} is not enrolled.")
        else:
          print(f"Student {id} has been dropped.")
        break

    if not is_found:
      print(f"No student found with ID: {id}")

  def view_student_info(self):
    for student in StudentDatabase.student_list:
      print(f"ID: {student.__student_id}, Name: {student.__name}, Department: {student.__department}, Enroll: {student.__is_enrolled}")


domagoj_gregor = Student("677cbb16-1597", "Domagoj Gregor", "CSE", False)
ahmose_annelie = Student("60f3b8f4-ad15", "Ahmose Annelie", "B-Tech", False)
ellen_farzana = Student("4fa18812-84e7", "Ellen Farzana", "Nursing", True)
nico_subhash = Student("f31e8893-ae87", "Nico Subhash", "Security", False)
virgilius_austyn = Student("0fdc58ae-a42f", "Virgilius Austyn", "AI", False)

  
while True:
  print("\n---- Student Management Menu ----")
  print("1. View All Students")
  print("2. Enroll Student")
  print("3. Drop Student")
  print("4. Exit")

  value = input("Enter your choice (1-4): ")

  if value == '1':
    domagoj_gregor.view_student_info()
  elif value == '2':
    student_id = input("Enter Student ID to enroll: ")
    domagoj_gregor.enroll_student(student_id)

  elif value == '3':
    student_id = input("Enter Student ID to drop: ")
    domagoj_gregor.drop_student(student_id)

  elif value == '4':
    print("Thank you for using Student Management System!")
    break

  else:
    print("Invalid choice! Please enter 1-4.")

