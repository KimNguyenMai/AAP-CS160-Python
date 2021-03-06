class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def displayData(self):
        print("In paremt class displayData method")
        print(self.name)
        print(self.age)

class Employee(Person):
    def __init__(self, name, age, id):
        #Calling constructor of super class:
        super().__init__(name,age)
        self.empID = id

    def displayData(self):
        print('In child class displayData method')
        print(self.name)
        print(self.age)
        print(self.empID)

#Person class obj
person = Person('John', 40)
person.displayData()

#Employee class obj
emp = Employee('John', 40, 'E005')
emp.displayData()