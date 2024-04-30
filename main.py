import json

class Person:
    def __init__(self, question_1=None, question_2=None, question_3=None, question_4=None, question_5=None):
        self.question_1 = question_1
        self.question_2 = question_2
        self.question_3 = question_3
        self.question_4 = question_4
        self.question_5 = question_5

    def add_info(self):
        self.question_1 = input("1st question: ")
        self.question_2 = int(input("2nd question: "))
        self.question_3 = input("3rd question: ")
        self.question_4 = input("4th question: ")
        self.question_5 = int(input("5th question: "))

    def display_info(self):
        print(f"1st question answer: {self.question_1}")
        print(f"2nd question answer: {self.question_2}")
        print(f"3rd question answer: {self.question_3}")
        print(f"4th question answer: {self.question_4}")
        print(f"5th question answer: {self.question_5}")

    def save(self, file_name):
        dct = {
            "1st question": self.question_1,
            "2nd question": self.question_2,
            "3rd question": self.question_3,
            "4th question": self.question_4,
            "5th question": self.question_5
        }

        with open(file_name, 'w') as file:
            json.dump(dct, file)




number = int(input("How many objects do ypu want to create? "))
for i in range(number):
    person = Person()
    person.add_info()
    person.display_info()
    person.save(f"data_{i+1}.json")



