#Student GradeBook
print("Student GradeBook")
print("==================")
class GradeBook:
    def __init__(self):
        self.grades = {}

    def add_student(self, name):
        if name not in self.grades:
            self.grades[name] = []

    def add_grade(self, name, grade):
        if name in self.grades:
            self.grades[name].append(grade)
        else: 
            print(f"Student {name} not found. Please add the student first.")

    def get_average(self, name):
        if name in self.grades and self.grades[name]:
            return sum(self.grades[name]) / len(self.grades[name])
        return 0.0

    def get_all_averages(self):
        averages = {}
        for name in self.grades:
            averages[name] = self.get_average(name)
        return averages
    def display_grades(self):
        if not self.grades:
            print("No students in the grade book.")
            return
        for name, grades in self.grades.items():
            print(f"{name}: {grades}")

def start():
    gradebook = GradeBook()
    while True:
        print("\nOptions:")
        print("1. Add Student")
        print("2. Add Grade")
        print("3. View Averages")
        print("4. View All Grades")
        print("5. Exit")
        choice = input("Select an option (1-5): ")

        if choice == '1':
            name = input("Enter student name: ")
            if name in gradebook.grades:
                print(f"Student {name} already exists.")
            else:
                gradebook.add_student(name)
                print(f"Student {name} added.")

        elif choice == '2':
            name = input("Enter student name: ")
            if name not in gradebook.grades:
                print("Student not found. Please add the student first.")
                continue
        
            try:
                grade = float(input("Enter a grade: "))
                if grade < 0 or grade > 100:
                    raise ValueError("Grade has to be between 0 and 100")
                gradebook.add_grade(name, grade)
                print(f'{grade} has been added for {name}')
            except ValueError as e:
                print(f'Error: {e}')
                          

        elif choice == '3':
            name = input("Enter student name: ")
            if name not in gradebook.grades:
                print("Error")
            else:
                average = gradebook.get_average(name)
                print(f"{name}'s average grade: {average:.2f}")

        elif choice == '4':
            print("All Grades:")
            gradebook.display_grades()

        elif choice == '5':
            print("Exiting GradeBook.")
            break
        else:
            print("Invalid option. Please try again.")
start()