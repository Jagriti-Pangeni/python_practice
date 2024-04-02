# # guess the number project
# import random
# print("Guess the right number between 1-100")
# target = random.randint(1,100)
# first=int(input("What's your initial guess?"))
# if(first==target):
#     print("Congratulations! You have guessed the number in your first guess.")

# else:
#     number=0
#     list=[]
#     while(number!=target):
#         print("oppps! That's the wrong guess")
#         number=int(input("Enter your guess again:"))
#         if(target>number):
#             print("The number is greater than",number)
#         else:
#             print("The number is smaller than",number)    
#         list.append(number)

#     a=len(list)
#     print("You guessed the number right in",a,"times")

#     print("Your score is ",100-a)    
# import string
# import random
# list=""
# passlen=int(input("Enter your desire password length:"))
# # while(num!=passlen):
# char= string.ascii_letters+string.digits+string.punctuation
# #     passw=random.choice(char)
# #     num+=1
# #     list+=passw

# passlen=int(input("Enter your desire password length:"))
# res="".join([random.choice(char) for a in range(passlen)])
# print("your password is",res)
# print("Your password is ",list)

# Unit converter
# program to convert meter to km
class Converter:
    def __init__(self,data=1):
        self.data=data

    def convert(self):
        km=self.data/1000
        print(self.data,"meter =",km,"kilometer")

c1=Converter(3)
c1.convert()