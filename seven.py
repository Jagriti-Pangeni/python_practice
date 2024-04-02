# f=open("demo.txt","r")
# demo1=f.read()
# print(demo1)

# f=open("demo.txt","w")
# demo2=f.write("I am learning python")
# print(demo2)

# f=open("demo.txt","a")
# demo3=f.write("\nIts being intresting day by day.")
# print(demo3)

# with syntax
# with open("demo.txt","r") as f:
#     demo=f.read()
#     print(demo)

# with open("demo.txt","w") as f:
#     demo2=f.write("new data")
#     print(demo2)    
# def replace():
#     with open("demo.txt","r+") as f:
#         demo=f.read()
#         print(demo)
#         demo1=demo.replace("Java","python")
#         print(demo1)
# replace() 

# def search(word):
#     with open("demo.txt","r") as f:
#         demo=f.read()
#         if (word in demo):
#             print(word,"found at line no.")
#             return True
#         else:
#             print(word,"not found.")
#             return False    
# # def checkline():
# #     with open("demo.txt","r") as f:
# #         data1=True
# #         line=1
# #         while data1:
# #             data1=f.readline()
# #             if(word in data1):
# #                 return line

# search("Java")      
# # checkline()              

# def func():
#     count=0
#     with open("demo.txt","r") as f:
#         nums=f.read()
#         print(nums)
#         if(nums%2==0):
#             count+=1
#         print(count)    
# func()