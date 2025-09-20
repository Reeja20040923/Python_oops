class Student:
    def __init__(self,name):
        self.sname = name
s1 = Student("Reeja")
#del s1 # delete keyword
print(s1.sname)       

# Private attributes 
class Account:
    def __init__(self,accno,accpass):
        self.acc_no = accno
        self.__acc_pass = accpass

    def __reset_pass(self):
        print(Account1.acc_pass)

    def __hello(self):
        print("Hello new user!!")

    def welcome(self):
        self.__hello()

Account1 = Account(12345 , 14671467) 
print(Account1.acc_no)
print(Account1.welcome())


# Inheritance
class Car:
    def __init__(self , Type):
        self.type = Type

    color = "White"
    @staticmethod
    def start():
        print("Car started ....")

    @staticmethod
    def stop():
        print("Car stopped ! ! !")

# Single Inheritance
class Toyotacar(Car):
    def __init__(self,name ,type):
        self.name = name
        super().__init__(type)
        super().start()
car1 = Toyotacar("Fortuner","electric")
car2 = Toyotacar("Brizo" , "Diese")
print(car1.name)
print(car1.start())
print(car1.color)
print(car1.type)


# Multi-level Inheritance
class Toyotacar(Car):
    def __init__(self,brand):
        self.brand = brand

class Fortuner(Toyotacar):
    def __init__(self , type ):
        self.type = type


car1 = Fortuner("Diesel")
car1.start()


#Multiple Inheritance
class A:
    varA = "Welcome to class A"

class B:
    varB = "welcome to class B"

class C(A,B):
    varC = "welcome to class C"

c1 = C()
print(c1.varA)
print(c1.varB)
print(c1.varC)


