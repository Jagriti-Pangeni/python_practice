# function to print the given string in a reverse order.
# def rev(str):
#     a=str[::-1]
#     print(a)
# str=input("Enter the string you want to reverse:")
# rev(str)
# write a function to take the input of a list and return the sum of all elements.
# list=[11,21,31,42,55,64,71]
# def sum(list):
#     a=0
#     for i in list:
#         a+=i
#     return a
# print(sum(list))        
# Implement a function that checks whether a given number is even or odd and returns the result.
# def oe_check(num):
#     if(num%2==0):
#         print("even")
#     else:
#         print("false")
# oe_check(8)            
# Write a recursive function that calculates the result of raising a base to an exponent.
# def func(base,exponent):
#     if(exponent==0):
#         return 1
#     return base*func(base,exponent-1)
# print(func(12,4))        
# Create a recursive function to check if a given string is a palindrome (reads the same backward as forward).
# def is_palindrome(str):
#     if(len(str)==0 or len(str)==1):
#         return True
#     else:
#         if(str[0]==str[-1]):
#             return is_palindrome(str[1:-1])   
#     return False
# print(is_palindrome("madam"))

# Implement a recursive function to find the GCD of two numbers using the Euclidean algorithm.
# def GCD(x,y):
#     if(y==0):
#         return x
#     return (GCD(y,x%y))    
# print(GCD(56,4))    
# Define a base class called Shape and derive subclasses like Circle, Rectangle, and Triangle. Implement methods to calculate the area and perimeter for each shape.
# import math
# class Circle:
#     def __init__(self,radius):
#         self.radius=radius

#     def area(self):
#         print("area of circle")
#         return math.pi*self.radius**2 
#     def perimeter(self):
#         print("perimeter of circle=",2*math.pi*self.radius) 
# class Rectangle:
#     def __init__(self,side1,side2):
#         self.side1=side1
#         self.side2=side2

#     def area(self):
#         print("area of rectangle=",self.side1*self.side2)   

#     def perimeter(self):
#         print("perimeter of rectangle=",2*(self.side1+self.side2))                   
# c1=Circle(3)        
# print(c1.area())
# c1.perimeter()

# r1=Rectangle(2,3)
# r1.area()
# r1.perimeter()
# Create a Python class representing a restaurant. Include methods to add dishes, remove dishes, and calculate the total bill.
class Resturant:
    def __init__(self):
        pass

    def add_dishes(self):
                     