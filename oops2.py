# Create a class called BankAccount with attributes balance and account_number. Implement a method withdraw() to deduct money from the account. Ensure that if the withdrawal amount exceeds the balance, an appropriate exception is raised.

class Bankaccount:
    def __init__(self,balance,acc_nu):
        self.balance=balance
        self.acc_nu=acc_nu
        print("Your new balance is :",self.balance)    

    def withdraw(self,withdraw_amt):
        if(withdraw_amt>=self.balance):
            print("Err! You can't withdraw more amount than your balance")
            return
        self.balance-=withdraw_amt
        print("Your new balance is:",self.balance)

    def deposit(self,deposit_amt):
        self.balance+=deposit_amt
        print("Your new balance is:",self.balance)

# Define a class called Vector that represents a 3-dimensional vector. Implement the __add__() method to allow addition of two vectors and the __mul__() method to allow scalar multiplication of a vector.
        
class Vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k

    def show(self):
        print(self.i,"i +",self.j,"j +",self.k,"k")    

    def __add__(self,vec2):
        newVec_i=self.i+vec2.i
        newVec_j=self.j+vec2.j
        newVec_k=self.k+vec2.k

        return Vector(newVec_i,newVec_j,newVec_k)

    def __mul__(self,S_F):
        newVec_i=self.i*S_F
        newVec_j=self.j*S_F
        newVec_k=self.k*S_F

        return Vector(newVec_i,newVec_j,newVec_k)
# c1=Vector(1,2,3)
# c1.show()
# c2=Vector(4,5,6)
# c2.show()
# c3=c1+c2
# c3.show()
# c4=c3*5
# c4.show()
    
#Implement a class called MathUtils with static methods add() and multiply() that take two numbers as arguments and return their sum and product respectively. Also, create a class method average() that calculates the average of a list of numbers. 
class Mathutils:
    def __init__(self):
        print("Math...")

    @staticmethod
    def add(a,b):
        print("sum:",a+b)

    def mul(a,b):
        print("Product:",a*b)    

    def avg(list):
        for value in list:
            sum=0
            sum+=list[value]
        avg=sum/len(list)    
        print("Average:",avg)
c1=Mathutils
c1.add(1,2)        
c1.mul(2,3)
c1.avg([1,2,3,4,5,6])