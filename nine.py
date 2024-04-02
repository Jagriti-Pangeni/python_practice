# super() method
# class Car:
#     def __init__(self,type):
#         self.type= type

#     @staticmethod
#     def start():
#         print("Car Started")

#     @staticmethod
#     def stop():
#         print("Car stopped")

# class ToyotaCar(Car):
#     def __init__(self,name,type):
#         super().__init__(type)
#         self.name=name
#         super().start()
# c1=ToyotaCar("Pirus","electric")
# print(c1.type)
# property decorator
# class Student:
#     def __init__(self,phy,chem,maths):
#         self.phy=phy
#         self.chem=chem
#         self.maths=maths
#         # self.per=str((self.phy+self.chem+self.maths)/3) + "%"

#     @property
#     def percentage(self):
#         return str((self.phy+self.chem+self.maths)/3) + "%"

# s1=Student(98,93,94)
# print(s1.percentage)       

# s1.phy=86
# # print(s1.phy)

# # print(s1.per)
# print(s1.percentage)

# polymorphism concept
# a program to add two complex numbers
# class Complex:
#     def __init__(self,real,img):
#         self.real=real
#         self.img=img

#     def show(self):
#         print(self.real,"i +",self.img,"j")

#     def __add__(self,num2):
#         newReal=self.real+num2.real
#         newImg=self.img+num2.img
#         return Complex(newReal,newImg)    

#     def __sub__(self,num2):
#         newReal=self.real-num2.real
#         newImg=self.img-num2.img
#         return Complex(newReal,newImg)        
#     def __truediv__(self,num2):
#         newReal=self.real/num2.real
#         newImg=self.img/num2.img
#         return Complex(newReal,newImg) 
#     def __floordiv__(self,num2):
#         newReal=self.real/num2.real
#         newImg=self.img/num2.img
#         return Complex(newReal,newImg) 

# c1=Complex(4,3)            
# c1.show()

# c2=Complex(1,1)
# c2.show()

# c3=c1+c2
# c3.show()

# c4=c1-c2
# c4.show()

# c5=c1/c3
# c5.show()

# c6=c1//c3
# c6.show()
# class Employee:
#     def __init__(self,name,dept,salary,role):
#         self.name=name
#         self.dept=dept
#         self.salary=salary
#         self.role=role

#     def showDetails(self):
#         print("Name of employee:",self.name)
#         print("Department:",self.dept)  
#         print("Salary:",self.salary)    
#         print("Role:",self.role)    

# class Engeenier(Employee):
#     def __init__(self,age):
#         self.age=age
#         super().__init__("Jagriti Pangeni","Product Managment",55000,"Manager")

# e1=Engeenier(20)
# e1.showDetails()

class Order:
    def __init__(self,iteam,price):
        self.iteam=iteam
        self.price=price
    
    def __gt__(self,odr2):
        return self.price>odr2.price

odr1=Order("chips",20)
odr2=Order("Tea",15)       

print(odr1>odr2)