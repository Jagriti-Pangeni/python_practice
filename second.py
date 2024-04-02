# for loop practice
# printing even numbers between 20 and 30.
# for number in range(21,31):
#     if number%2==0:
#         print(number)
# Calculate the sum of numbers from 1 to 100 using a for loop.
# num=0
# for number in range(0,101):
#     num+=number+1
# print(num)
# Print numbers from 10 to 1 in reverse order using a for loop.
# for number in range(11,0,-1):
#     print(number)
# Generate the multiplication table for a given number (e.g., 5) using a for loop.
# num=0
# for number in range(0,11,1):
#     num=number*5
#     print("5*",number,"=",num)
# Write a program to calculate the factorial of a number using a for loop.
# num=int(input("enter a number"))
# fact=1
# print("printing the factorial of",num)
# for number in range(1,num+1):
#     fact*=number
# print(fact)
# Given a list of numbers, use a for loop to find and print the maximum value.
# numbers= [1,100,1000,45,69,000,45600]
# max_value=0
# for value in numbers:
#     if value>max_value:
#         max_value=value
# print(max_value)        
# Iterate through a string and print each character on a new line using a for loop.
# name="Jagriti Pangeni"
# for value in name:
#     print(value,"\n")
# Create a nested loop to print a pattern of stars (e.g., a triangle).
# hor=int(input("Enter number of rows:"))
# for i in range(1,hor+1): 
#     for j in range(1,i+1):
#         print("*" ,end="")
#     print()    
# Given a list of numbers, use a for loop to square each element in the list and update the list.
# numbers=[1,2,3,4,5,6]
# num=[]
# for value in numbers:
#     value*=value
#     num.append(value)
# print(num) 
# name="jagriti Pangeni"
# print(name.replace("a","don"))
# print(name.capitalize())
# WAP to ask the user their 3 favourite movies and store them in list.
# movies=[]
# mov1=input("Enter your 1st movie:")
# mov2=input("Enter your 2nd movie:")
# mov3=input("Enter your 3rd movie:")
# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)
# print(movies)
# words=["racecar","ma'am","Jagriti"]
# for value in words:
    # print(value.reverse)
# tuples=['litchi','mango','banana','apple']
# print(tuples)
# tuples.append('kiwi')
# print(tuples)
# tuples.sort()
# print(tuples)
# tuples.reverse()
# print(tuples)
list=[1,2,3,4,5]
print(list[2:4])
# strings operators.
str='Hello'
print('w'in str)#returns true if the letter or string inside underscore is inside the given string else false.
print(r'C://python37')#print the statement inside underscore.
print(str*3)#print the string 3 times
print(str[2:4])