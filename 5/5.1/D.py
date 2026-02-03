class Programmer:

    __POSITIONS = {"Junior": 10, "Middle": 15, "Senior": 20}

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        self.working_hours = 0
        self.salary_per_hour = self.__POSITIONS[grade]
        self.salary = 0

    def rise(self):
        if self.grade == "Junior":
            self.grade = "Middle"
            self.salary_per_hour = 15
        elif self.grade == "Middle":
            self.grade = "Senior"
            self.salary_per_hour = 20
        else:
            self.salary_per_hour += 1

    def work(self, time):
        self.working_hours += time
        self.salary += time * self.salary_per_hour

    def info(self):
        return f"{self.name} {self.working_hours}ч. {self.salary}тгр."


programmer = Programmer("Васильев Иван", "Junior")
programmer.work(750)
print(programmer.info())
programmer.rise()
programmer.work(500)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())
