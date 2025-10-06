#property
class Student:
    def __init__(self,phy,math,chem):
        self.phy = phy
        self.math = math
        self.chem = chem
        #self.percentage = str((self.phy+self.math+self.chem)/3)

   # def calPercentage(self):
   #     self.percentage = str((self.phy+self.math+self.chem)/3)
    
#best way is to use property decorator
    @property
    def percentage(self):
        return str((self.phy+self.math+self.chem)/3)
st1 = Student(98,95,91)
print(st1.percentage)

#when changed
st1.phy = 86
#print(st1.phy)
#st1.calPercentage()
print(st1.percentage) # value of percentage not yet changed


# Dunder functions : underscores used before init (eg: __) i.e double underscore
#polymorphism
class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
    def showNumber(self):
        print(self.real,"i +" , self.img,"j ")

    def __add__(self,num2):
        newreal = self.real+num2.real
        newimg = self.img+num2.img
        return Complex(newreal,newimg)
    
    def __sub__(self,num2):
        newreal = self.real-num2.real
        newimg = self.img-num2.img
        return Complex(newreal,newimg)

num1 = Complex(1,3)
num1.showNumber()
num2 = Complex(4,16)
num2.showNumber()  

#num3 = num1.add(num2)
#num3.showNumber()

num3 = num1+num2
num3.showNumber()

num3 = num1-num2
num3.showNumber()