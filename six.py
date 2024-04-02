# functions in python
# def add(a,b):
#     sum=a+b
#     print(sum)

# add(2,3)
# add(4,5)
# add(1000,400)

# a function to calculate the average of 3 numbers.
# def avg(a,b,c):
#     return((a+b+c)/3)
# print(avg(3,4,5)) 
# print(avg(10,20,30))   
# a function to print the length of list
# alphabets=["a","b","c"]
# numbers=[1,2,3,4,5,6]

# def length(list):
#     print(len(list))
# length(alphabets)
# length(numbers)   
# a function to print the factorial of n number n is the parameter

# n=int(input("enter a number:"))
# def fact(a):
#     i=1
#     for value in range(1,a+1,1):
#         i*=value
#     print(i)
# fact(n)

# write a function to convert USD to NRS.
# def converter(a):
#     nrs=a*110.4352
#     return nrs
# print(converter(312))    
# write a fnction which decides if the passed arguments is odd or even
# def checker(a):
#     if(a%2==0):
#         print("even")
#     else:
#         print("odd")
# checker(599)  
# recursion      
# def show(n):
#     if(n==0):
#         return
#     print(n)
#     show(n-1)
#     print("end",n)
# show(5)    
# factorial through recursion
# def fact(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n*fact(n-1)    
# print(fact(7))
# fibonacci series
# list=[]
# def fibb(n):
#     if(n==0):
#         return 0
#     elif(n==1):
#         return 1
#     return fibb(n-1)+fibb(n-2)
# print(fibb(16))
# sum of first natural numbers using recursion.
# def sum(n):
#     if(n==1):
#         return 1
#     return n+sum(n-1)

# print(sum(100))  
#recursive functions to print all the elements in a list.
