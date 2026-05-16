class Person:
    def __init__(self, full_name: str, age: int):
        self.full_name = full_name
        self.age = age

    def print_info(self):
        print(f"ФИО: {self.full_name}, Возраст: {self.age}")

class Student(Person):
    def __init__(self, full_name: str, age: int, group_number: str, gpa: float):
        super().__init__(full_name, age)
        self.group_number = group_number
        self.gpa = gpa

    def get_stipend(self) -> int:
        if self.gpa == 5.0:
            return 6000
        elif 0 < self.gpa < 5.0:
            return 4000
        return 0

    def compare_stipend(self, other: 'Student') -> str:
        if self.get_stipend() > other.get_stipend():
            return "Больше"
        elif self.get_stipend() < other.get_stipend():
            return "Меньше"
        return "Равны"

class Postgraduate(Student):
    def __init__(self, full_name: str, age: int, group_number: str, gpa: float, research_title: str):
        super().__init__(full_name, age, group_number, gpa)
        self.research_title = research_title

    def get_stipend(self) -> int:
        if self.gpa == 5.0:
            return 8000
        elif 0 < self.gpa < 5.0:
            return 6000
        return 0
        
