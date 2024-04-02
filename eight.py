# class Student:
#     collage_name="birendra Multiple campus"
    
#     def __init__(self,fullname):
#         self.name=fullname
#         print("added to the database")
# s1=Student("Jagriti")
# print(s1.name) 
# s2=Student("Samundra")   
# print(s2.name)
# print(s2.collage_name)
# print(Student.collage_name)
# class Student:
#     def __init__(self,phy,chem,maths):
#         self.phy=phy
#         self.chem=chem
#         self.maths=maths
#     def avg(self):
#         print("The average marks is:",(self.phy+self.chem+self.maths)/3)     
# s1=Student(12,13,14)
# s1.avg()


class Account:
    def __init__(self,balance,account_no):
        self.balance=balance
        self.account_no=account_no

    def debit(self,amount):
        self.balance-=amount
        print("Rs.",amount,"was debited.")
        print("total balance=",self.get_balance())

    def credit(self,amount):
        self.balance+=amount
        print("Rs.",amount,"was credited.")     
        print("total balance=",self.get_balance())

    def get_balance(self):
        return self.balance

a1=Account(10000,34521)        
a1.debit(1000)
a1.credit(5000)