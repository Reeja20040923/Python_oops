"""# Object Oriented Programming System (OOPS)
#default constructors
class Student:
    def __init__(self):
        pass
    

class Student:
    name = "Reeja"
    id = 236
Student_1 = Student()
print(Student_1.name)
print(Student_1.id)

#__init__method:
#parameterized constructor
class Student:
    #class attribute
    college_name = "Kommuri Pratap Reddy Institute of Technology"
    def __init__(self,fullname,id,marks):
        self.name = fullname
        self.id = id
        self.score = marks

    def welcome(self):
        print(f"Welcome to KPRIT ! {self.name}") 

    def get_marks(self):
        return self.score 

Student_1 = Student("Reeja Yaramalla",236,98)
print(Student_1.name) #Reeja Yaramalla
print(Student_1.id)   #236
print(Student_1.score) #98
print(Student_1.college_name)
Student_1.welcome()
print(Student_1.get_marks())

# example 1
class Student:
    def __init__(self,name,marks): 
        self.sname = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi",self.sname,"avg score is:",sum/3)

    # staic method
    @staticmethod
    def hello():
        print("Hello")

s1 = Student("Reeja Yaramalla", [95,98,97])
s1.get_avg()
s1.sname = "Riya"
s1.get_avg()
s1.hello()
"""
# Abstraction
class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
    
    def start(self):
        self.clutch = True
        self.acc = True
        print("Car Started...!!")

Car1 = Car()
Car1.start()
print(Car1.clutch)





