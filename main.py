import json

class Person:
    def __init__(self, name=None, age=None, country=None, city=None, order=None):
        self.name = name
        self.age = age
        self.country = country
        self.city = city
        self.order = order

    def add_info(self):
        self.name = input("Input name: ")
        self.age = int(input("Input age: "))
        self.country = input("Input country: ")
        self.city = input("Input city: ")
        self.order = int(input("Input order number: "))

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Country: {self.country}")
        print(f"City: {self.city}")
        print(f"Order Number: {self.order}")

    def save(self, file_name):
        dct = {
            "name": self.name,
            "age": self.age,
            "country": self.country,
            "city": self.city,
            "order": self.order
        }

        with open(file_name, 'w') as file:
            json.dump(dct, file)



    def load(self, file_name):
        with open(file_name, 'r') as file:
            dct = json.load(file)

        self.name = dct["name"]
        self.age = dct["age"]
        self.country = dct["country"]
        self.city = dct["city"]
        self.order = dct["order"]

    def change_info(self, file_name):
        self.name = input("Input new name: ")
        self.age = int(input("Input new age: "))
        self.country = input("Input new country: ")
        self.city = input("Input new city: ")
        self.order = int(input("Input new order number: "))

        dct = {
            "name": self.name,
            "age": self.age,
            "country": self.country,
            "city": self.city,
            "order": self.order
        }

        with open(file_name, 'w') as file:
            json.dump(dct, file)



person = Person()
person.add_info()
person.display_info()
person.save("data.json")
person.load("data.json")
person.change_info("data.json")


