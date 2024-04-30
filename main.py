import json
import pickle

class Stadium:
    def __init__(self, name=None, date=None, state=None, city=None, capacity=None):
        self.name = name
        self.date = date
        self.state = state
        self.city = city
        self.capacity = capacity


    def data_input(self):
        self.name = input("Input stadium name: ")
        self.opening_date = input("Input opening date: ")
        self.country = input("Input country: ")
        self.city = input("Input city: ")
        self.capacity = int(input("Input capacity: "))

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Opening date: {self.opening_date}")
        print(f"Country: {self.country}")
        print(f"City: {self.city}")
        print(f"Capacity: {self.capacity}")

    def save(self, file_name):
        dct = {
            "name": self.name,
            "opening_date": self.opening_date,
            "country": self.country,
            "city": self.city,
            "capacity": self.capacity
        }

        with open(file_name, 'w') as file:
            json.dump(dct, file)

    def load(self, file_name):
        with open(file_name, 'r') as file:
            dct = json.load(file)

        self.name = dct["name"]
        self.opening_date = dct["opening_date"]
        self.country = dct["country"]
        self.city = dct["city"]
        self.capacity = dct["capacity"]

stadium1 = Stadium()
stadium1.data_input()
stadium1.display_info()
stadium1.save("data_1")
stadium1.load("data_1")



class StadiumPickle:
    def __init__(self, name=None, opening_date=None, state=None, city=None, capacity=None):
        self.name = name
        self.opening_date = opening_date
        self.state = state
        self.city = city
        self.capacity = capacity


    def data_input(self):
        self.name = input("Input stadium name: ")
        self.opening_date = input("Input opening date: ")
        self.state = input("Input country: ")
        self.city = input("Input city: ")
        self.capacity = int(input("Input capacity: "))

    def display_info(self):
        print(f"Stadium name: {self.name}")
        print(f"Opening date: {self.opening_date}")
        print(f"Country: {self.state}")
        print(f"City: {self.city}")
        print(f"Capacity: {self.capacity}")

    def save_data_pck(self, data, file_name):
        with open(file_name, "wb") as file:
            pickle.dump(data, file)
        return "Data saved."


    def read_data_pck(self, file_name):
        with open(file_name, "rb") as file:
            read_data = pickle.load(file)
        return read_data


stadium2 = StadiumPickle()
stadium2.data_input()
data = f"Stadium name is {stadium2.name}. It was opened in {stadium2.opening_date}, in {stadium2.state}, in city of {stadium2.city} with capacity of {stadium2.capacity}."
stadium2.display_info()
stadium2.save_data_pck(data, "stadiums.pickle")
stadium2.read_data_pck("stadiums.pickle")


