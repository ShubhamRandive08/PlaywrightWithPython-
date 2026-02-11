class Demo:
    @staticmethod
    def add():
        print("This is a static method")

    def sub(self):
        print('This is a instance method')


obj = Demo()
obj.add()
obj.sub()