# class DemoClass:
#     """
    # This is a demo class to illustrate object-oriented programming concepts.
    # """
# print(DemoClass.__doc__)

class DemoClass:
    """
    This is a demo class to illustrate object-oriented programming concepts.
     It has a class variable, an instance variable, and a method.
     The class variable is shared among all instances of the class, while the instance variable is unique to each instance.
     The method is used to display the values of the class variable and the instance variable.
    """
    num = 10

    def dis(self):
        print("Number : ", self.num)

obj1 = DemoClass()
obj1.dis()

