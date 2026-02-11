class Demo:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_data(self):
        print("Name : ", self.name)
        print("Age : ", self.age)

obj = Demo("Shubham", 25)
obj.print_data();